import streamlit as st
import pandas as pd
st.title("Restaurant Growth Potential Analysis")
st.write("This project analyzes restaurant performance using business analytics.")
df = pd.read_csv("data.csv")
st.subheader("Dataset Preview")
st.dataframe(df.head())
st.subheader("Dataset Summary")
st.write(df.describe())
if "GrowthCategory" in df.columns:
    st.subheader("Growth Category Distribution")
    st.bar_chart(df["GrowthCategory"].value_counts())
if "MonthlyOrders" in df.columns:
    st.subheader("Monthly Orders Distribution")
    st.bar_chart(df["MonthlyOrders"])
st.success("Project completed successfully using Streamlit, Python and Business Analytics.")
