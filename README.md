# 🌫️ Climate Visibility Prediction System

A machine learning-powered fog prediction and visibility forecasting system for JFK Airport, built with Streamlit and XGBoost.

## 📋 Overview

This project analyzes weather conditions to predict fog formation and visibility levels at JFK Airport. The system uses historical weather data including temperature, humidity, dew point, wind speed, and time of day to provide real-time fog alerts and visibility estimates.

## 🚀 Features

- **Real-time Fog Prediction**: Classifies fog risk into three levels (Clear, Yellow Alert, Red Alert)
- **Visibility Forecasting**: Predicts visibility distance in kilometers
- **Interactive Web Interface**: Built with Streamlit for easy use
- **Machine Learning Models**: XGBoost-based predictions trained on historical JFK weather data
- **Data Analysis**: Comprehensive EDA notebook for weather pattern insights

## 🏗️ Project Structure

```
├── app/
│   └── app.py                 # Streamlit web application
├── models/
│   ├── fog_model.pkl         # Trained fog prediction model
│   ├── visibility_model.pkl  # Trained visibility prediction model
│   └── features.pkl          # Feature list for model input
├── notebooks/
│   ├── eda.ipynb            # Exploratory Data Analysis notebook
│   └── jfk_weather_cleaned.csv # Cleaned JFK weather dataset
├── utils/
│   └── predict.py           # Prediction functions and model loading
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd climate-visibility-ml-project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app/app.py
   ```

2. **Access the application:**
   Open your browser and navigate to `http://localhost:8501`

3. **Input weather conditions:**
   - Relative Humidity (%)
   - Dry Bulb Temperature (°F)
   - Dew Point Temperature (°F)
   - Wind Speed (mph)
   - Hour of Day

4. **Get predictions:**
   - Fog risk level with probability
   - Visibility distance in kilometers

## 📊 Model Details

### Fog Prediction Model
- **Algorithm**: XGBoost Classifier
- **Output**: Probability of fog formation
- **Alert Levels**:
  - 🟢 **Clear**: Low fog risk (< 40%)
  - 🟡 **Yellow Alert**: Moderate fog risk (40-70%)
  - 🔴 **Red Alert**: High fog risk (> 70%)

### Visibility Prediction Model
- **Algorithm**: XGBoost Regressor
- **Output**: Visibility distance in kilometers
- **Features**: Weather conditions + derived dew point depression

## 📈 Data Analysis

The project includes an exploratory data analysis notebook (`notebooks/eda.ipynb`) that:
- Analyzes JFK Airport weather patterns
- Identifies correlations between weather variables and visibility
- Visualizes fog formation conditions
- Prepares data for model training

## 🔧 Dependencies

Key libraries used:
- **streamlit**: Web application framework
- **xgboost**: Machine learning algorithms
- **pandas**: Data manipulation
- **numpy**: Numerical computations
- **scikit-learn**: Machine learning utilities
- **matplotlib/seaborn**: Data visualization

See `requirements.txt` for complete list of dependencies.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## � Author

**Abhinay Pal**

## �🙏 Acknowledgments

- JFK Airport weather data
- XGBoost for powerful gradient boosting algorithms
- Streamlit for making ML apps accessible

---

**Built with ❤️ for safer aviation through better weather prediction**