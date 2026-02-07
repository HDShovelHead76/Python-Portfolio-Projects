# CLI AI Agent with Langchain & Todoist

**Developer:** StackDevOps8999  
**Technologies:** Python 3.13, Langchain, Google Gemini AI, Todoist API  
**Status:** Complete ✅

---

## 🎯 Overview

A command-line AI agent that combines task management with general knowledge through Langchain's agent framework. Powered by Google Gemini AI, this intelligent assistant manages your Todoist tasks while answering any questions you throw at it - all through a conversational CLI interface.

This project demonstrates:
- **Langchain Agent Architecture:** Multi-tool agent with function calling
- **Dual-Purpose AI:** Task management + general knowledge base
- **CLI Interface:** Interactive command-line experience
- **API Integration:** Todoist for productivity, Gemini for intelligence
- **Conversational Memory:** Context-aware responses across interactions
- **Error Handling:** Graceful API failure management

---

## ✨ Key Features

### **🤖 Langchain Agent Framework**
- **5 Integrated Tools:** Task creation, listing, updating, deletion, and general Q&A
- **OpenAI-Style Tools:** Function calling with structured parameters
- **Agent Executor:** Intelligent tool selection based on user intent
- **Memory Management:** Maintains conversation history for context
- **Verbose Mode:** See the agent's reasoning process in real-time

### **📋 Todoist Task Management**
- **Add Tasks:** Create new tasks with optional descriptions
- **List Tasks:** View all active tasks with IDs
- **Update Tasks:** Modify task content or descriptions by ID
- **Delete Tasks:** Remove completed or unwanted tasks
- **Natural Language:** "Add task to buy groceries" → Creates Todoist task

### **🧠 General Knowledge Base**
- **Universal Q&A:** Answer questions on any topic via Google Gemini
- **Recipe Suggestions:** "What can I make with chicken and rice?"
- **Planning Help:** "Plan a weekend trip to Boston"
- **Factual Information:** "Why are apples red?"
- **Creative Ideas:** "Give me startup ideas for 2026"

### **💬 Conversational CLI**
- **Interactive Loop:** Continuous conversation until "exit" or "quit"
- **Greeting Message:** "Hello Warrior, command your tasks (or ask anything):"
- **Real-Time Responses:** Agent reasoning displayed in verbose mode
- **Error Handling:** Safe API calls with user-friendly error messages
- **Rate Limiting:** Built-in 6-second delay to respect API limits

### **🔒 Secure Configuration**
- **Environment Variables:** API keys stored in `.env` file
- **Template Provided:** `.env.example` for easy setup
- **No Hardcoded Secrets:** Production-ready security practices
- **Git Protection:** `.gitignore` prevents credential leaks

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.13 | Core programming language |
| **Langchain** | 0.2.0+ | Agent framework and orchestration |
| **Langchain Google GenAI** | 0.1.0+ | Google Gemini AI integration |
| **Google Gemini AI** | 2.5 Flash | Large language model for responses |
| **Todoist API** | 2.2.0+ | Task management integration |
| **python-dotenv** | 1.0.0+ | Environment variable management |
| **Pydantic** | 2.0.0+ | Data validation for tool parameters |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))
- Todoist API key ([Get one here](https://todoist.com/app/settings/integrations/developer))
- pip package manager

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
   cd Python-Portfolio-Projects/early-projects/cli-ai-agent-langchain
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # OR
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Configure `.env` file:**
   ```bash
   # Google Gemini API Key
   GEMINI_API_KEY=AIza...your-key-here
   
   # Todoist API Key
   TODOIST_API_KEY=your-todoist-token-here
   ```

6. **Run the agent:**
   ```bash
   python main.py
   ```

---

## 🚀 Usage

### **Starting the Agent:**

```bash
python main.py
```

You'll see:
```
Hello Warrior, command your tasks (or ask anything):
```

### **Example Interactions:**

#### **Task Management:**

**Create a Task:**
```
> Add a task to review Python documentation
✅ Task 'Review Python documentation' added
```

**List All Tasks:**
```
> Show me my tasks
- Review Python documentation (id: 8123456789)
- Buy groceries (id: 8123456790)
```

**Update a Task:**
```
> Update task 8123456789 to "Read Python advanced features"
✏️ Task 8123456789 updated.
```

**Delete a Task:**
```
> Delete task 8123456791
🗑️ Task 8123456791 deleted.
```

#### **General Knowledge:**

**Factual Questions:**
```
> Why are apples red?
Apples are red due to pigments called anthocyanins, which are produced 
during the ripening process. As an apple ripens, the green chlorophyll 
breaks down, allowing the red anthocyanins to become visible...
```

**Recipe Ideas:**
```
> What can I make with chicken, rice, and broccoli?
You can make a delicious chicken and broccoli stir-fry! Cook the chicken 
in a pan with garlic and ginger, add steamed broccoli, and serve over 
fluffy rice...
```

**Planning Help:**
```
> Help me plan a productive morning routine
A great morning routine starts with waking up at a consistent time. 
Begin with 10 minutes of meditation or stretching, followed by a healthy 
breakfast. Review your tasks for the day and prioritize the top 3...
```

#### **Exit:**
```
> exit
👋 Goodbye, Warrior!
```

---

## 📁 Project Structure

```
cli-ai-agent-langchain/
├── main.py                         # Main application with agent logic
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .gitignore                      # Git exclusion patterns
└── README.md                       # This file
```

---

## 🔧 Configuration

### **Environment Variables (.env)**

```bash
# Google Gemini API Key
# Get one at: https://aistudio.google.com/app/apikey
GEMINI_API_KEY=your-gemini-api-key-here

# Todoist API Key
# Get one at: https://todoist.com/app/settings/integrations/developer
TODOIST_API_KEY=your-todoist-api-key-here
```

### **Agent System Prompt**

Defined in `main.py`:

```python
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful assistant that manages tasks via Todoist. "
     "For task operations, always use tools. For general queries, "
     "use the 'general_info' tool."),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
    MessagesPlaceholder("history")
])
```

**Customization:** Modify the system message to change agent behavior.

### **LLM Configuration**

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",        # Fast, efficient model
    google_api_key=gemini_api_key,
    temperature=0.7,                  # Balanced creativity
)
```

**Options:**
- `temperature`: 0.0 (deterministic) to 1.0 (creative)
- `model`: `gemini-2.5-flash` (fast) or `gemini-pro` (advanced)

---

## 🎓 Architecture Deep Dive

### **Langchain Agent Flow:**

```
User Input (CLI)
    ↓
Agent Executor
    ↓
Tool Selection
    ├── add_task (Todoist API)
    ├── show_tasks (Todoist API)
    ├── update_task (Todoist API)
    ├── delete_task (Todoist API)
    └── general_info (Gemini LLM)
    ↓
Tool Execution
    ↓
Response Generation
    ↓
CLI Output
    ↓
[6 second delay]
    ↓
Next Input Prompt
```

### **Tools Breakdown:**

```python
# 1. Task Creation
@tool
def add_task(task: str, desc: str = ""):
    """Add a new task to the user's Todoist list."""
    # Creates task via Todoist API

# 2. Task Listing
@tool
def show_tasks():
    """Show all tasks in the user's Todoist list."""
    # Retrieves and formats all active tasks

# 3. Task Update
@tool
def update_task(task_id: str, new_task: str = None, new_desc: str = None):
    """Update a task's content or description by ID."""
    # Modifies existing task

# 4. Task Deletion
@tool
def delete_task(task_id: str):
    """Delete a task by ID."""
    # Removes task from Todoist

# 5. General Knowledge
@tool
def general_info(query: str):
    """Answer general questions (recipes, facts, ideas, planning help)."""
    # Delegates to Gemini for natural language response
```

### **Error Handling Pattern:**

```python
def safe_api_call(func, *args, **kwargs):
    """DRY helper for safe API calls with error handling."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return f"❌ Error: {str(e)}"
```

**Benefits:**
- Prevents crashes on API failures
- User-friendly error messages
- Single point of error handling (DRY principle)

---

## 🎯 Learning Objectives Demonstrated

This project showcases proficiency in:

✅ **AI/ML Integration:**
- Langchain agent framework
- Multi-tool orchestration
- Function calling patterns
- Conversational memory
- LLM integration (Google Gemini)

✅ **CLI Development:**
- Interactive command loops
- User input handling
- Real-time output display
- Graceful exit handling

✅ **API Integration:**
- Todoist REST API
- Google Gemini API
- Authentication (Bearer tokens)
- Error handling and retry logic
- Rate limiting strategies

✅ **Software Engineering:**
- Environment-based configuration
- DRY principles (safe_api_call)
- Tool abstraction patterns
- Security best practices
- Clean code organization

---

## 🔒 Security Notes

**⚠️ Important Security Considerations:**

This application implements several security best practices:

- **Environment Variables:** All API keys stored in `.env` file
- **Git Protection:** `.gitignore` prevents credential commits
- **No Hardcoded Secrets:** Production-ready configuration
- **Safe API Calls:** Error handling prevents credential exposure
- **Input Validation:** Pydantic validates tool parameters

**Security Audit Status:**
- ✅ Zero critical vulnerabilities
- ✅ No hardcoded API keys
- ✅ Proper `.gitignore` configuration
- ✅ Environment variable validation
- ✅ Safe error handling

**For Production Deployment:**
- Use strong API keys (rotate regularly)
- Enable HTTPS for web-based versions
- Implement rate limiting per user
- Add logging for security audits
- Regular dependency updates

---

## 🧪 Testing

### **Manual Testing Checklist:**

**Basic Functionality:**
- [ ] Agent starts without errors
- [ ] Can add tasks to Todoist
- [ ] Can list all tasks
- [ ] Can update task by ID
- [ ] Can delete task by ID
- [ ] Can answer general questions

**Tool Selection:**
- [ ] Agent chooses correct tool for task operations
- [ ] Agent uses general_info for questions
- [ ] Agent maintains context across turns
- [ ] Verbose mode shows reasoning

**Error Handling:**
- [ ] Invalid task ID shows error
- [ ] Missing API keys show clear message
- [ ] Network errors handled gracefully
- [ ] Invalid input doesn't crash agent

**Memory:**
- [ ] Agent remembers previous tasks
- [ ] Context maintained across conversation
- [ ] Session ID properly configured

### **Example Test Commands:**

```bash
# Task Management
"Add a task to study Python"
"Show my tasks"
"Update task [ID] to 'Study advanced Python'"
"Delete task [ID]"

# General Questions
"Why is the sky blue?"
"What should I cook for dinner?"
"Help me plan a workout routine"
"Explain quantum computing"

# Mixed Commands
"Add task to learn Langchain, then explain what Langchain is"
"Show my tasks and suggest which to prioritize"

# Edge Cases
"" (empty input)
"asdfghjkl" (gibberish)
"exit" (should gracefully close)
```

---

## 🚧 Known Limitations

- **CLI Only:** No web interface (command-line use only)
- **Rate Limiting:** 6-second delay between interactions (Gemini free tier)
- **Session Memory:** Resets when script restarts (in-memory storage)
- **Single User:** No multi-user support or authentication
- **Todoist Dependency:** Requires active Todoist account

---

## 🔮 Future Enhancements

### **Potential Improvements:**

**CLI Enhancements:**
- [ ] Rich text formatting (colors, tables)
- [ ] Auto-completion for commands
- [ ] Command history (up/down arrows)
- [ ] Progress bars for long operations
- [ ] Help command with tool descriptions

**Web Interface:**
- [ ] Flask/Django web UI
- [ ] REST API endpoints
- [ ] WebSocket for real-time updates
- [ ] Multi-user sessions

**Advanced Features:**
- [ ] Task prioritization (AI-suggested)
- [ ] Natural language date parsing ("tomorrow", "next week")
- [ ] Recurring task support
- [ ] Project organization (Todoist projects)
- [ ] Task labels and filters
- [ ] Calendar integration (Google Calendar)
- [ ] Email notifications

**AI Improvements:**
- [ ] Personality customization
- [ ] Voice input/output
- [ ] Image analysis (Gemini Vision)
- [ ] Document upload and analysis
- [ ] Web search tool (real-time info)
- [ ] Code execution tool

---

## 🐛 Troubleshooting

### **Common Issues:**

**Problem:** "Invalid API key" error  
**Solution:** Verify GEMINI_API_KEY and TODOIST_API_KEY in `.env` are correct

**Problem:** Tasks not appearing  
**Solution:** Check Todoist web app - API changes may take a few seconds to sync

**Problem:** Agent not responding  
**Solution:** Check terminal for errors, ensure `.env` file exists with valid keys

**Problem:** "ModuleNotFoundError: No module named 'langchain'"  
**Solution:** Activate virtual environment and run `pip install -r requirements.txt`

**Problem:** Rate limit errors  
**Solution:** Increase delay in `time.sleep(6)` to 10-15 seconds

---

## 📧 Contact

**Developer:** StackDevOps8999  
**GitHub:** [HDShovelHead76](https://github.com/HDShovelHead76)  
**Portfolio:** [Python Portfolio Projects](https://github.com/HDShovelHead76/Python-Portfolio-Projects)

---

## 📄 License

This project is part of a learning portfolio and is available for educational purposes.

---

## 🙏 Acknowledgments

- Powered by **Google Gemini AI** for natural language understanding
- Built with **Langchain** agent framework for tool orchestration
- Integrated with **Todoist API** for task management
- Demonstrates CLI-based AI agent architecture with multi-tool integration
- Part of ongoing AI/ML software development learning journey

---

## 📝 Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
cd Python-Portfolio-Projects/early-projects/cli-ai-agent-langchain
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env  # Add your GEMINI_API_KEY and TODOIST_API_KEY

# Run the agent
python main.py
```

---

**Note:** This is an educational AI project demonstrating CLI AI agent and Langchain multi-tool agent architecture. Google Gemini API key and Todoist API key required. Try managing your tasks or ask about anything - "Hello Warrior" combines productivity with knowledge! 🤖⚡
