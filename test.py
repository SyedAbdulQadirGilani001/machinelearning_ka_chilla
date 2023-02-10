import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
st.header("Hello World")
st.text("This is a test")
st.header("This is a test")
df=sns.load_dataset('iris')
st.write(df[['sepal_length','sepal_width']])
st.bar_chart(df[['sepal_length','sepal_width']])
st.line_chart(df[['sepal_length','sepal_width']])