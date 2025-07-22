import streamlit as st

def render():
    st.set_page_config(
        page_title="Plot your Docs!",
        page_icon="📊",
        layout="wide",
    )

    st.title("📊 Plot your Docs")
    st.write("Welcome to the ultimate app for importing files, analyzing data, and visualizing statistics!")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### What can you do here?
        - **Import your data files** (CSV, Excel) easily using the sidebar.
        - **Explore data summaries** and statistics with **Streamlit**.
        - **Visualize data** interactively using multiple types of plots with **Plotly**.
        - **Download processed data** or plots for your reports.
        
        ### How to get started:
        1. Use the **sidebar** to upload your file.
        2. Navigate through the tabs to explore data statistics and plots.
        3. Export your results if needed.
        """)
        st.info("💡 Tip: The **Dashboard** section offers more extensive results depending on the content of the imported file.")

    with col2:
        st.image(
            "https://images.pexels.com/photos/669610/pexels-photo-669610.jpeg?_gl=1*dtk7hn*_ga*MTk0Njg4NTIxMC4xNzMxMzIwODkx*_ga_8JE65Q40S6*czE3NTMxOTg5MDAkbzIkZzEkdDE3NTMxOTkwMDQkajU3JGwwJGgw",
        )

    st.markdown("---")

    st.subheader("Why choose this app?")
    st.markdown("""
    - 🚀 **Fast and easy:** Upload and analyze data in seconds.
    - 📈 **Interactive visualizations:** Customize plots on the fly.
    - 🔄 **Seamless integration:** Works smoothly with Pandas dataframes.
    - 📥 **Export options:** Save your analysis and charts locally.
    """)

    st.markdown("---")

