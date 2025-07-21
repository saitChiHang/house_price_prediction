import streamlit as st
from styles import welcome_msg
def welcome():
    st.header(":wave: Welcome - House Price Prediction", divider='rainbow',anchor=False)
    st.image("images/welcome.jpg", caption="House Price Prediction")
    st.markdown(welcome_msg, unsafe_allow_html=True)
    
   