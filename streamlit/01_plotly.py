import numpy as np
import pandas as pd   
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
st.markdown('''
# **Exploratory Data Analysis App**
This is an exploratory data analysis app created in Streamlit using the **pandas** and **pandas_profiling** libraries.
''')
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")
with st.sidebar.header('2. Set Parameters'):
    profiling = st.sidebar.radio('Do you want to do Profiling?', ('Yes', 'No'))
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")
@st.cache_data
def load_csv():
    df=pd.DataFrame(np.random.randn(100, 20), columns=('col %d' % i for i in range(20)))
    return df
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        df = pd.read_csv(uploaded_file)
        return df
    df = load_csv()
    st.subheader('**1. Glimpse of dataset**')
    st.write(df)
    if profiling == 'Yes':
        pr = ProfileReport(df, explorative=True)
        st.subheader('**2. Profile Report**')
        st_profile_report(pr)
    else:
        st.subheader('**2. Describe DataFrame**')
        st.write(df.describe())
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example dataframe
        @st.cache_data
        def load_csv():
            a = np.random.randn(1, 20)
            for i in range(1, 100):
                a = np.append(a, np.random.randn(1, 20), axis=0)
            df = pd.DataFrame(a, columns=('col %d' % i for i in range(20)))
            return df
        df = load_csv()
        st.subheader('**1. Glimpse of dataset**')
        st.write(df)
        if profiling == 'Yes':
            pr = ProfileReport(df, explorative=True)
            st.subheader('**2. Profile Report**')
            st_profile_report(pr)
        else:
            st.subheader('**2. Describe DataFrame**')
            st.write(df.describe())
