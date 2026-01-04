import streamlit as st

def factorial(n):
    n = int(n)
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

st.title("Factorial Calculator")

number = st.number_input(
    "Enter a number to calculate its factorial:",
    min_value=0,
    max_value=100,
    step=1
)

if st.button("Calculate"):
    st.write(f"The factorial of {int(number)} is {factorial(number)}")
