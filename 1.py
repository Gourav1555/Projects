import streamlit as st
import pandas as pd1
import plotly.express as px1
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')
  
#Page configuration
st.set_page_config(page_title= "Automation Department", page_icon= ":bar_chart:", layout= "wide")

st.title(" :bar_chart: Automation Department")
st.write(""" # FY - 2024-2025 """)


# Get current date and time
current_datetime = datetime.now()

# Display date and time on Streamlit web page
st.write("Current date and time:", current_datetime)

#Reading Excel Sheet
dataset = pd1.read_excel('e:/python/project status/project plan.xlsx')


st.sidebar.header('Filter By:-')

category=st.sidebar.multiselect('Filter by category:-',
options=dataset["Status"].unique(),
default=dataset["Status"].unique())

selection_query=dataset.query(
    "Status==@category"
)
st.dataframe(selection_query)











