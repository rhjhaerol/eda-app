import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# web title
st.markdown('''
# **Exploratory Data Analysis App**
''')

# upload cvs data
with st.sidebar.header('Upload CSV data'):
    uploaded_file = st.sidebar.file_uploader('Upload your input csv file', type=["csv"])

if uploaded_file is not None:
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    
    df = load_csv()
    pr = ProfileReport(df, explorative=True)

    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
