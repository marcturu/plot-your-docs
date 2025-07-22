import streamlit as st
import duckdb
import plotly.express as px
import plotly.graph_objects as go
import random
from utils import clean_currency

def plot_metric(label, value, prefix="", suffix="", show_graph=False, color_graph=""):
    fig = go.Figure()
    fig.add_trace(
        go.Indicator(
            value=value,
            gauge={"axis": {"visible": False}},
            number={"prefix": prefix, "suffix": suffix, "font.size": 28},
            title={"text": label, "font": {"size": 24}},
        )
    )
    if show_graph:
        fig.add_trace(
            go.Scatter(
                y=random.sample(range(0, 101), 30),
                hoverinfo="skip",
                fill="tozeroy",
                fillcolor=color_graph,
                line={"color": color_graph},
            )
        )
    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    fig.update_layout(margin=dict(t=30, b=0), showlegend=False, plot_bgcolor="white", height=100)
    st.plotly_chart(fig, use_container_width=True)

def plot_gauge(indicator_number, indicator_color, indicator_suffix, indicator_title, max_bound):
    fig = go.Figure(
        go.Indicator(
            value=indicator_number,
            mode="gauge+number",
            domain={"x": [0, 1], "y": [0, 1]},
            number={"suffix": indicator_suffix, "font.size": 26},
            gauge={"axis": {"range": [0, max_bound], "tickwidth": 1}, "bar": {"color": indicator_color}},
            title={"text": indicator_title, "font": {"size": 28}},
        )
    )
    fig.update_layout(height=200, margin=dict(l=10, r=10, t=50, b=10, pad=8))
    st.plotly_chart(fig, use_container_width=True)

def render(df):

    all_months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    for m in all_months:
        if m in df.columns:
            df[m] = df[m].apply(clean_currency)

    con = duckdb.connect()
    con.register("df", df)

    top_left_col, top_right_col = st.columns((2, 1))
    bottom_left_col, bottom_right_col = st.columns(2)

    with top_left_col:
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            plot_metric("Total Accounts Receivable", 6621280, prefix="$", show_graph=True, color_graph="rgba(0, 104, 201, 0.2)")
            plot_gauge(1.86, "#0068C9", "%", "Current Ratio", 3)
        with c2:
            plot_metric("Total Accounts Payable", 1630270, prefix="$", show_graph=True, color_graph="rgba(255, 43, 43, 0.2)")
            plot_gauge(10, "#FF8700", " days", "In Stock", 31)
        with c3:
            plot_metric("Equity Ratio", 75.38, suffix=" %")
            plot_gauge(7, "#FF2B2B", " days", "Out Stock", 31)
        with c4:
            plot_metric("Debt Equity", 1.10, suffix=" %")
            plot_gauge(28, "#29B09D", " days", "Delay", 31)

    with top_right_col:
        query = f"""
            WITH sales_data AS (
                UNPIVOT (
                    SELECT Scenario, business_unit, {','.join(all_months)}
                    FROM df
                    WHERE Year=2023 AND Account='Sales'
                )
                ON {','.join(all_months)}
                INTO NAME month VALUE sales
            )
            SELECT Scenario, business_unit, SUM(sales) AS sales
            FROM sales_data
            GROUP BY Scenario, business_unit
            ORDER BY sales DESC
        """
        sales_summary = con.execute(query).df()
        fig = px.bar(sales_summary, x="business_unit", y="sales", color="Scenario", barmode="group", title="Sales for Year 2023", height=400)
        st.plotly_chart(fig, use_container_width=True)

    with bottom_left_col:
        query = f"""
            WITH sales_data AS (
                SELECT Scenario, {','.join(all_months)}
                FROM df
                WHERE Year=2023 AND Account='Sales' AND business_unit='Software'
            )
            UNPIVOT sales_data
            ON {','.join(all_months)}
            INTO NAME month VALUE sales
        """
        sales_data = con.execute(query).df()
        fig = px.line(sales_data, x="month", y="sales", color="Scenario", markers=True, title="Monthly Budget vs Forecast 2023")
        st.plotly_chart(fig, use_container_width=True)

    with bottom_right_col:
        query = f"""
            WITH sales_data AS (
                UNPIVOT (
                    SELECT Account, Year, {','.join([f'ABS({m}) AS {m}' for m in all_months])}
                    FROM df
                    WHERE Scenario='Actuals' AND Account!='Sales'
                )
                ON {','.join(all_months)}
                INTO NAME year VALUE sales
            )
            SELECT Account, Year, SUM(sales) AS sales
            FROM sales_data
            GROUP BY Account, Year
        """
        sales_summary = con.execute(query).df()
        fig = px.bar(sales_summary, x="Year", y="sales", color="Account", title="Actual Yearly Sales Per Account")
        st.plotly_chart(fig, use_container_width=True)