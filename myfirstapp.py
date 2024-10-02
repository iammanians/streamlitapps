import pandas as pd
import streamlit as st
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
import os

st.title("DQ Profiler")

if 'clicked' not in st.session_state:
    st.session_state.clicked=True

uploaded_file = st.file_uploader("Choose a file")
if st.session_state.clicked:
    if uploaded_file is not None:
        input_file = pd.read_csv(uploaded_file)
        input_filename = uploaded_file.name
        if not ".csv" in input_filename:
            st.write("Invalid input file. Select only CSV file")
        st.write("File uploaded Successfully")

def gen_report():
    pr = input_file.profile_report()
    st.title("Profiling in Streamlit")
    st.write(input_file)
    st_profile_report(pr)

if 'Profile_Data' not in st.session_state:
    st.session_state.Profile_Data = False

def set_Profile_Data():
    st.session_state.Profile_Data = True

if st.button("Profile_Data"):
    st.write("Calling function with filename: ", input_filename)
    gen_report()

if st.buttong("Clear"):
    st.write("Clearing off Screen")
    input_file=[]
    st.rerun()

