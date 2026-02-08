# 🧠 Einstein CLI Agent

An interactive command-line AI assistant powered by Google's Gemini LLM and LangChain agent framework, featuring Albert Einstein's personality and conversational memory. Built to demonstrate advanced agent architecture, session-based chat history, and custom system prompts for personality-driven interactions.

## 🎯 Project Overview

This application creates a conversational AI agent that embodies Albert Einstein's voice, reasoning style, and personality. Using LangChain's agent executor framework with Google Gemini 2.5 Flash, the agent maintains conversation context across multiple exchanges, responds with Einstein's characteristic wit and wisdom, and shares personal anecdotes naturally within responses.

**Use Case:** Educational tool, conversational AI demonstration, or interactive learning companion that makes complex topics approachable through Einstein's engaging personality and storytelling approach.

## ✨ Key Features

- **Personality-Driven Responses** - Custom system prompt configures Einstein's voice, humor, and personal storytelling
- **Conversational Memory** - LangChain message history maintains context across the entire session
- **Agent Architecture** - Uses LangChain's agent executor pattern for extensible tool integration
- **Session Management** - Implements `RunnableWithMessageHistory` for proper conversation threading
- **Google Gemini Integration** - Leverages Gemini 2.5 Flash model for fast, intelligent responses
- **Interactive CLI** - Clean terminal-based conversation loop with user-friendly prompts
- **Environment Security** - API keys loaded from `.env` file using python-dotenv
- **Verbose Logging** - Optional agent executor verbosity for debugging and learning

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.x |
| **LangChain** | Agent framework and orchestration | 0.3.x |
| **LangChain Core** | Core abstractions (prompts, runnables) | 0.3.x |
| **LangChain Google GenAI** | Google Gemini LLM integration | 2.x |
| **LangChain Community** | Community tools (chat message history) | 0.3.x |
| **Google Gemini** | Large language model (Gemini 2.5 Flash) | API |
| **python-dotenv** | Environment variable management | 1.x |

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))
- pip package manager

### Setup Instructions

1. **Clone or download this repository**
```bash
   cd einstein-cli-agent
```

2. **Create a virtual environment (recommended)**
```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Configure API credentials**
   
   Create a `.env` file in the project root:
```bash
   cp .env.example .env
```
   
   Edit `.env` and add your Gemini API key:
```
   GEMINI_API_KEY=your_actual_gemini_api_key_here
```

## 🚀 Usage

### Running the Agent

1. **Start the conversational agent**
```bash
   python main.py
```

2. **Interact with Einstein**
```
   👋 Hi, I am Albert! How can I help you today?
   Hello Warrior, what's on your mind today? What is relativity?
   
   Albert 🤓: Ah, relativity! My favorite topic...
```

3. **Exit the conversation**
   - Type `exit` or `quit` to end the session

### Example Interactions

**Question about Physics:**
```
You: Explain quantum mechanics simply
Albert 🤓: Ah, quantum mechanics! It troubled me greatly at times. 
You see, God does not play dice with the universe, yet the quantum 
world seems to delight in probability and uncertainty. Imagine a cat 
that is both alive and dead until you peek—absurd, yes? That's the 
essence of superposition! ðŸ˜„
```

**Personal Anecdotes:**
```
You: Tell me about your work
Albert 🤓: My years at the Swiss Patent Office were formative! While 
examining inventions, my mind wandered to the nature of time and 
space. That humble office gave me the freedom to think deeply about 
the universe. Sometimes the best discoveries come when you're 
supposed to be working on something else! ðŸ˜„
```

## 🏗️ Project Architecture

### System Design
```
User Input
    ↓
LangChain Agent Executor
    ↓
ChatPromptTemplate (System + History + User)
    ↓
Google Gemini 2.5 Flash LLM
    ↓
Agent Response
    ↓
ChatMessageHistory (Session Memory)
    ↓
Console Output
```

### Core Components

**1. Environment Configuration**
```python
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
```
- Loads API credentials securely from `.env` file
- Prevents hardcoded secrets in source code

**2. System Prompt (Personality Definition)**
```python
system_prompt = """
You are Einstein 🧠.
Answer questions through Einstein's voice and reasoning...
You will speak from your point of view and share personal stories
even when not directly asked.
Keep answers 2–5 sentences and include humor 😄.
"""
```
- Defines agent personality and behavioral constraints
- Instructs response length and tone
- Encourages personal anecdotes and humor

**3. LLM Initialization**
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.5,
)
```
- Configures Google Gemini model connection
- Sets temperature for balanced creativity/consistency
- Uses fast Flash variant for responsive interactions

**4. LangChain Prompt Template**
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
    MessagesPlaceholder("history"),
])
```
- Structures conversation with system prompt, user input, and history
- `agent_scratchpad` - Reserved for tool usage thoughts
- `history` - Stores previous conversation turns

**5. Agent Creation**
```python
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```
- Creates agent capable of tool usage (currently no tools defined)
- `verbose=True` enables debugging output showing agent reasoning
- Agent executor manages the execution loop

**6. Conversational Memory**
```python
chat_history = ChatMessageHistory()
agent_with_history = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: chat_history,
    input_messages_key="input",
    history_messages_key="history",
)
```
- `ChatMessageHistory` stores conversation turns in memory
- `RunnableWithMessageHistory` wraps executor with session-based memory
- Session ID enables multiple concurrent conversations (future expansion)

**7. Interactive Loop**
```python
while True:
    user_input = input("Hello Warrior, what's on your mind today? ")
    if user_input.lower() in ["exit", "quit"]:
        break
    
    response = agent_with_history.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "einstein"}},
    )
    
    print(f"Albert 🤓: {response['output']}")
    time.sleep(2)
```
- Continuous conversation loop with exit handling
- Invokes agent with session configuration
- 2-second delay prevents API rate limiting

## 🎓 Learning Objectives

This project demonstrates proficiency in:

### LangChain Framework
- **Agent Architecture** - Understanding agent executors and tool integration patterns
- **Prompt Engineering** - Crafting effective system prompts with message placeholders
- **Memory Management** - Implementing conversational context with `ChatMessageHistory`
- **Runnables** - Using `RunnableWithMessageHistory` for stateful conversations
- **Session Handling** - Configuring session IDs for multi-user scenarios

### LLM Integration
- **API Authentication** - Secure credential management with environment variables
- **Model Configuration** - Selecting appropriate models and temperature settings
- **Response Handling** - Parsing and displaying agent outputs
- **Rate Limiting** - Implementing delays to respect API quotas

### Python Development
- **CLI Design** - Creating user-friendly terminal interfaces
- **Loop Control** - Managing infinite loops with graceful exit conditions
- **Exception Handling** - Robust error management (implicit in LangChain)
- **Code Organization** - Structured script with clear component separation

### AI Agent Concepts
- **Personality Prompts** - Designing system instructions for consistent character voice
- **Context Windows** - Managing conversation history within token limits
- **Tool Readiness** - Architecture prepared for future tool integration
- **Verbose Logging** - Debugging agent reasoning and decision-making

## 🔒 Security Notes

- ✅ API keys loaded from `.env` file (never committed to version control)
- ✅ `.env` included in `.gitignore` to prevent accidental exposure
- ✅ `.env.example` template provided for easy setup
- ✅ No hardcoded credentials in source code
- ⚠️ **Important:** Keep your `.env` file private and never share API keys publicly

### .gitignore Configuration
Ensure your `.gitignore` includes:
```
.env
.env.*
!.env.example
```

## 🚧 Future Enhancements

Potential improvements for extended functionality:

### Tool Integration
- [ ] **Web Search Tool** - Enable Einstein to search for current information
- [ ] **Calculator Tool** - Perform mathematical calculations on demand
- [ ] **Wikipedia Tool** - Fetch historical context and biographical data
- [ ] **Code Interpreter** - Execute Python code for demonstrations

### Memory & Persistence
- [ ] **Persistent Storage** - Save conversations to SQLite or JSON files
- [ ] **Conversation Retrieval** - Load and continue previous sessions
- [ ] **Summary Generation** - Periodic conversation summaries for long chats
- [ ] **Memory Optimization** - Implement sliding window for token management

### User Experience
- [ ] **Multi-Personality Mode** - Switch between historical figures (Einstein, Curie, Tesla)
- [ ] **Rich Terminal UI** - Use `rich` library for colored, formatted output
- [ ] **Conversation Export** - Save transcripts as text or markdown files
- [ ] **Voice Input/Output** - Integrate speech-to-text and text-to-speech

### Advanced Features
- [ ] **Multi-Turn Planning** - Complex reasoning across multiple steps
- [ ] **Document QA** - Upload PDFs and ask Einstein questions about content
- [ ] **Image Understanding** - Integrate Gemini Vision for image-based questions
- [ ] **Web Interface** - Build Streamlit or Flask frontend for browser access

## 🐛 Troubleshooting

### Common Issues

**Problem:** `AuthenticationError: Invalid API key`
- **Solution:** Verify your Gemini API key in `.env` file is correct and active

**Problem:** `ImportError: No module named 'langchain'`
- **Solution:** Activate virtual environment and reinstall: `pip install -r requirements.txt`

**Problem:** Agent responses are slow or timeout
- **Solution:** Check internet connection; consider switching to faster model or reducing conversation history

**Problem:** `KeyError: 'GEMINI_API_KEY'`
- **Solution:** Ensure `.env` file exists in project root with proper key name

**Problem:** Agent gives generic responses (not Einstein-like)
- **Solution:** Review system prompt; increase temperature for more personality (0.7-0.9)

**Problem:** Memory not persisting between messages
- **Solution:** Verify `RunnableWithMessageHistory` configuration; check session_id is consistent

**Problem:** `QuotaExceeded` or rate limit errors
- **Solution:** Increase `time.sleep()` delay; check Gemini API quota limits

## 💡 Code Architecture Notes

### Why LangChain Agent Pattern?

This project uses LangChain's agent architecture even though no tools are currently defined. This design choice demonstrates:

1. **Extensibility** - Easy to add tools (web search, calculators, etc.) without refactoring
2. **Industry Standard** - LangChain is widely used for production AI applications
3. **Best Practices** - Separates concerns (prompt, LLM, memory, execution)
4. **Future-Proofing** - Prepared for multi-tool, complex reasoning scenarios

### Alternative Implementation

The code includes a commented-out "Python Memory Wrapper" that achieves similar results with simpler code:
```python
python_history = []  # Custom list-based memory

messages = [{"role": "system", "content": system_prompt}] + python_history + [
    {"role": "user", "content": user_input}
]

response = llm.invoke(messages)
python_history.append({"role": "user", "content": user_input})
python_history.append({"role": "assistant", "content": response.content})
```

**LangChain Advantages:**
- Standardized abstractions
- Built-in session management
- Tool integration support
- Production-ready error handling

**Custom Python Advantages:**
- Simpler to understand for beginners
- Less dependency overhead
- Direct control over memory structure

Both approaches are valid; this project uses LangChain to demonstrate professional framework patterns.

## 📞 Contact & Portfolio

**Developer:** StackDevOps8999  
**GitHub:** [@HDShovelHead76](https://github.com/HDShovelHead76)  
**Portfolio:** [Python Portfolio Projects](https://github.com/HDShovelHead76/Python-Portfolio-Projects)

---

## 📝 License

This project is available for educational and personal use. Feel free to modify and extend for your own learning purposes.

---

*Built as part of Python learning journey - demonstrating LangChain agent architecture, LLM integration, and conversational AI development*
