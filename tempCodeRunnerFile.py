import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('C:\Users\VICTUS\OneDrive\Documents\House_price_prediction\House_prediction_model.pkl','rb'))

st.header('Bangalore House Price Prediction')
data = pd.read_csv('C:\Users\VICTUS\OneDrive\Documents\House_price_prediction\Cleaned_data.csv')

loc = st.selectbox('Choose the location', data['location'].unique())
sqft = st.number_input('Enter Total Sqft')
beds = st.number_input('Enter Number of Bedrooms')
bath = st.number_input('Enter Number of Bathrooms')
balc = st.number_input('Enter Number of Balconies')


input = pd.DataFrame([['loc',sqft,bath,balc,beds]],columns=['location','total_sqft','bath','balcony','bedrooms'])

if st.button('Predict Price'):
    output = model.predict(input)
    out_str = 'Price of the House is ' + str(output[0]*100000)