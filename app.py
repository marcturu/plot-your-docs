import streamlit as sl 
import pandas as pd 
import plotly.express as px

def main_page():
    sl.title("Main Page")
    sl.write("Welcome!")
    sl.write("Use the sidebar to navigate through the app")

def data_visualization():
    sl.title("Data Visualisation")
    loaded_file = sl.file_uploader("Load a CSV file to visualize the data", type="csv")

    if loaded_file is not None:
        df = pd.read_csv(loaded_file)
        sl.write("File data:")
        sl.write(df)
        sl.write("Descriptive stats:")
        sl.write(df.describe())

def plot_representation():
    sl.title("Plot Representation")
    loaded_file = sl.file_uploader("Load a CSV file to see its plot", type="csv", key="2")

    if loaded_file is not None:
        df = pd.read_csv(loaded_file)
        x_axis = sl.selectbox("Choose a column for the X axis:", df.columns)
        y_axis = sl.selectbox("Choose a column for the Y axis:", df.columns)

        if sl.button("Create plot"):
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} for {x_axis}")
            sl.plotly_chart(fig)

sl.sidebar.title("Sidebar")
page = sl.sidebar.selectbox("", ["Main Page", "Data Visualization", "Plot Representation"])

if page == "Main Page":
    main_page()
elif page == "Data Visualization":
    data_visualization()
elif page == "Plot Representation":
    plot_representation()