from dotenv import load_dotenv
import os
import time

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# --- Load keys ---
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# --- Prompt ---
system_prompt = """
You are Einstein 🧠.
Answer questions through Einstein's voice and reasoning...
You will speak from your point of view and share personal stories
even when not directly asked. For example, if asked about relativity,
you might also share your memory of working in the Swiss Patent Office.
Keep answers 2–5 sentences and include humor 😄.
"""

# --- LLM ---
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.5,
)

print("👋 Hi, I am Albert! How can I help you today?")


# ---------------------------------------------------------
# 🧩 LangChain Memory Wrapper
# ---------------------------------------------------------

# --- Tools (none for now) ---
tools = []

# --- LangChain prompt ---
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
    MessagesPlaceholder("history"),
])

# --- Agent + Executor ---
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# --- LangChain Memory wrapper ---
chat_history = ChatMessageHistory()
agent_with_history = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: chat_history,   # memory per session
    input_messages_key="input",
    history_messages_key="history",
)

# --- Interactive Loop ---
print("👋 Hi, I am Albert! How can I help you today?")

while True:
    user_input = input("Hello Warrior, what's on your mind today? ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye, Warrior!")
        break

    response = agent_with_history.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "einstein"}},
    )

    print(f"Albert 🤓: {response['output']}")
    time.sleep(2)

"""
# ---------------------------------------------------------
# 🐍 Python Memory Wrapper (custom, simple)
# ---------------------------------------------------------
python_history = []  # just a list of dicts

while True:
    user_input = input("Big Dawg: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye, Warrior!")
        break

    # Build the conversation context: system + history + user input
    messages = [{"role": "system", "content": system_prompt}] + python_history + [
        {"role": "user", "content": user_input}
    ]

    # Call Gemini
    response = llm.invoke(messages)

    # Show response
    print(f"Albert 🤓: {response.content}")

    # Store to history
    python_history.append({"role": "user", "content": user_input})
    python_history.append({"role": "assistant", "content": response.content})

    # Slow down if needed (avoid hitting quota)
    time.sleep(2)
    """
