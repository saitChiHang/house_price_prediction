
import streamlit as st
from streamlit_navigation_bar import st_navbar
import contents as pg
from styles import navbar_styles, navbar_options, html_styles
import os

st.set_page_config(
        page_title="House Price Prediction",
        layout="centered",
)

st.html(html_styles)

pages = ["Welcome","Prediction","Exploration", "About"]

page = st_navbar(
    pages,
    styles=navbar_styles,
    options=navbar_options,
    logo_path = os.path.join("images", "sait-logo_horz-white.svg"),
)

functions = {
    "Home":  pg.welcome,
    "Welcome":  pg.welcome,
    "Exploration": pg.exploration,
    "Prediction": pg.prediction,
    "About": pg.about
}

go_to = functions.get(page)

if go_to:
    go_to()