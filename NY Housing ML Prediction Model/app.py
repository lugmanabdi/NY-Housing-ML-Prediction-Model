import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model.pkl")

st.title("NY House Price Prediction App")

st.divider()

st.write("This app predicts the price of a house based on its features using machine learning. For using this app you can enter the inputs from this user interface and use the 'Predict' button to get the predicted price.")

st.divider()

bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=2)
sqft = st.number_input("Property Square Feet", min_value=200, value=1000)
property_type = st.selectbox("Property Type", 
                           ["House for sale", "Condo for sale", "Co-op for sale", 
                            "Townhouse for sale", "Multi-family home for sale"])

locality = st.selectbox("Borough/Area", 
                      ["New York", "New York County", "Queens County", "Kings County",
                       "Brooklyn", "Queens", "The Bronx", "Richmond County", 
                       "United States", "Flatbush"])

sublocality = st.selectbox("Neighborhood", 
                         ["New York", "Manhattan", "Brooklyn", "Queens", "Kings County",
                          "Queens County", "New York County", "The Bronx", "Staten Island",
                          "Richmond County", "Brooklyn Heights", "Coney Island", "Dumbo",
                          "East Bronx", "Flushing", "Fort Hamilton", "Jackson Heights",
                          "Rego Park", "Riverdale", "Snyder Avenue"])

st.divider()

predictbutton = st.button("Predict")

if predictbutton:
    # Create DataFrame
    input_df = pd.DataFrame({
        'BEDS': [bedrooms],
        'BATH': [bathrooms], 
        'PROPERTYSQFT': [sqft],
        'TYPE': [property_type],
        'LOCALITY': [locality],
        'SUBLOCALITY': [sublocality]
    })
    
    # Apply get_dummies
    input_encoded = pd.get_dummies(input_df, drop_first=True)
    
    # Expected features
    expected_features = [
        'BEDS', 'BATH', 'PROPERTYSQFT',
        'TYPE_Condo for sale', 'TYPE_Condop for sale', 'TYPE_Contingent',
        'TYPE_For sale', 'TYPE_Foreclosure', 'TYPE_House for sale',
        'TYPE_Land for sale', 'TYPE_Mobile house for sale', 'TYPE_Multi-family home for sale',
        'TYPE_Townhouse for sale', 'LOCALITY_Brooklyn', 'LOCALITY_Flatbush',
        'LOCALITY_Kings County', 'LOCALITY_New York', 'LOCALITY_New York County',
        'LOCALITY_Queens', 'LOCALITY_Queens County', 'LOCALITY_Richmond County',
        'LOCALITY_The Bronx', 'LOCALITY_United States', 'SUBLOCALITY_Brooklyn',
        'SUBLOCALITY_Brooklyn Heights', 'SUBLOCALITY_Coney Island', 'SUBLOCALITY_Dumbo',
        'SUBLOCALITY_East Bronx', 'SUBLOCALITY_Flushing', 'SUBLOCALITY_Fort Hamilton',
        'SUBLOCALITY_Jackson Heights', 'SUBLOCALITY_Kings County', 'SUBLOCALITY_Manhattan',
        'SUBLOCALITY_New York', 'SUBLOCALITY_New York County', 'SUBLOCALITY_Queens',
        'SUBLOCALITY_Queens County', 'SUBLOCALITY_Rego Park', 'SUBLOCALITY_Richmond County',
        'SUBLOCALITY_Riverdale', 'SUBLOCALITY_Snyder Avenue', 'SUBLOCALITY_Staten Island',
        'SUBLOCALITY_The Bronx'
    ]
    
    # Add missing columns
    for feature in expected_features:
        if feature not in input_encoded.columns:
            input_encoded[feature] = 0
    
    # Reorder columns
    input_encoded = input_encoded.reindex(columns=expected_features, fill_value=0)
    
    # Make prediction
    prediction = model.predict(input_encoded)
    st.write(f"The predicted price of the house is: ${prediction[0]:,.2f}")

else:
    st.write("Please click the 'Predict' button to get the predicted price.")
