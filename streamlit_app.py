"""
A simple streamlit calculator app.
"""
import streamlit as st
from funcs import add, sub, mult

st.markdown("""<style>.stApp { background-color: red; }</style>""", unsafe_allow_html=True)

a = st.number_input("a:", value=0)
b = st.number_input("b:", value=0)
operator = st.selectbox("operator:", ["+", "-", "*"])
result = 0

if st.button("Equals"):
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mult(a, b)
    st.write(f"Result: {result}")
