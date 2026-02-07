# Student Management System with MySQL

**Developer:** StackDevOps8999  
**Technologies:** Python 3.13, PyQt5, MySQL, python-dotenv  
**Status:** Complete ✅

---

## 📋 Overview

A desktop GUI application for managing student records with MySQL database backend. Built with PyQt5, this system provides a complete student information management solution with secure credential handling and real-time database synchronization.

This project demonstrates:
- Desktop application development with PyQt5
- MySQL database integration and CRUD operations
- Secure environment-based configuration
- GUI event handling and table widget management
- Input validation and error handling
- Cross-platform compatibility

---

## ✨ Key Features

### **Student Record Management**
- **Add Students:** Create new student records with complete information
- **View Records:** Display all students in interactive table widget
- **Update Information:** Edit existing student details with validation
- **Delete Records:** Remove students with confirmation dialogs
- **Real-time Sync:** Automatic database updates on all operations

### **Search & Filter**
- **Quick Search:** Find students by name, ID, or any field
- **Dynamic Filtering:** Results update as you type
- **Clear Filters:** Reset to view all records instantly

### **Database Features**
- **MySQL Backend:** Reliable relational database for data persistence
- **Auto-Connect:** Automatic connection on application startup
- **Error Handling:** Graceful handling of connection and query errors
- **Transaction Support:** Data integrity with rollback capability

### **Security**
- **Environment Variables:** Secure credential management with `.env`
- **No Hardcoded Passwords:** All sensitive data in environment files
- **Git Protection:** `.gitignore` prevents credential leaks
- **SQL Injection Prevention:** Parameterized queries throughout

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.13 | Core programming language |
| **PyQt5** | Latest | Desktop GUI framework |
| **MySQL** | 8.0+ | Relational database system |
| **mysql-connector-python** | Latest | MySQL database driver |
| **python-dotenv** | 1.0.0 | Environment variable management |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- MySQL Server 8.0+ installed and running
- pip package manager

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
   cd Python-Portfolio-Projects/early-projects/student-management-mysql
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
   # Edit .env with your MySQL credentials
   ```

5. **Configure MySQL database:**
   ```sql
   -- Login to MySQL
   mysql -u root -p
   
   -- Create database
   CREATE DATABASE school;
   
   -- Verify database
   SHOW DATABASES;
   
   -- Exit MySQL
   EXIT;
   ```

6. **Run application:**
   ```bash
   python main.py
   ```
   *Note: Application will auto-create required tables on first run*

---

## 🚀 Usage

### **Run the Application:**

```bash
# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows

# Launch application
python main.py
```

### **Application Interface:**

#### **1. Add New Student**

1. Click **"Add Student"** button in toolbar
2. Fill in student information:
   - **First Name:** Required field
   - **Last Name:** Required field
   - **Email:** Optional, validated format
   - **Phone:** Optional contact number
   - **Student ID:** Unique identifier
3. Click **"Save"** to commit to database
4. Table refreshes automatically with new entry

#### **2. View All Students**

- Main table displays all student records
- Columns: ID, Name, Email, Phone, Enrollment Date
- Click column headers to sort
- Scroll for large datasets

#### **3. Update Student Information**

1. **Select** student row in table
2. Click **"Edit"** button or double-click row
3. Modify fields in edit dialog
4. Click **"Update"** to save changes
5. Confirmation message displays

#### **4. Delete Student**

1. **Select** student row
2. Click **"Delete"** button
3. **Confirm deletion** in dialog box
4. Record removed from database
5. Table refreshes automatically

#### **5. Search Students**

1. Enter search term in search box
2. Press **Enter** or click **"Search"**
3. Table filters to matching records
4. Clear search box to show all students

---

## 📁 Project Structure

```
student-management-mysql/
├── main.py                          # Main application entry point
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── .gitignore                       # Git exclusion patterns
├── README.md                        # This file
│
├── icons/                           # Application icons (optional)
│   ├── add.png                      # Add button icon
│   └── search.png                   # Search button icon
│
└── instance/                        # Runtime data (gitignored)
    └── (empty - no sensitive data)
```

---

## 🗄️ Database Schema

### **Students Table**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | INT | PRIMARY KEY, AUTO_INCREMENT | Unique student identifier |
| `student_id` | VARCHAR(50) | UNIQUE, NOT NULL | Student ID number |
| `first_name` | VARCHAR(100) | NOT NULL | Student first name |
| `last_name` | VARCHAR(100) | NOT NULL | Student last name |
| `email` | VARCHAR(150) | UNIQUE | Student email address |
| `phone` | VARCHAR(50) | | Contact phone number |
| `grade` | VARCHAR(10) | | Current grade level |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation time |
| `updated_at` | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Last modification time |

### **SQL Creation Script:**

```sql
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    phone VARCHAR(50),
    grade VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

---

## 🏗️ Architecture

### **Application Flow:**

```
PyQt5 GUI (main.py)
    ↓
Event Handlers (button clicks, table selection)
    ↓
Database Connection (mysql.connector)
    ↓
MySQL Database (school.students)
    ↓
Result Display (table widget refresh)
```

### **Component Breakdown:**

```python
# Main Application Components:

1. MainWindow (QMainWindow)
   - Application window and layout
   - Menu bar and toolbar
   - Status bar for messages

2. Database Manager
   - Connection pooling
   - Query execution
   - Error handling

3. Student Table Widget
   - Display records
   - Handle selections
   - Sorting and filtering

4. Dialog Windows
   - Add student form
   - Edit student form
   - Delete confirmation
```

---

## 🔧 Configuration

### **Environment Variables (.env)**

```bash
# MySQL Database Configuration
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_secure_password_here
DB_NAME=school

# Optional: Connection Settings
DB_PORT=3306
DB_CHARSET=utf8mb4
```

### **Environment Variable Validation:**

The application validates required environment variables on startup:

```python
# Startup validation
required_vars = ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME']

for var in required_vars:
    if not os.getenv(var):
        raise ValueError(f"Missing required environment variable: {var}")
```

---

## 🎓 Learning Objectives Demonstrated

This project showcases proficiency in:

✅ **Desktop GUI Development:**
- PyQt5 widget composition and layouts
- Event-driven programming with signals/slots
- Table widget data binding
- Dialog window management
- Toolbar and menu creation

✅ **Database Management:**
- MySQL connection handling with connection pooling
- CRUD operations (Create, Read, Update, Delete)
- Parameterized queries for SQL injection prevention
- Transaction management and rollback
- Error handling and recovery

✅ **Security Best Practices:**
- Environment variable configuration
- Credential protection (no hardcoded passwords)
- `.gitignore` for sensitive files
- Input validation and sanitization
- Secure database connections

✅ **Software Engineering:**
- Code organization and modularity
- Error handling and user feedback
- Cross-platform compatibility
- Documentation and code comments
- Virtual environment management

---

## 🔒 Security Notes

**⚠️ Important Security Considerations:**

This application implements several security best practices:

- **Environment Variables:** All database credentials stored in `.env` file
- **Git Protection:** `.gitignore` prevents credential commits
- **Parameterized Queries:** SQL injection prevention throughout
- **Input Validation:** User input sanitized before database operations
- **Connection Security:** MySQL connections use secure parameters

**Security Audit Status:**
- ✅ Zero critical vulnerabilities
- ✅ No hardcoded passwords
- ✅ Proper `.gitignore` configuration
- ✅ Environment variable validation
- ✅ SQL injection prevention

**For Production Deployment:**
- Use strong database passwords (16+ characters)
- Enable MySQL SSL/TLS connections
- Implement user authentication
- Add audit logging for database changes
- Regular security updates for dependencies

---

## 🧪 Testing

### **Manual Testing Checklist:**

**Basic Operations:**
- [ ] Application launches successfully
- [ ] Database connection established
- [ ] Table displays on startup
- [ ] Add new student record
- [ ] View all students in table
- [ ] Update existing student
- [ ] Delete student with confirmation
- [ ] Search functionality works

**Error Handling:**
- [ ] Invalid database credentials show error
- [ ] Empty required fields show validation message
- [ ] Duplicate student ID prevented
- [ ] Database connection loss handled gracefully
- [ ] Invalid email format rejected

**Data Persistence:**
- [ ] Records persist after application restart
- [ ] Updates saved correctly to database
- [ ] Deletions remove from database
- [ ] No data corruption on crash

### **Test Credentials (for demonstration):**

```bash
# Test database setup
DB_HOST=localhost
DB_USER=test_user
DB_PASSWORD=test_password
DB_NAME=school_test
```

---

## 🚧 Future Enhancements

### **Potential Improvements:**

**User Features:**
- [ ] Student photo upload and display
- [ ] Grade tracking and GPA calculation
- [ ] Attendance management system
- [ ] Export data to CSV/Excel/PDF
- [ ] Print student reports
- [ ] Email notifications for events
- [ ] Parent/guardian contact management

**Technical Improvements:**
- [ ] User authentication (admin/teacher roles)
- [ ] Audit log for all database changes
- [ ] Data backup and restore functionality
- [ ] Dark mode theme support
- [ ] Multi-language support (i18n)
- [ ] Advanced search with filters
- [ ] Bulk import from CSV
- [ ] Dashboard with statistics and charts

**Advanced Features:**
- [ ] Class assignment and scheduling
- [ ] Course enrollment tracking
- [ ] Fee management system
- [ ] Library book tracking
- [ ] Disciplinary records
- [ ] Cloud database migration (AWS RDS/Azure)
- [ ] Real-time collaboration (multiple users)
- [ ] Mobile app companion (React Native)

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

- Built with PyQt5 desktop GUI framework
- MySQL database integration for reliable data persistence
- Demonstrates desktop application development skills
- Security audit completed with zero critical vulnerabilities
- Part of software development learning journey

---

## 📝 Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
cd Python-Portfolio-Projects/early-projects/student-management-mysql
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Configure database
cp .env.example .env
nano .env  # Add your MySQL credentials

# Create database
mysql -u root -p -e "CREATE DATABASE school;"

# Run application
python main.py
```

---

**Note:** This is an educational project demonstrating desktop GUI development with database integration. Database credentials must be configured via `.env` file before running. Suitable for portfolio showcase and learning purposes.
