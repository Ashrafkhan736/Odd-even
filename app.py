import streamlit as st

st.write("""
# Even - Odd Calculator

This app tell whether given number is odd or not. 
""")

#Take Input from user
st.header('User Input')

def user_input():
    num = st.number_input("Enter an integer",min_value=float("-inf"),max_value=float("inf"),step=1)

    return num

num = user_input()

st.subheader('User Input Number')
st.write(num)

#prepocessing
def odd_even(num):
    if num % 2 ==0:
        return f"{num} is even number."
    return f"{num} is odd number."

st.write(odd_even(num))