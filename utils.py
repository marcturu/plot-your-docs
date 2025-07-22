import pandas as pd
import streamlit as st

@st.cache_data
def load_data(uploaded_file):
    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file)

def clean_currency(val):
    if pd.isna(val):
        return 0
    val = str(val).replace('$', '').replace('.', '').replace(',', '').replace('(', '-').replace(')', '').strip()
    try:
        return float(val)
    except:
        return 0
