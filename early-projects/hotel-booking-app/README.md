# Hotel Booking System

**Developer:** StackDevOps8999  
**Technologies:** Python 3.13, Pandas, Object-Oriented Programming  
**Status:** Complete ✅

---

## 📋 Overview

A command-line hotel booking simulation system demonstrating **Object-Oriented Programming (OOP)** principles including **inheritance**, **encapsulation**, **properties**, and **class methods**. The system simulates hotel reservations with credit card validation and optional spa package bookings.

This project showcases practical implementation of:
- Class hierarchies (Hotel → SpaHotel)
- Credit card validation with two-factor authentication
- CSV data persistence with Pandas
- Property decorators for dynamic data access
- Secure payment processing simulation

---

## ✨ Key Features

### **Hotel Management**
- Browse available hotels from CSV database
- Real-time availability checking
- Automatic booking status updates
- Hotel data persistence across sessions

### **Reservation System**
- Customer name validation and formatting
- Booking confirmation ticket generation
- Optional spa package add-on
- Separate ticket generation for spa services

### **Credit Card Processing**
- Card validation (number, expiration, CVC, holder name)
- Two-factor authentication with password verification
- Secure card database lookup
- Support for basic and secure card types

### **OOP Architecture**
- **Inheritance:** `Hotel` → `SpaHotel`, `CreditCard` → `SecureCreditCard`, `Reservation` → `SpaTicket`
- **Encapsulation:** Data protection through properties
- **Properties:** Dynamic access to hotel name and availability
- **Class Methods:** Centralized data management via `DataStore`

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.13** | Core programming language |
| **Pandas** | CSV data manipulation and persistence |
| **Pathlib** | Cross-platform file path handling |
| **OOP Principles** | Class design and inheritance |
| **Type Hints** | Code documentation and IDE support |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
   cd Python-Portfolio-Projects/early-projects/hotel-booking-app
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

4. **Verify data files exist:**
   ```bash
   ls Hotels/hotels.csv
   ls CreditCards/cards.csv
   ls CreditCards/card_security.csv
   ```

---

## 🚀 Usage

### **Run the Application:**

```bash
python main.py
```

### **Sample Interaction:**

```
     id              name         city  capacity available
0   134  Tourist Sunny Apartment  Anchorage       4        no
1   188  Snow Palace             New Delhi       5        no
2   655  City Break Inn          Porto-Novo      3        no

Enter the ID of the Hotel: 134
Enter your name: John Doe

Thank you for your reservation!
Name: John Doe
Hotel: Tourist Sunny Apartment

Would you like to purchase a Spa Package? (yes/no): yes
Spa package booked for Tourist Sunny Apartment!

Thank you, enjoy your Spa Day!
Name: John Doe
Hotel: Tourist Sunny Apartment
```

### **Test Credentials (for demonstration):**

```python
Card Number: 1234123412341234
Expiration: 12/26
CVC: 123
Holder Name: JOHN SMITH
Password: mypass
```

---

## 📁 Project Structure

```
hotel-booking-app/
├── main.py                          # Main application logic
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
├── Hotels/
│   └── hotels.csv                   # Hotel inventory database
│
├── CreditCards/
│   ├── cards.csv                    # Valid credit cards
│   └── card_security.csv            # Card authentication passwords
│
├── Planning/
│   ├── planning.txt                 # Project planning notes
│   ├── Code_Breakdown.md            # Simplified code explanation
│   └── hotel_booking_system.pdf     # Class diagram
│
└── D39Student/
    └── (Course materials)
```

---

## 🏗️ Architecture

### **Class Hierarchy:**

```
DataStore (Class Variables & Methods)
    └── Manages all CSV data access and persistence

Hotel (Base Class)
    ├── Properties: name, available
    ├── Methods: book()
    └── SpaHotel (Inherits Hotel)
        └── Additional: book_spa_package()

Reservation (Base Class)
    ├── Generates booking confirmation
    └── SpaTicket (Inherits Reservation)
        └── Generates spa confirmation

CreditCard (Base Class)
    ├── Validates card details
    └── SecureCreditCard (Inherits CreditCard)
        └── Adds password authentication
```

### **Data Flow:**

```
1. User selects hotel → System checks availability
2. User provides card details → Basic validation
3. User enters password → Secure authentication
4. System books hotel → Updates CSV
5. System generates tickets → Displays confirmations
```

---

## 🎓 Learning Objectives Demonstrated

This project demonstrates proficiency in:

✅ **Object-Oriented Design:**
- Class inheritance and polymorphism
- Property decorators for computed attributes
- Class methods for shared behavior

✅ **Data Management:**
- CSV file reading/writing with Pandas
- Data persistence across sessions
- Type-safe data handling

✅ **Design Patterns:**
- Centralized data store pattern
- Factory-like object creation
- Separation of concerns

✅ **Python Best Practices:**
- Type hints for code clarity
- Docstrings for documentation
- DRY (Don't Repeat Yourself) principle
- Magic methods (`__str__`, `__repr__`)

---

## 🔒 Security Notes

**⚠️ Important:** This is an **educational demonstration** project. In production systems:

- **Never store passwords in plain text** (use hashing: bcrypt, Argon2)
- **Never store full credit card numbers** (use tokenization/PCI compliance)
- **Never commit sensitive data to Git** (use `.env` files)
- **Use proper encryption** for sensitive data at rest
- **Implement HTTPS** for data in transit

This project uses simplified authentication for learning purposes only.

---

## 📊 Sample Data

### **hotels.csv:**
```csv
id,name,city,capacity,available
134,Tourist Sunny Apartment,Anchorage,4,yes
188,Snow Palace,New Delhi,5,yes
655,City Break Inn,Porto-Novo,3,yes
```

### **cards.csv:**
```csv
number,expiration,cvc,holder
1234123412341234,12/26,123,JOHN SMITH
5678,12/28,456,JANE SMITH
```

### **card_security.csv:**
```csv
number,password
1234123412341234,mypass
```

---

## 🚧 Future Enhancements

### **Potential Improvements:**
- [ ] Add user registration and login system
- [ ] Implement booking history tracking
- [ ] Add multiple room booking support
- [ ] Create web interface with Flask/Django
- [ ] Add date-based booking calendar
- [ ] Implement email confirmation system
- [ ] Add payment gateway integration (Stripe API)
- [ ] Create database backend (SQLite/PostgreSQL)
- [ ] Add unit tests with pytest
- [ ] Implement logging for transactions

### **Advanced Features:**
- [ ] Multi-currency support
- [ ] Dynamic pricing based on demand
- [ ] Customer loyalty program
- [ ] Review and rating system
- [ ] Admin dashboard for hotel management

---

## 🧪 Testing

### **Manual Testing Checklist:**

✅ Test available hotel booking  
✅ Test unavailable hotel rejection  
✅ Test valid credit card acceptance  
✅ Test invalid credit card rejection  
✅ Test password authentication  
✅ Test spa package booking  
✅ Verify CSV updates after booking  

### **Run Tests:**

```bash
# Test with valid credentials
python main.py
# Enter hotel ID: 134
# Enter name: Test User
# Card validates successfully

# Test with invalid hotel ID
python main.py
# Enter hotel ID: 999
# Should show "Hotel is not available"
```

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

- Project planning documents and class diagrams included in `/Planning` folder
- Demonstrates concepts from Python OOP curriculum
- Built as part of software development learning journey

---

**Note:** This is an educational project demonstrating Object-Oriented Programming principles. It simulates a hotel booking system with credit card validation for learning purposes.
