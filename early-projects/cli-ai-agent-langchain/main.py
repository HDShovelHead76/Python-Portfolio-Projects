from dotenv import load_dotenv
import os
import time

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from todoist_api_python.api import TodoistAPI

load_dotenv()

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

todoist = TodoistAPI(todoist_api_key)

# --- DRY Helper ---
def safe_api_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --- Tools ---
@tool
def add_task(task: str, desc: str = ""):
    """Add a new task to the user's Todoist list."""
    task_obj = safe_api_call(todoist.add_task, content=task, description=desc)
    if isinstance(task_obj, str):
        return task_obj
    return f"✅ Task '{task}' added with description '{desc}'"

@tool
def show_tasks():
    """Show all tasks in the user's Todoist list."""
    tasks = safe_api_call(todoist.get_tasks)
    if isinstance(tasks, str):
        return tasks
    if not tasks:
        return "📭 No tasks found."
    return "\n".join([f"- {t.content} (id: {t.id})" for t in tasks])

@tool
def update_task(task_id: str, new_task: str = None, new_desc: str = None):
    """Update a task's content or description by ID."""
    updated = safe_api_call(
        todoist.update_task,
        task_id=task_id,
        content=new_task,
        description=new_desc
    )
    if isinstance(updated, str):
        return updated
    return f"✏️ Task {task_id} updated."

@tool
def delete_task(task_id: str):
    """Delete a task by ID."""
    deleted = safe_api_call(todoist.delete_task, task_id)
    if isinstance(deleted, str):
        return deleted
    return f"🗑️ Task {task_id} deleted."

@tool
def general_info(query: str):
    """Answer general questions (recipes, facts, ideas, planning help)."""
    # Delegate directly to Gemini for a natural-language answer
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=gemini_api_key,
        temperature=0.8,
    )
    response = llm.invoke(query)
    return response.content if hasattr(response, "content") else str(response)

tools = [add_task, show_tasks, update_task, delete_task, general_info]

# --- LLM ---
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.7,
)

# --- Prompt ---
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful assistant that manages tasks via Todoist. "
     "For task operations, always use tools. For general queries, "
     "use the 'general_info' tool."),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
    MessagesPlaceholder("history")
])

# --- Agent + Executor ---
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- Memory wrapper ---
chat_history = ChatMessageHistory()
agent_with_history = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: chat_history,
    input_messages_key="input",
    history_messages_key="history"
)

# --- Interactive loop ---
while True:
    user_input = input("Hello Warrior, command your tasks (or ask anything): ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye, Warrior!")
        break

    response = agent_with_history.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "warrior"}}
    )
    print(response["output"])

    time.sleep(6)
