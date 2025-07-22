import streamlit as st
import plotly.express as px

def render(df):
    st.title("Plot Representation")
    x_axis = st.selectbox("Choose X axis", df.columns)
    y_axis = st.selectbox("Choose Y axis", df.columns)
    if st.button("Create plot"):
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} for {x_axis}")
        st.plotly_chart(fig)