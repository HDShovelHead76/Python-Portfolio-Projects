import sys
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from PyQt5.QtWidgets import (
    QApplication, QLineEdit, QPushButton, QMainWindow, QAction, QMessageBox,
    QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox, QMenu,
    QToolBar, QStatusBar
)
from PyQt5.QtCore import Qt

# -----------------------------
# Database Configuration
# -----------------------------
# Load environment variables
load_dotenv()

HOST = os.getenv("DB_HOST", "localhost")
USER = os.getenv("DB_USER", "root")
PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "school")

# Validate required environment variables
if not PASSWORD:
    raise ValueError(
        "❌ DB_PASSWORD not found in environment variables!\n"
        "Create a .env file with: DB_PASSWORD=your_password"
    )

class DatabaseManager:
    """Handles all database operations for the Student Management System."""
    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.ensure_database()

    def connect(self, with_db=True):
        """Create a connection to MySQL."""
        try:
            if with_db:
                return mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.db_name
                )
            else:
                return mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password
                )
        except Error as e:
            QMessageBox.critical(None, "Database Error", f"MySQL connection failed:\n{e}")
            sys.exit(1)

    def ensure_database(self):
        """Create database and table if they do not exist."""
        try:
            conn = self.connect(with_db=False)
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
            conn.close()

            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    course VARCHAR(255) NOT NULL,
                    mobile VARCHAR(20) NOT NULL
                )
            """)
            conn.commit()
            conn.close()
        except Error as e:
            QMessageBox.critical(None, "Database Error", f"Error creating database/table:\n{e}")
            sys.exit(1)

    def fetch_students(self, search_term=None):
        """Retrieve students from database. Can search by name, course, or mobile."""
        conn = self.connect()
        cursor = conn.cursor()
        if search_term:
            query = """
                SELECT * FROM students 
                WHERE name LIKE %s OR course LIKE %s OR mobile LIKE %s
            """
            like_term = f"%{search_term}%"
            cursor.execute(query, (like_term, like_term, like_term))
        else:
            cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        conn.close()
        return result

    def insert_student(self, name, course, mobile):
        """Insert a new student into the database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)",
            (name, course, mobile)
        )
        conn.commit()
        conn.close()

    def update_student(self, student_id, name, course, mobile):
        """Update student details by ID."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s",
            (name, course, mobile, student_id)
        )
        conn.commit()
        conn.close()

    def delete_student(self, student_id):
        """Delete student by ID."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()
        conn.close()

# -----------------------------
# Main Application Window (unchanged except DB manager usage)
# -----------------------------
class MainWindow(QMainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.db = db_manager
        self.setWindowTitle("Student Management System")
        self.resize(700, 400)

        # Menu bar
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu.addAction(add_student_action)

        edit_student_action = QAction("Edit Student", self)
        edit_student_action.triggered.connect(self.edit_student)
        file_menu.addAction(edit_student_action)

        delete_student_action = QAction("Delete Student", self)
        delete_student_action.triggered.connect(self.delete_student)
        file_menu.addAction(delete_student_action)

        search_student_action = QAction("Search Student", self)
        search_student_action.triggered.connect(self.search_student)
        file_menu.addAction(search_student_action)

        about_action = QAction("About Student System", self)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        help_menu.addAction(about_action)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.show_context_menu)
        self.setCentralWidget(self.table)

        # Toolbar
        toolbar = QToolBar()
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_student_action)
        self.addToolBar(toolbar)

        # Status Bar
        self.setStatusBar(QStatusBar())

    def load_data(self, search_term=None):
        result = self.db.fetch_students(search_term)
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def insert(self):
        dlg = InsertDialog(self.db)
        if dlg.exec_():
            self.load_data()

    def edit_student(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Selection Error", "Please select a student to edit.")
            return
        student_id = self.table.item(selected_row, 0).text()
        dlg = EditDialog(self.db, student_id)
        if dlg.exec_():
            self.load_data()

    def delete_student(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Selection Error", "Please select a student to delete.")
            return
        student_id = self.table.item(selected_row, 0).text()
        confirm = QMessageBox.question(self, "Confirm Delete", f"Delete student ID {student_id}?")
        if confirm == QMessageBox.Yes:
            self.db.delete_student(student_id)
            QMessageBox.information(self, "Deleted", "Student deleted successfully.")
            self.load_data()

    def search_student(self):
        dlg = SearchDialog()
        if dlg.exec_():
            self.load_data(dlg.search_term)

    def show_context_menu(self, position):
        menu = QMenu()
        index = self.table.indexAt(position)
        if index.isValid():
            edit_action = QAction("Edit", self)
            edit_action.triggered.connect(self.edit_student)
            menu.addAction(edit_action)

            delete_action = QAction("Delete", self)
            delete_action.triggered.connect(self.delete_student)
            menu.addAction(delete_action)

        search_action = QAction("Search", self)
        search_action.triggered.connect(self.search_student)
        menu.addAction(search_action)
        menu.exec_(self.table.viewport().mapToGlobal(position))

# -----------------------------
# Dialogs (unchanged)
# -----------------------------
class InsertDialog(QDialog):
    def __init__(self, db_manager):
        super().__init__()
        self.db = db_manager
        self.setWindowTitle("Insert New Student")
        self.setFixedSize(320, 250)
        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        self.course_name.addItem("Select a Course")
        self.course_name.addItems(["Biology", "Math", "Astronomy", "Physics"])
        layout.addWidget(self.course_name)

        self.mobile_name = QLineEdit()
        self.mobile_name.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile_name)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.add_student)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text().strip()
        course = self.course_name.currentText()
        mobile = self.mobile_name.text().strip()

        if not name or course == "Select a Course" or not mobile:
            QMessageBox.warning(self, "Input Error", "Please fill all fields correctly.")
            return

        self.db.insert_student(name, course, mobile)
        QMessageBox.information(self, "Success", "Student added successfully!")
        self.accept()

class EditDialog(QDialog):
    def __init__(self, db_manager, student_id):
        super().__init__()
        self.db = db_manager
        self.student_id = student_id
        self.setWindowTitle("Edit Student Info")
        self.setFixedSize(320, 250)
        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        self.course_name.addItem("Select a Course")
        self.course_name.addItems(["Biology", "Math", "Astronomy", "Physics"])
        layout.addWidget(self.course_name)

        self.mobile_name = QLineEdit()
        layout.addWidget(self.mobile_name)

        submit_button = QPushButton("Update")
        submit_button.clicked.connect(self.update_student)
        layout.addWidget(submit_button)

        self.setLayout(layout)
        self.load_student()

    def load_student(self):
        students = self.db.fetch_students()
        for s in students:
            if str(s[0]) == str(self.student_id):
                self.student_name.setText(s[1])
                index = self.course_name.findText(s[2])
                if index >= 0:
                    self.course_name.setCurrentIndex(index)
                self.mobile_name.setText(s[3])

    def update_student(self):
        name = self.student_name.text().strip()
        course = self.course_name.currentText()
        mobile = self.mobile_name.text().strip()

        if not name or course == "Select a Course" or not mobile:
            QMessageBox.warning(self, "Input Error", "Please fill all fields correctly.")
            return

        self.db.update_student(self.student_id, name, course, mobile)
        QMessageBox.information(self, "Success", "Student updated successfully!")
        self.accept()

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedSize(320, 150)
        self.search_term = ""
        layout = QVBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter name, course, or mobile")
        layout.addWidget(self.search_input)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.do_search)
        layout.addWidget(search_button)

        self.setLayout(layout)

    def do_search(self):
        self.search_term = self.search_input.text().strip()
        self.accept()

# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    db_manager = DatabaseManager(HOST, USER, PASSWORD, DB_NAME)
    app = QApplication(sys.argv)
    window = MainWindow(db_manager)
    window.show()
    window.load_data()
    sys.exit(app.exec_())
