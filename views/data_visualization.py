import streamlit as st

def render(df):
    st.write("Data preview:")
    st.dataframe(df)
    st.write("Descriptive statistics:")
    st.write(df.describe())