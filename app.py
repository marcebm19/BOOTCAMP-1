a=2
b=3
print(a+b)
##import streamlit as st ## importamos libreria streamlit
##st.write("Hello world") ## imprimimos en pantalla

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib as mp

dataframe = pd.DataFrame(
    np.random.randn(10,20),## creamos valores aleatorios
    columns=('col %d' % i for i in range(20)))
    ##aplicamos estilo "highlight"a Dataframe
st.dataframe(dataframe.style.highlight_max(axis=0))##resaltar valores máximos por columna