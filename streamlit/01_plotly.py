import streamlit as st
import plotly.express as px
import pandas as pd
st.title('Plotly Example')
df=px.data.gapminder()
st.write(df.head()) 
st.write(df.columns)
st.write(df.describe())
year_options=df['year'].unique().tolist()
year=st.selectbox('Select Year',year_options,0)
df=df[df['year']==year]
fig=px.scatter(df,x='gdpPercap',y='lifeExp',size='pop',color='continent',hover_name='country',log_x=True,size_max=60)
fig.update_layout(title='Life Expectancy vs GDP Per Capita',width=800,height=500)
st.write(fig)