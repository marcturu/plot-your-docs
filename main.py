import streamlit as st
from utils import load_data
from views import main_page, data_visualization, plot_representation, dashboard

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# Sidebar con navegación
page = st.sidebar.selectbox("Select a page", ["Main Page", "Data Visualization", "Plot Representation", "Dashboard"])

# Control de flujo según la página
uploaded_file = None
if page in ["Data Visualization", "Plot Representation", "Dashboard"]:
    uploaded_file = st.sidebar.file_uploader("Upload Excel or CSV file", type=["csv", "xlsx"])

if page == "Main Page":
    main_page.render()
elif page == "Data Visualization":
    st.title("Data Visualization") 
    if uploaded_file:
        df = load_data(uploaded_file)
        data_visualization.render(df)
    else:
        st.info("Please upload a file to continue.")
elif page == "Plot Representation":
    st.title("Plot Representation")  
    if uploaded_file:
        df = load_data(uploaded_file)
        plot_representation.render(df)
    else:
        st.info("Please upload a file to continue.")
elif page == "Dashboard":
    st.title("Sales Dashboard")  
    if uploaded_file:
        df = load_data(uploaded_file)
        dashboard.render(df)
    else:
        st.info("Please upload a file to continue.")
        st.warning("⚠️ Remember: the file must follow the expected financial structure, including columns like 'Year', 'Account', and 'Scenario'.")
