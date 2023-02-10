import streamlit as st
import seaborn as sns
import pandas as pd
header=st.beta_container()
datasets=st.beta_container()
features=st.beta_container()
model_training=st.beta_container()
with header:
    st.title('Machine Learning App')
    st.text('This is a machine learning app')
with datasets:
    st.header('Datasets')
    st.text('This is a datasets')
    df=sns.load_dataset('titanic')
    st.write(df.head())
    st.write(df.shape)
    st.bar_chart(df['class'].value_counts())
    st.subheader('Data Types')
    st.bar_chart(df.dtypes.value_counts())
with features:
    st.header('Features')
    st.text('This is a features')
with model_training:
    st.header('Model Training')
    st.text('This is a model training')
