import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open("regression.pkl", "rb")
regression = pickle.load(pickle_in)


def predict(Year, Present_Price, Kms_Driven, Fuel_type):
    prediction = regression.predict([[Year, Present_Price, Kms_Driven, Fuel_type]])
    print(prediction)
    output = "Rs. " + str(prediction[0]) + " Lakhs"
    return output


def main():
    #####################################
    st.title("Car Price Prediction problem")
    #######################################

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Car Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Year = st.text_input("Year")
    Present_Price = st.text_input("Present_Price")
    Kms_Driven = st.text_input("Kms_Driven")
    Fuel_type = st.text_input("Fuel_Type")

    result = ""
    if st.button("Predict"):
        result = predict(
            int(Year), float(Present_Price), int(Kms_Driven), int(Fuel_type)
        )
    st.success("Car Selling price will be {}".format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == "__main__":
    main()
