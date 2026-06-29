import streamlit as st
import pandas as pd
df = pd.read_csv("data/raw/sales_data.csv")
st.title("Sales Dashboard")
st.line_chart(df.groupby("date")["sales"].sum())
