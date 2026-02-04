# Food Ordering App - Django Restaurant Menu System

**Developer:** StackDevOps8999  
**Technologies:** Django 5.2.5, Python 3.13, SQLite, QR Code Generation  
**Status:** Complete ✅

---

## 📋 Overview

A full-featured Django web application for restaurant menu management with QR code integration. Restaurant owners can create, manage, and display their menu items online, while customers can browse the menu through a mobile-friendly interface or scan a QR code for quick access.

This project demonstrates:
- Full CRUD operations for menu items
- Category-based menu organization
- SEO-friendly slug-based URLs
- QR code generation for contactless menu access
- Django admin interface for menu management
- Responsive HTML templates
- Database migrations and data modeling

---

## ✨ Key Features

### **Restaurant Owner Features**
- **Menu Management:** Create, update, and delete menu items through Django admin
- **Category Organization:** Organize items into Starters, Salads, Main Dishes, and Desserts
- **Item Status Control:** Mark items as Available or Unavailable
- **SEO-Friendly URLs:** Automatic slug generation for each menu item
- **QR Code Generation:** Generate QR codes for contactless menu access
- **Author Tracking:** Track which staff member created each menu item

### **Customer Features**
- **Browse Menu:** View all available menu items organized by category
- **Detailed View:** Click any item to see full description and pricing
- **Mobile-Friendly:** Responsive design works on all devices
- **QR Code Access:** Scan QR code to instantly access menu

### **Technical Features**
- **Database Persistence:** SQLite database with proper relationships
- **Data Validation:** Price validation, unique meal names, category constraints
- **Timestamps:** Automatic creation and update timestamps
- **Migration System:** Database schema versioning with Django migrations
- **Template Inheritance:** DRY templating with base.html

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 5.2.5 | Web framework and ORM |
| **Python** | 3.13 | Core programming language |
| **SQLite** | Default | Database for menu items |
| **Pillow** | 11.3.0 | Image processing for QR codes |
| **qrcode** | 8.2 | QR code generation |
| **django-qrcode** | 0.3 | Django QR code integration |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
   cd Python-Portfolio-Projects/early-projects/food-ordering-app-django
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
   # Edit .env with your settings
   ```

5. **Generate a new Django SECRET_KEY:**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   # Copy the output and paste into .env file
   ```

6. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Create admin superuser:**
   ```bash
   python manage.py createsuperuser
   # Follow prompts to set username, email, and password
   ```

8. **Run development server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the application:**
   - **Main Menu:** http://127.0.0.1:8000/
   - **Admin Panel:** http://127.0.0.1:8000/admin/

---

## 🚀 Usage

### **For Restaurant Owners:**

#### **1. Add Menu Items via Admin Panel**

1. Navigate to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Click "Items" under RESTAURANT_MENU
4. Click "Add Item" button
5. Fill in:
   - **Meal:** Item name (e.g., "Grilled Salmon")
   - **Description:** Brief description
   - **Price:** Decimal price (e.g., 24.99)
   - **Category:** Choose from dropdown
   - **Status:** Available or Unavailable
   - **Author:** Select staff member
6. Slug auto-generates from meal name
7. Click "Save"

#### **2. Generate QR Code**

```bash
# Run QR code generator
python qr.py

# Output: qr.png created in project root
# Print and display this QR code in your restaurant
```

**Update QR URL for production:**
Edit `qr.py` line 4:
```python
url = "https://your-restaurant-domain.com"  # Change from localhost
```

### **For Customers:**

#### **Browse Menu Online**
1. Visit http://127.0.0.1:8000/
2. See all available menu items
3. Click any item for detailed view

#### **Scan QR Code**
1. Use phone camera to scan QR code
2. Automatically opens menu in browser
3. Browse and view items on mobile device

---

## 📁 Project Structure

```
food-ordering-app-django/
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── .env.example                     # Environment variables template
├── qr.py                           # QR code generator script
├── qr.png                          # Generated QR code image
│
├── mysite/                         # Django project settings
│   ├── __init__.py
│   ├── settings.py                 # Project configuration
│   ├── urls.py                     # Main URL routing
│   ├── asgi.py                     # ASGI configuration
│   └── wsgi.py                     # WSGI configuration
│
├── restaurant_menu/                # Menu management app
│   ├── __init__.py
│   ├── admin.py                    # Admin interface config
│   ├── apps.py                     # App configuration
│   ├── models.py                   # Database models (Item)
│   ├── views.py                    # View logic
│   ├── urls.py                     # App URL routing
│   ├── tests.py                    # Unit tests
│   │
│   ├── migrations/                 # Database migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py         # Initial Item model
│   │   ├── 0002_item_slug.py       # Add slug field
│   │   └── 0004_populate_slugs.py  # Auto-populate slugs
│   │
│   └── templates/
│       └── restaurant_menu/
│           ├── base.html           # Base template
│           ├── menu_list.html      # Menu listing page
│           └── menu_item_details.html  # Item detail page
│
└── templates/                      # Project-wide templates
```

---

## 🗄️ Database Schema

### **Item Model**

| Field | Type | Description |
|-------|------|-------------|
| `id` | BigAutoField | Primary key (auto-generated) |
| `meal` | CharField(500) | Menu item name (unique) |
| `description` | CharField(500) | Item description |
| `price` | DecimalField(20,2) | Item price |
| `category` | CharField | Starters, Salads, Main Dishes, or Desserts |
| `status` | IntegerField | 0=Unavailable, 1=Available |
| `slug` | SlugField | SEO-friendly URL (auto-generated) |
| `author` | ForeignKey(User) | Staff member who created item |
| `date_created` | DateTimeField | Auto-set on creation |
| `date_updated` | DateTimeField | Auto-updated on save |

### **Relationships**
- **Item → User:** Many-to-One (author field)
- **Item.category:** Choice field with predefined options

---

## 🎨 Templates

### **base.html**
Base template with common HTML structure, navigation, and styling.

### **menu_list.html**
Displays all available menu items organized by category.

### **menu_item_details.html**
Shows detailed information for a single menu item including full description and pricing.

---

## 🔧 Configuration

### **Environment Variables (.env)**

```bash
# Django Configuration
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite is default, configure if using PostgreSQL)
# DATABASE_URL=postgresql://user:password@localhost/dbname
```

### **Settings Highlights (mysite/settings.py)**

- **Database:** SQLite (default) - suitable for small restaurants
- **Static Files:** Configured for development
- **Templates:** Django template engine with app_directories loader
- **Apps:** restaurant_menu app installed
- **Middleware:** Standard Django security middleware

---

## 🚧 Deployment to Production

### **Pre-Deployment Checklist:**

1. **Update QR Code URL:**
   ```python
   # In qr.py, change:
   url = "https://your-actual-domain.com"
   ```

2. **Generate new QR code:**
   ```bash
   python qr.py
   ```

3. **Update settings.py:**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
   ```

4. **Set up production database:**
   - Consider PostgreSQL for production
   - Update DATABASE setting in settings.py

5. **Collect static files:**
   ```bash
   python manage.py collectstatic
   ```

6. **Use production-grade server:**
   - Gunicorn or uWSGI
   - Nginx reverse proxy
   - SSL certificate (Let's Encrypt)

---

## 🎓 Learning Objectives Demonstrated

This project showcases proficiency in:

✅ **Django Framework:**
- Models, Views, Templates (MVT) architecture
- Django ORM and database migrations
- Admin interface customization
- URL routing and slug-based URLs

✅ **Database Design:**
- Relational database modeling
- Foreign key relationships
- Data validation and constraints
- Migration management

✅ **Web Development:**
- HTML templating and template inheritance
- Responsive design principles
- CRUD operations
- User authentication integration

✅ **Python Best Practices:**
- Virtual environment management
- Requirements management
- Environment variable configuration
- Code organization and modularity

---

## 🔒 Security Notes

**⚠️ Important Security Considerations:**

- **SECRET_KEY:** Never commit to Git, use environment variables
- **DEBUG Mode:** Set to `False` in production
- **ALLOWED_HOSTS:** Configure properly for production
- **Database Credentials:** Use environment variables
- **HTTPS:** Always use SSL/TLS in production
- **User Authentication:** Admin panel requires login

**Current Security Status:**
- ✅ SECRET_KEY uses environment variable
- ✅ .env.example provided (no real secrets)
- ✅ .gitignore configured properly
- ⚠️ DEBUG=True (development only)

---

## 🧪 Testing

### **Manual Testing Checklist:**

**Menu Management:**
- [ ] Create new menu item via admin
- [ ] Update existing menu item
- [ ] Delete menu item
- [ ] Mark item as unavailable
- [ ] Verify slug auto-generation

**Public Menu:**
- [ ] View menu list page
- [ ] Click item to see details
- [ ] Verify only available items show
- [ ] Test category filtering

**QR Code:**
- [ ] Generate QR code with qr.py
- [ ] Scan QR code with phone
- [ ] Verify URL opens correctly

### **Run Django Tests:**

```bash
python manage.py test restaurant_menu
```

---

## 🚀 Future Enhancements

### **Potential Improvements:**

- [ ] Shopping cart functionality
- [ ] Online ordering system
- [ ] Payment gateway integration (Stripe/PayPal)
- [ ] Email order confirmations
- [ ] Customer accounts and order history
- [ ] Table reservation system
- [ ] Multi-language support (i18n)
- [ ] Image uploads for menu items
- [ ] Nutrition information display
- [ ] Allergen warnings
- [ ] Daily specials feature
- [ ] Customer reviews and ratings

### **Advanced Features:**

- [ ] Real-time order tracking
- [ ] Kitchen display system integration
- [ ] Inventory management
- [ ] Analytics dashboard for owners
- [ ] Mobile app (React Native)
- [ ] Social media integration
- [ ] Loyalty program
- [ ] Gift card system

---

## 📱 QR Code Usage

### **For Restaurant Owners:**

1. **Generate QR Code:**
   ```bash
   python qr.py
   ```

2. **Print QR Code:**
   - Print `qr.png` on table tents
   - Display at entrance
   - Include on business cards
   - Add to social media

3. **Update for Production:**
   - Change URL in `qr.py` to your domain
   - Regenerate QR code
   - Test scan functionality

### **QR Code Configuration:**

```python
# In qr.py:
qr = qrcode.QRCode(
    version=1,              # Size (1-40)
    error_correction=L,     # Error correction level
    box_size=10,            # Pixel size
    border=4,               # Border thickness
)
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

- Built with Django 5.2.5 web framework
- QR code generation powered by python-qrcode
- Demonstrates full-stack web development skills
- Part of software development learning journey

---

## 📝 Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
cd Python-Portfolio-Projects/early-projects/food-ordering-app-django
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Setup database
python manage.py migrate
python manage.py createsuperuser

# Run server
python manage.py runserver

# Generate QR code
python qr.py

# Access
# Menu: http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
```

---

**Note:** This is an educational project demonstrating Django web development with menu management and QR code integration. Suitable for portfolio showcase and learning purposes.
