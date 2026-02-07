from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
import json
import requests

# LangChain & Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain.tools import tool

# --- Load .env ---
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
todoist_api_key = os.getenv("TODOIST_API_KEY")


# --- System Prompt ---
system_prompt = """
You are Einstein 🧠, witty and humorous 😄.
Answer all types of messages — questions, greetings, thanks, small talk.
Use 2–5 sentences.
If the user asks you to remember something as a task, call the Todoist tool.
"""


# --- LLM ---
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.5,
)

# --- Tools ---
@tool
def add_todo_task(task: str) -> str:
    """Add a task to Todoist 📋"""
    if not todoist_api_key:
        return "⚠️ Todoist API key missing."
    url = "https://api.todoist.com/rest/v2/tasks"
    headers = {"Authorization": f"Bearer {todoist_api_key}"}
    payload = {"content": task}
    try:
        r = requests.post(url, headers=headers, json=payload)
        if r.status_code in [200, 204]:
            return f"✅ Task added: {task}"
        else:
            return f"⚠️ Failed to add task: {task} (status {r.status_code})"
    except Exception as e:
        return f"⚠️ Exception adding task: {str(e)}"


tools = [add_todo_task]

# --- Prompt Template ---
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
    MessagesPlaceholder("history"),
])

# --- Agent ---
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# --- Memory Wrapper ---
chat_history = ChatMessageHistory()
agent_with_history = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: chat_history,
    input_messages_key="input",
    history_messages_key="history",
)


# --- Views ---
def home(request):
    return render(request, "chat.html")


def chat(request):
    return render(request, "chat.html")


@csrf_exempt
def ask_einstein(request):
    """AJAX POST endpoint for Einstein chat, fully robust for quotes and special characters"""
    if request.method == "POST":
        try:
            # Decode JSON safely
            data = json.loads(request.body.decode("utf-8"))
            user_input = data.get("message", "")
        except Exception:
            user_input = request.body.decode("utf-8").strip()

        if not user_input:
            return JsonResponse({"reply": "🤔 I didn’t catch that."})

        # Only escape quotes, leave parentheses, emojis, etc.
        safe_input = user_input.replace('"', '\\"').replace("'", "\\'")

        try:
            response = agent_with_history.invoke(
                {"input": safe_input},
                config={"configurable": {"session_id": "einstein"}},
            )
        except Exception as e:
            return JsonResponse({"reply": f"⚠️ Error processing input: {str(e)}"})

        reply = response.get("output", str(response))
        return JsonResponse({"reply": reply})

    return JsonResponse({"reply": "⚠️ Only POST supported."}, status=405)
