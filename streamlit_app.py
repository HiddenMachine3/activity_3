"""
A simple streamlit calculator app.
"""
import streamlit as st
from funcs import add, sub, mult


st.title("Calculator App")
a = st.number_input("a:", value=0)
b = st.number_input("b:", value=0)
operator = st.selectbox("operator:", ["+", "-", "*"])


if st.button("Equals"):
    RESULT = 0
    if operator == "+":
        RESULT = add(a, b)
    elif operator == "-":
        RESULT = sub(a, b)
    elif operator == "*":
        RESULT = mult(a, b)
    st.write(f"Result: {RESULT}")
