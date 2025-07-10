# 🌿 GreenGuard AI - AI-Powered Agricultural Assistant

**An intelligent web application providing comprehensive agricultural solutions through AI-powered crop management, disease detection, and farming assistance.**

## 📖 Overview

GreenGuard AI is a Flask-based web application designed to empower farmers and agricultural enthusiasts with cutting-edge AI technology. The platform combines machine learning models, real-time data integration, and intelligent chatbot assistance to provide end-to-end agricultural support - from crop selection to disease management and market analysis.

**Target Users:** Farmers, agricultural researchers, gardening enthusiasts, and agribusiness professionals seeking data-driven farming solutions.

## 🚀 Features

### 🌱 **Plant Disease Detection**
- **AI-powered image analysis** using MobileNet deep learning model
- **Support for 40+ plant diseases** across multiple crop types (Apple, Bell Pepper, Corn, Tomato, etc.)
- **Real-time diagnosis** with confidence scoring
- **Treatment recommendations** and symptom analysis for identified diseases

### 🌾 **Intelligent Crop Recommendation**
- **ML-based crop prediction** using soil and environmental parameters
- **Input parameters:** Nitrogen, Phosphorus, Potassium levels, temperature, humidity, pH, rainfall
- **22 crop varieties** supported including Rice, Maize, Cotton, Coffee, and more
- **Data-driven suggestions** for optimal crop selection

### 🧪 **Fertilizer Recommendation System**
- **Decision tree-based fertilizer suggestions** tailored to specific crop and soil conditions
- **Comprehensive input analysis:** soil color, NPK levels, pH, rainfall, temperature, crop type
- **Personalized recommendations** with detailed fertilizer information and application guidelines

### ☁️ **Weather & Market Intelligence**
- **Real-time weather data** integration via OpenWeather API
- **Current and forecast weather** for location-based farming decisions
- **Commodity price tracking** using government data sources (data.gov.in API)
- **Price prediction models** for 23+ agricultural commodities
- **Market trend analysis** for informed selling decisions

### 💬 **AI Chat Assistant "Bloom"**
- **RAG-powered chatbot** using LangChain and Ollama/Groq LLMs
- **Agriculture-specific knowledge base** with vector embeddings
- **Natural language queries** for farming advice and troubleshooting
- **Context-aware responses** limited to 10-30 words for quick insights

### 🤝 **Community Platform**
- **Farmer community forum** for knowledge sharing
- **Image and text posting** capabilities
- **Real-time message exchange** among registered users
- **Experience sharing** and collaborative problem-solving

### 📰 **Agricultural News Integration**
- **Automated news scraping** from agricultural news sources
- **Region-specific updates** (Tamil Nadu agriculture focus)
- **Latest market trends** and government policy updates

## 🛠️ Tech Stack

**Backend Framework:**
- **Flask 2.x** - Python web framework
- **SQLite** - Database for user management and community features
- **Gunicorn** - WSGI HTTP Server for production deployment

**Machine Learning & AI:**
- **TensorFlow/Keras** - Deep learning models for disease detection
- **scikit-learn** - Crop recommendation and fertilizer prediction models
- **LangChain** - RAG framework for AI chatbot
- **Ollama** - Local LLM deployment (Llama 3.1)
- **ChromaDB** - Vector database for document embeddings

**Data Processing:**
- **NumPy & Pandas** - Data manipulation and analysis
- **BeautifulSoup4** - Web scraping for news aggregation
- **Requests** - API integration for weather and price data

**Frontend Technologies:**
- **HTML/CSS/JavaScript** - Responsive web interface
- **Bootstrap 4** - UI framework
- **jQuery** - Frontend JavaScript library
- **Chart.js** - Data visualization

**Security & Authentication:**
- **bcrypt** - Password hashing
- **Flask Sessions** - User session management
- **CSRF Protection** - Secure form handling

## 📁 Project Structure

```
GreenGuardAPP-master/
├── app.py                    # Flask application entry point
├── config.py                 # Configuration settings and API keys
├── main.db                   # SQLite database
├── requirements.txt          # Python dependencies
├── runtime.txt              # Python version specification
│
├── routes/                   # Blueprint route modules
│   ├── auth_routes.py       # Authentication (login/register/logout)
│   ├── crop_routes.py       # Crop recommendation functionality
│   ├── disease_routes.py    # Disease detection and analysis
│   ├── fertilizer_routes.py # Fertilizer recommendation
│   ├── weather_routes.py    # Weather data integration
│   ├── price_routes.py      # Commodity price prediction
│   ├── chat_routes.py       # AI chatbot functionality
│   ├── community_routes.py  # Community forum features
│   ├── news_routes.py       # Agricultural news aggregation
│   └── general_routes.py    # General pages (index, about)
│
├── models/                   # Pre-trained ML models
│   ├── crop_recommendation/ # Crop prediction models and scalers
│   ├── disease_detection/   # MobileNet disease classification model
│   └── fertilizer_recommendation/ # Decision tree and transformer
│
├── utils/                    # Utility modules
│   ├── authentication.py   # Password hashing and login decorators
│   ├── database.py         # Database connection and table creation
│   └── chatbot/             # AI chatbot components
│       ├── models.py        # LangChain model initialization
│       └── ingest.py        # Document processing for RAG
│
├── services/                 # Business logic services
│   ├── disease_detection.py # Image preprocessing and prediction
│   └── crops.py             # Crop-related data processing
│
├── resources/               # Data files and configurations
│   ├── disease.py          # Disease information database
│   └── fertilizer.py       # Fertilizer details and recommendations
│
├── data/                    # Historical crop price data
│   └── crop_data/          # CSV files for 23 commodities
│
├── templates/               # HTML templates
│   ├── index.html          # Dashboard homepage
│   ├── login.html          # User authentication
│   ├── disease-detection.html
│   ├── crop-prediction.html
│   ├── fertilizer-recommendation.html
│   ├── chat-assistant.html
│   ├── community.html
│   └── [other templates]
│
└── static/                  # Static assets
    ├── css/                # Stylesheets
    ├── js/                 # JavaScript files
    ├── images/             # Application images
    └── uploads/            # User-uploaded files
```

## ⚙️ Installation Guide

### Prerequisites
- **Python 3.10.8** (specified in runtime.txt)
- **pip** package manager
- **Git** for version control

### Step 1: Clone the Repository
```bash
git clone https://github.com/PGV-da/Green-Guard-AI.git
cd Green-Guard-AI
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration
Create a `config.env` file in the root directory:
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=main.db
WEATHER_API_KEY=your_openweather_api_key
GROQ_API_KEY=your_groq_api_key
PORT=4000
```

### Step 5: Set Up AI Models

**For Local Ollama Setup:**
```bash
# Install Ollama (https://ollama.ai/)
ollama pull llama3.1
ollama pull tazarov/all-minilm-l6-v2-f32
```

**Alternative: Use Groq API** (recommended for production)
- Sign up at [Groq Console](https://console.groq.com/)
- Add your API key to `config.env`

### Step 6: Initialize Database
```bash
python app.py
# This will create the SQLite database and required tables
```

## 💻 How to Run

### Development Mode
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Run the application
python app.py
```

The application will be available at `http://localhost:4000`

### Production Deployment
```bash
# Using Gunicorn (included in requirements.txt)
gunicorn --bind 0.0.0.0:4000 app:app

# Or with environment variables
PORT=4000 gunicorn --bind 0.0.0.0:$PORT app:app
```

### Docker Deployment (Optional)
```dockerfile
FROM python:3.10.8-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 4000

CMD ["gunicorn", "--bind", "0.0.0.0:4000", "app:app"]
```

## 🧪 Testing

### Manual Testing
1. **User Registration/Login**
   - Navigate to `/register` to create an account
   - Use `/` to login with credentials

2. **Disease Detection**
   - Go to `/disease/diseasedetection`
   - Upload a plant image (JPEG/PNG)
   - Verify disease prediction and confidence score

3. **Crop Recommendation**
   - Access `/crop/crop-recommendation`
   - Input soil parameters (N, P, K, temperature, humidity, pH, rainfall)
   - Check recommended crop output

4. **AI Chatbot**
   - Visit `/chatassistant`
   - Ask agriculture-related questions
   - Verify contextual responses from Bloom AI

5. **Weather Integration**
   - Test `/currentweather` with location coordinates
   - Verify real-time weather data display

### API Testing
```bash
# Test commodity prices API
curl -X GET "http://localhost:4000/api/commodity-prices"

# Test chat API
curl -X POST "http://localhost:4000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "How to prevent tomato blight?"}'
```

### Model Validation
- **Disease Detection:** Test with sample plant images from each disease category
- **Crop Recommendation:** Validate with known good/bad parameter combinations
- **Price Prediction:** Compare predictions with historical price data

---

**Contributing:** Fork the repository, create feature branches, and submit pull requests for improvements.

**License:** Check the LICENSE file for project licensing information.

**Support:** Open issues on GitHub for bug reports or feature requests.
