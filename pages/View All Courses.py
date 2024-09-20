import streamlit as st
import json
import pandas as pd

filepath = './data/courses-full.json'

with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)
    # df = pd.DataFrame.from_dict(dict_of_courses, orient='index')[['name', 'category', 'provider']]    

    # Create DataFrame with S/N, name, category, and provider
    df = pd.DataFrame.from_dict(dict_of_courses, orient='index')

    # Add Serial Number (S/N)
    df.reset_index(drop=True, inplace=True)
    # df.index += 1
    # df.index.name = 'S/N'

    # st.write(dict_of_courses)
    st.dataframe(df)