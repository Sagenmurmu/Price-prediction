import os
import pandas as pd
import pickle as pk
import streamlit as st

#Get current directory (works on Render, Windows, or anywhere)
current_dir = os.path.dirname(__file__)

#Use relative paths (no more C:\... errors)
model_path = os.path.join(current_dir, 'House_prediction_model.pkl')
data_path = os.path.join(current_dir, 'Cleaned_data.csv')

#Load model and data safely
with open(model_path, 'rb') as file:
    model = pk.load(file)

data = pd.read_csv(data_path)

#Streamlit UI
st.header('Bangalore House Price Prediction')

loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter Total Sqft')
beds = st.number_input('Enter Number of Bedrooms')
bath = st.number_input('Enter Number of Bathrooms')
balc = st.number_input('Enter Number of Balconies')

#Prepare input for model
input_df = pd.DataFrame([[loc, sqft, bath, balc, beds]],
                        columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])

# Predict button
if st.button('Predict Price'):
    output = model.predict(input_df)
    out_str = f'Price of the House is ₹{output[0] * 100000:,.2f}'
    st.success(out_str)
