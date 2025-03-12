import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
    np.random.randn(20,4), ##genero valores aleatorios
    columns =['a','b','c','d']) ##genero las columnas
st.write(chart_data)
st.line_chart(chart_data)    
