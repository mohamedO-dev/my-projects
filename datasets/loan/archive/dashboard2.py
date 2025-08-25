import streamlit as st

st.write("This is the second dashboard page.")

st.sidebar.subheader("Models")
models=["Model A", "Model B", "Model C"]
st.sidebar.selectbox(
    "Model Selection",
    options=models)