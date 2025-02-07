<<<<<<< HEAD
# GeoWall Guardians 🌍

**GeoWall Guardians** is a web application designed for geospatial analysis, offering an interactive map interface and advanced analytical tools to predict locust breeding grounds using satellite imagery and machine learning.

---
## 🚀 Features
- **Time Range Settings:** Choose start and end dates for analysis.
- **Parameter Settings:**
  - Time Step (1-60 days)
  - Confidence Threshold for prediction (0.0-1.0)
- **Mask Settings:**
  - Cloud Masking
  - Water Body Masking
- **Interactive Map Functionality:**
  - Support for multiple regions (East Africa, West Africa, North Africa, Middle East)
  - Multiple map layers (OpenStreetMap, Terrain maps)
  - Map zooming and panning support

---
## 🛠️ System Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning repositories)

---
## 📥 Installation Steps

### 1. Clone or Download the Project
```bash
# Clone the repository
git clone https://github.com/yourusername/GEOWALL.git

# Or download the ZIP archive and unzip it
```

### 2. Create and Activate a Virtual Environment

#### **Windows:**
```bash
# Navigate to the project directory
cd GEOWALL/app

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
```

#### **Linux/Mac:**
```bash
# Navigate to the project directory
cd GEOWALL/app

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install streamlit folium streamlit-folium
```

---
## 🎮 Run the Application

### 1. Navigate to the App Directory
```bash
cd GEOWALL/app
```

### 2. Launch the Application
```bash
streamlit run app.py
```

### 3. Access the Application
- **Local Access:** [http://localhost:8501](http://localhost:8501)
- **Network Access:** [http://your-ip-address:8501](http://your-ip-address:8501)

---
## 📊 Functional Description

### 🔧 Time Range Settings
- Select the start and end dates for analysis.
- The system automatically verifies the validity of the date range.

### ⚙️ Parameter Settings
- **Time Step:** Define the time interval for analysis (1-60 days).
- **Confidence Threshold:** Set the confidence threshold for predictions (0.0-1.0).

### 🌫️ Mask Settings
- **Cloud Mask:** Enable or disable cloud masking.
- **Water Mask:** Enable or disable water body masking.

### 🗺️ Map Features
- Multiple supported regions (East Africa, West Africa, North Africa, Middle East).
- Interactive map layers (OpenStreetMap, terrain maps).
- Support for zooming and panning.

---
## ❓ Common Troubleshooting

### 1. **No module named 'streamlit'**
```bash
pip install streamlit
```

### 2. **Port is Occupied**
```bash
streamlit run app.py --server.port 8502
```

### 3. **Updating Dependencies**
```bash
pip install --upgrade streamlit folium streamlit-folium
```

---
## 📋 Notes
- Ensure the virtual environment is activated (you should see `(venv)` before the command prompt).
- Verify that all dependencies are installed correctly.
- If you use a proxy, you may need to set proxy environment variables.

---
## 🔧 Technical Support

If you encounter problems:
1. Verify that all installation steps were followed correctly.
2. Confirm the versions of Python and all dependencies.
3. Review the error messages and search for relevant solutions.

---
## 📜 License
This project is licensed under the MIT License.

---
## ❤️ Acknowledgments
Powered by InstaGeo | GeoAI Hackathon

=======
# GeoWall Guardians 🌍

**GeoWall Guardians** is a web application designed for geospatial analysis, offering an interactive map interface and advanced analytical tools to predict locust breeding grounds using satellite imagery and machine learning.

---
## 🚀 Features
- **Time Range Settings:** Choose start and end dates for analysis.
- **Parameter Settings:**
  - Time Step (1-60 days)
  - Confidence Threshold for prediction (0.0-1.0)
- **Mask Settings:**
  - Cloud Masking
  - Water Body Masking
- **Interactive Map Functionality:**
  - Support for multiple regions (East Africa, West Africa, North Africa, Middle East)
  - Multiple map layers (OpenStreetMap, Terrain maps)
  - Map zooming and panning support

---
## 🛠️ System Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning repositories)

---
## 📥 Installation Steps

### 1. Clone or Download the Project
```bash
# Clone the repository
git clone https://github.com/yourusername/GEOWALL.git

# Or download the ZIP archive and unzip it
```

### 2. Create and Activate a Virtual Environment

#### **Windows:**
```bash
# Navigate to the project directory
cd GEOWALL/app

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
```

#### **Linux/Mac:**
```bash
# Navigate to the project directory
cd GEOWALL/app

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install streamlit folium streamlit-folium
```

---
## 🎮 Run the Application

### 1. Navigate to the App Directory
```bash
cd GEOWALL/app
```

### 2. Launch the Application
```bash
streamlit run app.py
```

### 3. Access the Application
- **Local Access:** [http://localhost:8501](http://localhost:8501)
- **Network Access:** [http://your-ip-address:8501](http://your-ip-address:8501)

---
## 📊 Functional Description

### 🔧 Time Range Settings
- Select the start and end dates for analysis.
- The system automatically verifies the validity of the date range.

### ⚙️ Parameter Settings
- **Time Step:** Define the time interval for analysis (1-60 days).
- **Confidence Threshold:** Set the confidence threshold for predictions (0.0-1.0).

### 🌫️ Mask Settings
- **Cloud Mask:** Enable or disable cloud masking.
- **Water Mask:** Enable or disable water body masking.

### 🗺️ Map Features
- Multiple supported regions (East Africa, West Africa, North Africa, Middle East).
- Interactive map layers (OpenStreetMap, terrain maps).
- Support for zooming and panning.

---
## ❓ Common Troubleshooting

### 1. **No module named 'streamlit'**
```bash
pip install streamlit
```

### 2. **Port is Occupied**
```bash
streamlit run app.py --server.port 8502
```

### 3. **Updating Dependencies**
```bash
pip install --upgrade streamlit folium streamlit-folium
```

---
## 📋 Notes
- Ensure the virtual environment is activated (you should see `(venv)` before the command prompt).
- Verify that all dependencies are installed correctly.
- If you use a proxy, you may need to set proxy environment variables.

---
## 🔧 Technical Support

If you encounter problems:
1. Verify that all installation steps were followed correctly.
2. Confirm the versions of Python and all dependencies.
3. Review the error messages and search for relevant solutions.

---
## 📜 License
This project is licensed under the MIT License.

---
## ❤️ Acknowledgments
Powered by InstaGeo | GeoAI Hackathon

>>>>>>> f4ef771 (add vz)
