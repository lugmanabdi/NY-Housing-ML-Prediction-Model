# NYC Real Estate Price Prediction

A machine learning web application that predicts New York City property prices using Random Forest regression. Built with Python, Scikit-learn, and Streamlit.

## Overview

This project predicts NYC real estate prices based on property characteristics and location data. The model achieves a **71.4% R² score** and **52% MAPE** on real-world NYC housing data.

## Model Performance

- **R² Score:** 71.4% (explains 71% of price variance)
- **Mean Absolute Percentage Error:** 52%
- **Predictions within 20% of actual:** 37.1%
- **Training Dataset:** 4,000+ NYC property listings

## Features

- **Real-time price predictions** for NYC properties
- **Location-based modeling** using NYC boroughs and neighborhoods
- **Interactive web interface** built with Streamlit
- **Comprehensive data preprocessing** with outlier detection and removal
- **Hyperparameter optimization** using GridSearchCV

## Technologies Used

- **Python** - Core programming language
- **Scikit-learn** - Machine learning framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Streamlit** - Web application framework
- **Jupyter Notebooks** - Development environment

## Project Structure

```
NY-Housing-ML-Prediction-Model/
├── README.md                                    # Project documentation
└── NY Housing ML Prediction Model/             # Main project folder
    ├── app.py                              # Streamlit web application
    ├── model.pkl                           # Trained Random Forest model
    ├── NYHouseDataset.csv                  # Raw dataset
    └── notebook.ipynb                      # Jupyter notebook with model development
```

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/lugmanabdi/NY-Housing-ML-Prediction-Model.git
   cd "NY Housing ML Prediction Model/NYC-Housing-ML-Prediction"
   ```

2. **Install required packages**
   ```bash
   pip install pandas numpy scikit-learn streamlit joblib
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** to `http://localhost:8501`

## Model Development Process

### 1. Data Preprocessing
- Removed pricing outliers (properties under $50K and over $100M)
- Filtered non-active listings (pending, contingent, foreclosure)
- Cleaned 306 problematic entries from 4,207 total properties

### 2. Feature Engineering
- Applied one-hot encoding to categorical variables using `pd.get_dummies()`
- Incorporated location features (boroughs and neighborhoods)
- Feature set: bedrooms, bathrooms, square footage, property type, locality, sublocality

### 3. Model Training
- Used Random Forest Regressor with GridSearchCV hyperparameter tuning
- Tested 1,350+ parameter combinations
- Optimized: criterion, max_depth, min_samples_split, min_samples_leaf
- Applied 80/20 train-test split with random_state=42

### 4. Model Evaluation
- Achieved significant improvement from 59.3% to 71.4% R² score through location feature engineering
- MAPE reduced from 112% to 52% after data cleaning
- Validated performance using cross-validation

## Input Features

The model predicts prices based on:

- **Property Characteristics:**
  - Number of bedrooms (1-10)
  - Number of bathrooms (1.0-8.0)
  - Property square footage (200-15,000 sq ft)
  - Property type (House, Condo, Co-op, Townhouse, Multi-family)

- **Location Data:**
  - Borough/Area (Manhattan, Brooklyn, Queens, Bronx, Staten Island)
  - Specific neighborhoods within each borough

## Web Application

The Streamlit app provides:
- User-friendly input interface
- Real-time price predictions
- Price per square foot calculations
- Estimated price ranges
- Clean, professional design

## Key Insights

- **Location is the primary price driver** in NYC real estate
- **Manhattan properties** command significantly higher prices
- **Property size and type** are secondary factors
- **Data quality** crucial for model performance

## Future Improvements

- Add more granular location data (specific addresses)
- Incorporate building age and amenities
- Include market trend analysis
- Implement time-series forecasting
- Add property condition assessments

## Sample Predictions

| Property Type | Location | Beds | Baths | Sq Ft | Predicted Price |
|---------------|----------|------|-------|-------|----------------|
| Condo | Manhattan | 2 | 2 | 1,200 | $1,850,000 |
| House | Queens | 4 | 3 | 2,500 | $950,000 |
| Co-op | Brooklyn | 1 | 1 | 800 | $650,000 |

## Dataset Information

- **Source:** NYC real estate listings
- **Size:** 4,000+ properties after cleaning
- **Coverage:** All 5 NYC boroughs
- **Price Range:** $50,000 - $100,000,000
- **Time Period:** Recent market data

## Author

**Lugman Abdi**
- LinkedIn: [linkedin.com/in/lugman-abdi](https://linkedin.com/in/lugman-abdi)
- GitHub: [github.com/lugmanabdi](https://github.com/lugmanabdi)
- Email: abdiluqmaan552@gmail.com

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Built as part of a comprehensive machine learning portfolio demonstrating end-to-end ML pipeline development, data preprocessing, model optimization, and web application deployment.*
