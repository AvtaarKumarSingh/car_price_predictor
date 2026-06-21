import pandas as pd
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl', 'rb'))

data = pd.read_csv('Cardetails.csv')

data['name'] = data['name'].apply(lambda x: x.split()[0])

st.title("Car Price Predictor")

name = st.selectbox("Car Brand", data['name'].unique())
year = st.slider("Manufacturing Year", 1994, 2024)
km_driven = st.number_input("Kilometers Driven", min_value=0)
fuel = st.selectbox("Fuel Type", data['fuel'].unique())
seller_type = st.selectbox("Seller Type", data['seller_type'].unique())
transmission = st.selectbox("Transmission", data['transmission'].unique())
owner = st.selectbox("Owner", data['owner'].unique())
mileage = st.number_input("Mileage")
engine = st.number_input("Engine CC")
max_power = st.number_input("Max Power")
seats = st.number_input("Seats", min_value=2)

if st.button("Predict Price"):

    input_df = pd.DataFrame(
        [[name, year, km_driven, fuel, seller_type,
          transmission, owner, mileage,
          engine, max_power, seats]],
        columns=[
            'name', 'year', 'km_driven', 'fuel',
            'seller_type', 'transmission', 'owner',
            'mileage', 'engine', 'max_power', 'seats'
        ]
    )

    prediction = model.predict(input_df)[0]

    st.success(
        f"Estimated Car Price: ₹ {prediction:,.0f}"
    )