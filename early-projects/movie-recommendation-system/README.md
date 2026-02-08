# 🎬 Django Movie Recommendation System

A full-stack web application featuring three machine learning recommendation algorithms: popularity-based ranking, content-based filtering using TF-IDF similarity, and collaborative filtering using matrix factorization. Built with Django 5.2.5, pandas, and scikit-learn to demonstrate both web development and data science capabilities.

## 🎯 Project Overview

This application provides personalized movie recommendations through an intuitive web interface. Users can discover movies using three different recommendation strategies, each leveraging different aspects of the movie dataset (ratings, content metadata, and user behavior patterns). The system processes real movie data to generate intelligent suggestions tailored to different use cases.

**Use Case:** Movie discovery platform, recommendation engine learning tool, or portfolio demonstration of full-stack ML integration. Shows how to bridge machine learning algorithms with production web applications.

## ✨ Key Features

### Three Recommendation Algorithms

**1. Popularity-Based Recommendations**
- Ranks movies by total rating count across all users
- Fast, simple aggregation queries
- Ideal for "trending" or "most watched" suggestions
- No personalization, universal rankings

**2. Content-Based Filtering**
- Uses TF-IDF (Term Frequency-Inverse Document Frequency) on movie overviews
- Computes cosine similarity between movie descriptions
- Recommends movies similar to one the user already likes
- Example: Input "The Dark Knight" → Get other Batman/superhero films

**3. Collaborative Filtering**
- Matrix factorization using Singular Value Decomposition (SVD)
- Predicts user ratings based on behavior patterns of similar users
- Personalized recommendations per user ID
- Example: User 1's predicted top-rated movies

### Web Application Features

- **Dynamic Homepage** - Displays top 5 popular movies on load
- **Interactive Forms** - Select recommendation type and input parameters
- **Results Display** - Formatted tables with movie titles and relevant metrics
- **Clean UI** - Simple, functional interface with Bootstrap-ready templates
- **Real-Time Processing** - Algorithms run on-demand per request

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.13 |
| **Django** | Web framework for MVC architecture | 5.2.5 |
| **pandas** | Data processing and CSV handling | 2.3.2 |
| **scikit-learn** | Machine learning algorithms (TF-IDF, SVD) | 1.7.1 |
| **NumPy** | Numerical computing for matrix operations | 2.3.2 |
| **SciPy** | Scientific computing for collaborative filtering | 1.16.1 |
| **python-dotenv** | Environment variable management | 1.0.1 |
| **SQLite** | Database (Django default) | Built-in |

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Virtual environment tool (recommended)

### Setup Instructions

1. **Clone or download this repository**
```bash
   cd movie-recommendation-system
```

2. **Create a virtual environment**
```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Configure Django secret key**
   
   Create a `.env` file in the project root:
```bash
   cp .env.example .env
```
   
   Generate a secret key and add to `.env`:
```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
   
   Edit `.env`:
```
   SECRET_KEY=your_generated_secret_key_here
```

5. **Apply database migrations**
```bash
   python manage.py migrate
```

6. **Run the development server**
```bash
   python manage.py runserver
```

7. **Access the application**
   
   Open your browser to: `http://127.0.0.1:8000/`

## 🚀 Usage

### Homepage Features

When you load the homepage, you'll see:

1. **Top 5 Popular Movies** - Automatically displays most-rated films
2. **Random Movie Suggestion** - A random title for content-based testing
3. **Recommendation Form** - Select algorithm type and input parameters

### Getting Recommendations

**Popularity-Based:**
1. Select "Popularity Based" from dropdown
2. Click "Get Recommendations"
3. View top 10 most-rated movies

**Content-Based:**
1. Select "Content Based" from dropdown
2. Enter a movie title (e.g., "The Dark Knight", "Inception", "Forrest Gump")
3. Click "Get Recommendations"
4. View 5 similar movies based on plot descriptions

**Collaborative Filtering:**
1. Select "Collaborative Filtering" from dropdown
2. Enter a User ID (integer, default: 1)
3. Click "Get Recommendations"
4. View 5 predicted top-rated movies for that user

### Example Queries

**Content-Based Examples:**
- "The Matrix" → Sci-fi action films
- "The Godfather" → Crime dramas
- "Toy Story" → Animated family films
- "Pulp Fiction" → Tarantino-style films

**Collaborative User Examples:**
- User 1 → Predicted preferences based on their rating history
- User 50 → Different user with different taste profile

## 🏗️ Project Architecture

### Directory Structure
```
Recommendation_Sys_Setup/
├── mysite/                       # Django project settings
│   ├── settings.py              # Configuration (SECRET_KEY from .env)
│   ├── urls.py                  # Root URL routing
│   └── wsgi.py                  # WSGI entry point
├── movie_recommender/            # Django app
│   ├── views.py                 # Request handlers
│   ├── urls.py                  # App URL patterns
│   ├── templates/               # HTML templates
│   │   └── movie_recommender/
│   │       ├── base.html        # Base template
│   │       ├── index.html       # Homepage
│   │       └── results.html     # Results display
│   └── ...
├── movie_recommendations/        # ML algorithms module
│   ├── popularity.py            # Popularity algorithm
│   ├── content.py               # Content-based filtering
│   ├── collaborative.py         # Collaborative filtering
│   └── utils.py                 # Shared utilities
├── data/                         # Movie datasets
│   ├── movies.csv               # Movie metadata (titles, overviews)
│   ├── ratings.csv              # User rating data
│   └── credits.csv              # Cast/crew information
├── notebooks/                    # Jupyter notebooks (development)
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (NOT in Git)
├── .env.example                  # Environment template
└── README.md                     # This file
```

### Data Flow
```
User Request → Django Views (views.py)
    ↓
Algorithm Selection (popularity/content/collaborative)
    ↓
movie_recommendations/ Module
    ↓
Load CSV Data (pandas)
    ↓
Apply ML Algorithm
    ↓
Return DataFrame Results
    ↓
Template Rendering (HTML tables)
    ↓
HTTP Response to Browser
```

### Algorithm Details

**1. Popularity Algorithm (`popularity.py`)**
```python
def popularity_recommendations(top_n=10):
    # Group ratings by movie ID
    # Count total ratings per movie
    # Sort by rating count descending
    # Merge with movie titles
    # Return top N
```
- **Time Complexity:** O(n log n) for sorting
- **Use Case:** Homepage trending section, new user recommendations

**2. Content-Based Algorithm (`content.py`)**
```python
def content_based(movie_title, top_n=5):
    # Load movie overviews
    # Compute TF-IDF vectors
    # Calculate cosine similarity matrix
    # Find movies similar to input
    # Return top N matches
```
- **Technique:** TF-IDF + Cosine Similarity
- **Time Complexity:** O(m²) for similarity matrix (m = number of movies)
- **Use Case:** "More like this" recommendations

**3. Collaborative Filtering (`collaborative.py`)**
```python
def collaborative_filtering(user_id, top_n=5):
    # Create user-movie rating matrix
    # Apply SVD matrix factorization
    # Predict ratings for unwatched movies
    # Return top N predictions
```
- **Technique:** Singular Value Decomposition (SVD)
- **Time Complexity:** O(nmk) where k = latent factors
- **Use Case:** Personalized user recommendations

## 🎓 Learning Objectives

This project demonstrates proficiency in:

### Machine Learning
- **Recommendation Systems** - Three different algorithmic approaches
- **Natural Language Processing** - TF-IDF for text feature extraction
- **Matrix Factorization** - SVD for collaborative filtering
- **Cosine Similarity** - Computing document similarity scores
- **Data Processing** - pandas DataFrames, merging, grouping
- **scikit-learn** - TfidfVectorizer, linear_kernel, TruncatedSVD

### Web Development
- **Django MVC** - Models, Views, Templates architecture
- **URL Routing** - Multi-page application with dynamic URLs
- **Template Rendering** - Context passing, loops, conditionals
- **Form Handling** - GET parameters, user input validation
- **Error Handling** - Try-except blocks with user-friendly messages

### Software Engineering
- **Project Structure** - Separation of ML code from web code
- **Environment Configuration** - .env files for secrets management
- **Dependency Management** - requirements.txt for reproducibility
- **Code Organization** - Modular design with clear responsibilities
- **Version Control** - Git-ready structure with proper .gitignore

## 🔒 Security Notes

- ✅ Django SECRET_KEY loaded from `.env` file (never hardcoded)
- ✅ `.env` included in `.gitignore` to prevent exposure
- ✅ `.env.example` template provided for easy setup
- ✅ No sensitive user data collected or stored
- ✅ Uses public movie datasets (TMDB-based data)
- ⚠️ **Important:** DEBUG=True in settings.py is for development only
- ⚠️ **Production:** Set DEBUG=False and configure ALLOWED_HOSTS before deploying

### .gitignore Configuration
Ensure your `.gitignore` includes:
```
.env
.env.*
!.env.example
*.pyc
__pycache__/
db.sqlite3
.venv/
```

## 🚧 Future Enhancements

Potential improvements for extended functionality:

### Algorithm Improvements
- [ ] **Hybrid Recommender** - Combine multiple algorithms with weighted scoring
- [ ] **Deep Learning** - Neural collaborative filtering with embeddings
- [ ] **Real-Time Updates** - Incremental model updates as users rate
- [ ] **Cold Start Handling** - Better recommendations for new users/movies
- [ ] **Genre Filtering** - Allow users to filter by genre preferences
- [ ] **Temporal Dynamics** - Account for rating timestamp patterns

### User Experience
- [ ] **User Accounts** - Django authentication for personalized profiles
- [ ] **Rating System** - Allow users to rate movies and update recommendations
- [ ] **Search Functionality** - Autocomplete movie title search
- [ ] **Movie Details Page** - Show cast, director, release year, plot
- [ ] **Watchlist Feature** - Save movies to watch later
- [ ] **Recommendation Explanations** - Show why a movie was recommended

### Technical Improvements
- [ ] **Caching** - Redis cache for expensive ML computations
- [ ] **Async Processing** - Celery tasks for background algorithm execution
- [ ] **API Endpoints** - RESTful API with Django REST Framework
- [ ] **PostgreSQL** - Production database instead of SQLite
- [ ] **Docker** - Containerize application for easy deployment
- [ ] **Testing** - Unit tests for algorithms and views
- [ ] **CI/CD** - GitHub Actions for automated testing

### Data Enhancements
- [ ] **Larger Dataset** - Integrate full TMDB or MovieLens dataset
- [ ] **More Metadata** - Include genres, directors, actors in recommendations
- [ ] **Image Integration** - Display movie posters from TMDB API
- [ ] **Ratings Distribution** - Show rating histograms and statistics

## 🐛 Troubleshooting

### Common Issues

**Problem:** `ValueError: SECRET_KEY not found in environment variables`
- **Solution:** Create `.env` file from `.env.example` and add SECRET_KEY

**Problem:** `ModuleNotFoundError: No module named 'dotenv'`
- **Solution:** Activate virtual environment and run `pip install -r requirements.txt`

**Problem:** Migrations warning on server start
- **Solution:** Run `python manage.py migrate` to apply database migrations

**Problem:** Movie not found in content-based recommendations
- **Solution:** Check exact movie title spelling; titles are case-sensitive

**Problem:** Collaborative filtering returns no results for user
- **Solution:** User ID may not exist in ratings data; try user IDs 1-600

**Problem:** Empty recommendation results
- **Solution:** Verify CSV files exist in `data/` folder with correct structure

**Problem:** TF-IDF memory error on large datasets
- **Solution:** Reduce dataset size or increase max_features parameter

## 💡 Dataset Information

The project uses movie data with the following structure:

**movies.csv**
- Columns: `id`, `title`, `overview`, `genres`, etc.
- ~1000+ movies with metadata
- Source: TMDB-style movie database

**ratings.csv**
- Columns: `userId`, `movieId`, `rating`, `timestamp`
- User ratings on 1-5 scale
- Source: User rating history

**credits.csv**
- Columns: `id`, `cast`, `crew`
- Cast and crew information
- Used for potential future enhancements

## 📞 Contact & Portfolio

**Developer:** StackDevOps8999
**GitHub:** [@HDShovelHead76](https://github.com/HDShovelHead76)  
**Portfolio:** [Python Portfolio Projects](https://github.com/HDShovelHead76/Python-Portfolio-Projects)

---

## 📝 License

This project is available for educational and personal use. Feel free to modify and extend for your own learning purposes.

---

*Built as part of Python learning journey - demonstrating full-stack machine learning integration, recommendation algorithms, and Django web development*
