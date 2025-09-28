import streamlit as st
from funcs import *


a = st.number_input("a:", value=0)
b = st.number_input("b:", value=0)
operator = st.selectbox("operator:", ["+", "-", "*"])

if st.button("Equals"):
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mult(a, b)
    st.write(f"Result: {result}")