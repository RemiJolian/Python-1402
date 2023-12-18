import streamlit as st
import pandas as pd
import numpy as np

st.write(' Hi! The test message: Hello World')
x = st.text_input('Input your favorite movie')
st.write(f'your favorite movie is: {x}')
is_clicked = st.button('Click Me')

data = pd.read_csv('vgsales.csv')
st.write(data)
# ---------------------------------------------- #

st.write('mycoll graph')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"] 
)

st.bar_chart(chart_data)
st.line_chart(chart_data)