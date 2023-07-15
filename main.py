import streamlit as st
import pandas as pd
import numpy as np
import pycelonis
import pm4py
from pycelonis.pql import PQL, PQLColumn, PQLFilter, OrderByColumn
import pandas as pd
import os
import tempfile
import warnings

warnings.filterwarnings("ignore")

def data_integration():
    url_input = st.text_input("Enter your URL:")
    # st.session_state.url_input = url_input
    # if st.button("Display your URL"):
    #     st.write("User URL:", url_input)

    api_input = st.text_input("Enter your api-token:")
    # st.session_state.api_input = api_input
    # if st.button("Display your api-token"):
    #     st.write("User Api-token:", api_input)
    if st.button('Connect with PyCelonis'):
        # create a get_celonis object
        try:
            celonis = pycelonis.get_celonis(base_url=url_input,
                                            api_token=api_input,
                                            key_type='USER_KEY')
            st.write('Connected with celonis successfully.')

        except:

            st.write("Please enter the right url or api-token.")

    else:
        st.write('Connect with celonis by clicking the button. ')

def data_upload():
    st.title("Uploaded File")

    file = st.file_uploader("Upload file")


    if file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file.getvalue())
            temp_file_path = temp_file.name
            if file.name.endswith('.xes'):

                original_data = pm4py.read_xes(temp_file_path)
                st.write(original_data)

            elif file.name.endswith('.csv'):

                original_data = pd.read_csv(temp_file_path)
                st.write(original_data)
            else:
                st.write('Please import IEEE XES files or CSV files. ')



            # Perform file operations using the temporary file path



if __name__ == "__main__":

    pages = ["Data integration", "Dataset upload"]
    choice = st.sidebar.radio("Go to", pages)

    if choice == "Data integration":
        data_integration()
    elif choice == "Dataset upload":
        data_upload()




