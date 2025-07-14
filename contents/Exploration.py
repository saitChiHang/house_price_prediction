import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
from styles import vis_spec

@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv("data/Housing.csv")
    return StreamlitRenderer(df,appearance="dark", spec = vis_spec)

def exploration():
    st.header("Data Exploration", divider='rainbow', anchor=False)
    renderer = get_pyg_renderer()
    renderer.explorer()