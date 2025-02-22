# 🌿 Green Guard AI – AI-Powered Agricultural Assistant 🚀

<!-- ![Green Guard AI](https://your-image-url.com)  Replace with a relevant project banner -->

## 🌟 Overview

**Green Guard AI** is an **AI-powered agricultural assistant** that helps farmers, gardeners, and agricultural professionals make **data-driven decisions** for better **plant health, crop management, and sustainable farming**. The core of this project is **Plant Disease Detection**, which enables farmers to **identify plant diseases using AI-based image analysis**. Additionally, it provides **fertilizer recommendations, crop prediction, and weather insights** to enhance agricultural productivity.

---

## 🚀 Features

### 🌱 **1. Plant Disease Detection (Main Module)**

- Upload a **leaf image**, and AI will **analyze and detect** plant diseases.
- Uses **Machine Learning (TensorFlow/Keras)** for **image classification**.
- Provides **disease diagnosis and suggested treatments**.

### 🌾 **2. AI-Based Crop Prediction**

- Suggests the **best crops** based on soil, climate, and nutrient levels.
- Uses **ML models** to analyze environmental conditions.

### 🧪 **3. Fertilizer Recommendation System**

- Analyzes **soil nutrients (NPK, Zn, Mg, S, etc.)** and suggests **optimal fertilizers**.
- Supports **organic & chemical fertilizers** for different crop types.

### ☁️ **4. Weather & Market Price Forecasting**

- Provides **real-time weather updates** to help plan **irrigation, sowing, and harvesting**.
- Tracks **commodity prices** for profitable crop selling decisions.

### 💬 **5. AI Chat Assistant for Farming Queries**

- Allows users to **ask farming-related questions** (e.g., crop selection, fertilizers, pest control).
- Provides **instant AI-driven answers** based on agricultural databases.

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript (Bootstrap)
- **Database:** SQLite / Firebase
- **Machine Learning:** TensorFlow, Keras (for disease detection)
- **APIs:** Weather API, Agricultural Market API

---

## ⚙️ Installation Guide

### **🔹 1. Clone the Repository**

```bash
git clone https://github.com/your-username/green-guard-ai.git
cd green-guard-ai
```

### **🔹 2. Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### **🔹 3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **🔹 4. Run the Application**

```bash
python app.py
```

## 🔬 How to Use

Once the **Green Guard AI** application is running, you can access its features through the web interface at: http://127.0.0.1:5000/

### **🌱 1. Plant Disease Detection (Main Feature)**

1. Navigate to **http://127.0.0.1:5000/disease-detection**.
2. Upload a **leaf image** of the affected plant.
3. The AI model will **analyze and detect** potential plant diseases.
4. The system will provide:
   - **Disease Name**
   - **Possible Causes**
   - **Recommended Treatments & Solutions**

### **🌾 2. Crop Prediction**

1. Go to **http://127.0.0.1:5000/crop-prediction**.
2. Enter the required details like **soil type, pH value, and climate conditions**.
3. Click **Predict**, and the AI will recommend the **best crops** to grow.

### **🧪 3. Fertilizer Recommendation**

1. Open **http://127.0.0.1:5000/fertilizer-recommendation**.
2. Enter soil nutrient levels (**NPK, Zn, Mg, S, etc.**) into the input fields.
3. Click **Get Recommendation**, and the system will suggest the **best fertilizer options** for your crop.

### **☁️ 4. Weather & Market Price Forecasting**

1. Visit **http://127.0.0.1:5000/weather** for real-time weather updates.
2. Go to **http://127.0.0.1:5000/price-forecast** to check crop market price trends.
3. Use this information to plan irrigation, sowing, and harvesting.

### **💬 5. AI Chat Assistant (For Farming Queries)**

1. Navigate to **http://127.0.0.1:5000/chat-assistant**.
2. Ask **agriculture-related questions**, such as:
   - "Which crop is best for my soil?"
   - "How to treat fungal infections in plants?"
   - "What’s the best time to sow wheat?"
3. The chatbot will provide **instant AI-driven answers** based on agricultural research and data.

---

Now you're ready to explore **Green Guard AI** and make smarter farming decisions! 🚀  
Let me know if you need any modifications. 😊
