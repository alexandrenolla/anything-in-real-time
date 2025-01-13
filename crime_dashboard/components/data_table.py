import streamlit as st

def render_data_table(filtered_data):
    st.header("Raw Data")
    st.dataframe(filtered_data)

