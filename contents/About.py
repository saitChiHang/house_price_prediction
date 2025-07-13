import streamlit as st
import pandas as pd
import numpy as np
from streamlit_navigation_bar import st_navbar
from styles import developers, fontawesome_css, developer_name_markdown, developer_introduction_markdown, developer_portfolio_markdown, developer_linkedin_markdown

def about():
    st.header("About Us", divider='rainbow',anchor=False)
    st.write(fontawesome_css, unsafe_allow_html=True)
    for developer in developers:
        with st.container(border=True):
            name_col, portfolio_col, linkedin_col = st.columns([2, 1, 1])
            name_col.markdown(developer_name_markdown(developer['name']), unsafe_allow_html=True)
            portfolio_col.markdown(developer_portfolio_markdown(developer['portfolio']), unsafe_allow_html=True)
            linkedin_col.markdown(developer_linkedin_markdown(developer['linkedin']), unsafe_allow_html=True)
            st.write(developer_introduction_markdown(developer['Introduction']), unsafe_allow_html=True)