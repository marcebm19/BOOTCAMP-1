import streamlit as st
x = st.slider('x') # esto es un widget
st.write(x,'squared is',x * x)