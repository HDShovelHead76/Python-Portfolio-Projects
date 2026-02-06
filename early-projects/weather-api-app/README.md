# Weather Data API - Historical Temperature Analysis

**Developer:** StackDevOps8999  
**Technologies:** Flask 3.1.1, Python 3.13, Pandas, European Climate Assessment Dataset  
**Status:** Complete ✅

---

## 📋 Overview

A Flask-based REST API for accessing and analyzing historical temperature data from the **European Climate Assessment & Dataset (ECA&D)**. Users can query temperature records from 95 weather stations across Europe, with data spanning from **1860 to present day**.

This application provides:
- Web interface for temperature data exploration
- RESTful API endpoints for programmatic access
- Station-specific historical temperature queries
- Date-range filtering (by year and month)
- Daily mean temperature readings
- Data quality indicators

**Data Source:** Klein Tank, A.M.G. and Coauthors, 2002. Daily dataset of 20th-century surface air temperature and precipitation series for the European Climate Assessment. Int. J. of Climatol., 22, 1441-1453.

---

## ✨ Key Features

### **For End Users:**
- **Web Interface:** User-friendly HTML pages for data exploration
- **Station Lookup:** Browse all available weather stations
- **Historical Data Access:** View temperature records from 1860-present
- **Date Filtering:** Query specific years or months
- **Quality Indicators:** See data quality codes (valid, suspect, missing)
- **Visual Presentation:** Clean HTML tables with temperature data

### **For Developers:**
- **REST API Endpoints:** JSON responses for programmatic access
- **Station Data API:** `/api/v1/station/<station_id>`
- **Date-Specific API:** `/api/v1/station/<station_id>/<date>`
- **Year/Month Filtering:** `/api/v1/station/<station_id>/<year>/<month>`
- **Pandas Integration:** Efficient data processing with DataFrames
- **Flexible Queries:** Multiple endpoint patterns supported

### **Data Features:**
- **95 Weather Stations:** Across Europe
- **165+ Years of Data:** From 1860 to 2022
- **Daily Granularity:** Mean temperature per day
- **Temperature Precision:** 0.1°C accuracy
- **Quality Codes:** 0=Valid, 1=Suspect, 9=Missing
- **Metadata Included:** Station IDs, source IDs, dates

---

## 🛠️ Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| **Flask** | 3.1.1 | Web framework and REST API |
| **Python** | 3.13 | Core programming language |
| **Pandas** | 2.3.1 | Data processing and CSV parsing |
| **NumPy** | 2.3.1 | Numerical computations |
| **Jinja2** | 3.1.6 | HTML template rendering |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
   cd Python-Portfolio-Projects/early-projects/weather-api-app
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

4. **Set up environment variables (optional):**
   ```bash
   cp .env.example .env
   # Edit .env if needed (defaults work fine)
   ```

5. **Run the application:**
   ```bash
   python main.py
   ```

6. **Access the application:**
   - **Web Interface:** http://127.0.0.1:5000/
   - **API Base:** http://127.0.0.1:5000/api/v1/

---

## 🚀 Usage

### **Web Interface:**

#### **Home Page**
- Navigate to: http://127.0.0.1:5000/
- View welcome page and station information
- Browse available API endpoints

#### **View All Station Data**
- URL Pattern: `/station/<station_id>`
- Example: http://127.0.0.1:5000/station/1
- Shows: All temperature records for Station 1 (Vaexjoe, Sweden)

#### **View Specific Date**
- URL Pattern: `/station/<station_id>/<date>`
- Example: http://127.0.0.1:5000/station/1/1860-01-01
- Shows: Temperature for specific date
- Date Format: YYYY-MM-DD

#### **View Year Data**
- URL Pattern: `/station/<station_id>/<year>/<month>`
- Example: http://127.0.0.1:5000/station/1/1860/1
- Shows: All temperatures for January 1860

---

### **API Endpoints:**

#### **1. Get All Station Data**

```bash
curl http://127.0.0.1:5000/api/v1/station/1
```

**Response:**
```json
{
  "station_id": "1",
  "station_name": "VAEXJOE, SWEDEN",
  "data": [
    {
      "date": "1860-01-01",
      "temperature": 2.1,
      "quality": "valid"
    },
    ...
  ]
}
```

#### **2. Get Temperature for Specific Date**

```bash
curl http://127.0.0.1:5000/api/v1/station/1/1860-01-01
```

**Response:**
```json
{
  "station_id": "1",
  "date": "1860-01-01",
  "temperature": 2.1,
  "quality": "valid"
}
```

#### **3. Get All Data for Year and Month**

```bash
curl http://127.0.0.1:5000/api/v1/station/1/1860/1
```

**Response:**
```json
{
  "station_id": "1",
  "year": "1860",
  "month": "01",
  "data": [
    {
      "date": "1860-01-01",
      "temperature": 2.1,
      "quality": "valid"
    },
    ...
  ],
  "count": 31
}
```

#### **4. Get Available Stations List**

```bash
# Read stations.txt file
cat data_small/stations.txt
```

---

## 📁 Project Structure

```
weather-api-app/
├── main.py                          # Flask application and API routes
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── .env.example                     # Environment variables template
│
├── data_small/                      # Weather data (95 stations)
│   ├── stations.txt                 # Station metadata and IDs
│   ├── TG_STAID000001.txt          # Station 1 temperature data
│   ├── TG_STAID000002.txt          # Station 2 temperature data
│   └── ...                          # (93 more station files)
│
├── static/
│   └── cat.png                      # Static image asset
│
└── templates/
    ├── home.html                    # Home page template
    ├── station_data.html            # All station data view
    └── station_date.html            # Specific date view
```

---

## 🗄️ Data Format

### **Station Data Files (TG_STAID*.txt)**

Each file contains daily mean temperatures for one weather station.

**File Format:**
```
STAID, SOUID,    DATE,   TG, Q_TG
    1, 35381,18600101,   21,    0
    1, 35381,18600102,   46,    0
```

**Column Descriptions:**

| Column | Format | Description |
|--------|--------|-------------|
| `STAID` | Integer | Station identifier (1-95) |
| `SOUID` | Integer | Source identifier |
| `DATE` | YYYYMMDD | Observation date |
| `TG` | Integer | Mean temperature in 0.1°C (divide by 10 for °C) |
| `Q_TG` | Integer | Quality code: 0=Valid, 1=Suspect, 9=Missing |

**Example:**
- `TG = 21` → 2.1°C
- `TG = -45` → -4.5°C
- `TG = 0` → 0.0°C

### **Missing Value Code**
- `-9999` indicates missing data

---

## 🌍 Available Weather Stations

**Sample Stations (95 total):**

| Station ID | Location | Data Start | Country |
|------------|----------|------------|---------|
| 1 | Vaexjoe | 1860 | Sweden |
| 2-95 | Various European locations | 1860-2000 | Multiple |

**Full station list:** See `data_small/stations.txt`

---

## 🔧 Configuration

### **Flask Configuration**

```python
# In main.py
app = Flask(__name__)
app.config['DEBUG'] = True

# Default host and port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### **Environment Variables (.env)**

```bash
FLASK_SECRET_KEY=your-secret-key-here
FLASK_ENV=development
DEBUG=True
HOST=0.0.0.0
PORT=5000
```

---

## 📊 Sample Queries

### **Temperature Analysis Examples:**

#### **Coldest Day at Station 1**
```python
import pandas as pd

df = pd.read_csv('data_small/TG_STAID000001.txt', skiprows=20, skipinitialspace=True)
df['TG'] = df['TG'] / 10  # Convert to °C
coldest = df[df['TG'] == df['TG'].min()]
print(coldest)
```

#### **Monthly Average Temperature**
```python
# Via API
import requests

response = requests.get('http://127.0.0.1:5000/api/v1/station/1/1860/1')
data = response.json()

temps = [record['temperature'] for record in data['data']]
avg_temp = sum(temps) / len(temps)
print(f"Average January 1860 temperature: {avg_temp:.1f}°C")
```

#### **Year-over-Year Comparison**
```python
# Compare January temperatures across years
years = [1860, 1900, 1950, 2000]

for year in years:
    response = requests.get(f'http://127.0.0.1:5000/api/v1/station/1/{year}/1')
    data = response.json()
    temps = [r['temperature'] for r in data['data']]
    avg = sum(temps) / len(temps)
    print(f"{year}: {avg:.1f}°C")
```

---

## 🎓 Learning Objectives Demonstrated

This project showcases proficiency in:

✅ **REST API Development:**
- Multiple endpoint patterns
- JSON response formatting
- URL parameter handling
- RESTful design principles

✅ **Data Processing:**
- CSV file parsing with Pandas
- Data cleaning and transformation
- Temperature unit conversions
- Date manipulation and filtering

✅ **Flask Web Development:**
- Route handling
- Template rendering with Jinja2
- Static file serving
- Error handling

✅ **Historical Data Analysis:**
- Time-series data management
- Quality indicator interpretation
- Date-range queries
- Statistical computations

---

## 🌡️ Temperature Data Notes

### **Understanding the Data:**

**Temperature Format:**
- Stored as integers in tenths of degrees Celsius
- `21` = 2.1°C = 35.78°F
- `0` = 0.0°C = 32.0°F
- `-45` = -4.5°C = 23.9°F

**Quality Codes:**
- **0 = Valid:** Data passed quality checks
- **1 = Suspect:** Data may be questionable
- **9 = Missing:** No data available for this date

**Data Gaps:**
- Some stations have incomplete records
- Missing values coded as `-9999`
- Early years (1860s) may have more gaps

---

## 🚧 Future Enhancements

### **Potential Improvements:**

- [ ] Add data visualization (charts/graphs)
- [ ] Temperature unit conversion (°C ↔ °F)
- [ ] Statistical analysis endpoints (min, max, avg)
- [ ] Date range queries (start_date to end_date)
- [ ] Export to CSV/Excel
- [ ] Search by location/country
- [ ] Climate trend analysis
- [ ] Multiple stations comparison
- [ ] Interactive map of stations
- [ ] Historical anomaly detection

### **Advanced Features:**

- [ ] Machine learning for temperature prediction
- [ ] Climate change trend visualization
- [ ] Seasonal pattern analysis
- [ ] Extreme weather event detection
- [ ] API rate limiting
- [ ] Authentication for API access
- [ ] Caching for performance
- [ ] Database migration (CSV → PostgreSQL)
- [ ] Real-time data updates
- [ ] Mobile app integration

---

## 🧪 Testing

### **Manual Testing:**

```bash
# Test home page
curl http://127.0.0.1:5000/

# Test station data
curl http://127.0.0.1:5000/api/v1/station/1

# Test specific date
curl http://127.0.0.1:5000/api/v1/station/1/1860-01-01

# Test year/month query
curl http://127.0.0.1:5000/api/v1/station/1/1860/1

# Test invalid station (should handle gracefully)
curl http://127.0.0.1:5000/api/v1/station/999

# Test invalid date format
curl http://127.0.0.1:5000/api/v1/station/1/invalid-date
```

---

## 📚 Data Attribution

**Dataset:** European Climate Assessment & Dataset (ECA&D)

**Citation:**
Klein Tank, A.M.G. and Coauthors, 2002. Daily dataset of 20th-century surface air temperature and precipitation series for the European Climate Assessment. Int. J. of Climatol., 22, 1441-1453.

**Data Source:** http://www.ecad.eu

**Usage:** This data can be used for non-commercial research and education provided that the source is acknowledged.

---

## 📧 Contact

**Developer:** StackDevOps8999  
**GitHub:** [HDShovelHead76](https://github.com/HDShovelHead76)  
**Portfolio:** [Python Portfolio Projects](https://github.com/HDShovelHead76/Python-Portfolio-Projects)

---

## 📄 License

This project is part of a learning portfolio and is available for educational purposes.

**Data License:** ECA&D data is available for non-commercial research and education use.

---

## 🙏 Acknowledgments

- European Climate Assessment & Dataset (ECA&D)
- Klein Tank, A.M.G. and Coauthors (2002)
- Built with Flask and Pandas
- Historical temperature data from 95 European weather stations
- Part of comprehensive software development portfolio

---

## 📝 Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/HDShovelHead76/Python-Portfolio-Projects.git
cd Python-Portfolio-Projects/early-projects/weather-api-app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run application
python main.py

# Access
# Web: http://127.0.0.1:5000/
# API: http://127.0.0.1:5000/api/v1/station/1

# Example queries
curl http://127.0.0.1:5000/api/v1/station/1/1860/1
curl http://127.0.0.1:5000/api/v1/station/1/2020-01-01
```

---

## 🔍 Example Use Cases

### **Climate Research:**
- Analyze 165-year temperature trends
- Study seasonal variations
- Identify extreme weather events
- Compare historical vs modern temperatures

### **Education:**
- Teach data analysis with real datasets
- Demonstrate REST API development
- Practice Pandas data processing
- Learn Flask web development

### **Software Development:**
- Portfolio project showcase
- API design patterns
- Data processing examples
- Web framework implementation

---

**Note:** This application provides access to historical European temperature data for educational and research purposes. The dataset spans from 1860 to 2022 and includes 95 weather stations across Europe.
