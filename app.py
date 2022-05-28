import altair as alt
import datetime
import folium
import geopandas as gpd
import geopy
import json
import base64
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import osmnx as ox
import pandas as pd
import plotly_express as px
import plotly.io as pio
import plotly.offline as pyo
import requests
import seaborn as sns
import streamlit as st
import psycopg2

from folium.features import DivIcon
from googletrans import Translator
from PIL import Image
from shapely.geometry import Point, LineString
from spacy import displacy
from spacy_streamlit import visualize_ner
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

from branca.element import Figure
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

ox.config(use_cache=True, log_console=True)
pyo.init_notebook_mode(connected=True)

st.set_page_config(
    page_title="Automatic River Encroachment Detection - Bangladesh",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown(
    """
    <style>
        .css-hby737, .css-17eq0hr, .css-qbe2hs {
            background-color:    #154360    !important;
            color: black !important;
        }
        div[role="radiogroup"] {
            color:black !important;
            margin-left:8%;
        }
        div[data-baseweb="select"] > div {
            
            color: black;
        }
        div[data-baseweb="base-input"] > div {
            background-color: #aab7b8 !important;
            color: black;
        }
        
        .st-cb, .st-bq, .st-aj, .st-c0{
            color: black !important;
        }
        .st-bs, .st-ez, .st-eq, .st-ep, .st-bd, .st-e2, .st-ea, .st-g9, .st-g8, .st-dh, .st-c0 {
            color: black !important;
        }
        .st-fg, .st-fi {
            background-color: #c6703b !important;
            color: black !important;
        }
       
        
        .st-g0 {
            border-bottom-color: #c6703b !important;
        }
        .st-fz {
            border-top-color: #c6703b !important;
        }
        .st-fy {
            border-right-color: #c6703b !important;
        }
        .st-fx {
            border-left-color: #c6703b !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown('<h1 style="margin-left:8%; color:#FA8072">Automatic River Encroachment Detection - Bangladesh</h1>', unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "",
    ("Home", "About", "Features", "River Encroachment Detection", "Visualizations", "Conclusion", "Team")
)

if add_selectbox == 'Home':
    
    LOGO_IMAGE = "omdena_bangladesh_logo.png"
    
    st.markdown(
          """
          <style>
          .container {
          display: flex;
        }
        .logo-text {
             font-weight:700 !important;
             font-size:50px !important;
             color: #f9a01b !important;
             padding-top: 75px !important;
        }
        .logo-img {
             float:right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
          f"""
          <div class="container">
               <img class="logo-img" src="data:image/jpg;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
          </div>
          """,
          unsafe_allow_html=True
    )
    
    st.subheader('PROBLEM STATEMENT')
    
    st.markdown('River encroachment is a threatening problem that has been going on for a few years now. Bangladesh Govt. has been relentlessly working to free rivers \ 
    from encroachment after ensuring their navigability by dredging them round the year. BIWTA has removed a total of 18,025 illegal structures from riverbanks between \ 
    2010 and 2019 and reclaimed 738 acres of riverbanks from encroachments in Dhaka and Narayanganj river port areas. The National River Conservation Commission says 50 \ 
    percent of the rivers have been freed from the clutch of grabbers, but the rate is only 7 percent in Barishal, the lawyer said. Bangladesh has around 800 rivers. The \
    State Minister recently said over 65,000 grabbers have encroached on the rivers.', unsafe_allow_html=True)


elif add_selectbox == 'About':
    
    st.subheader('ABOUT THE PROJECT')

    st.markdown('<h4>Project Goals</h4>', unsafe_allow_html=True)
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    
    st.markdown('<h4>Location Choosen</h4>', unsafe_allow_html=True)
    st.markdown('We had choosen "Keraniganj", "Kamrangirchar" and "Bosilsaa" as our regions of interest, which is onto the river banks of "Buriganga" river. Its located in the city premises of Dhaka',
                unsafe_allow_html=True)
    
    st.markdown('<h4>Developments Made</h4>', unsafe_allow_html=True)
    st.markdown('• ',
                unsafe_allow_html=True)
    st.markdown('• '
                , unsafe_allow_html=True)
  

elif add_selectbox == 'Features':

    st.subheader('PROJECT ENDORSEMENTS')

    st.markdown('• ', unsafe_allow_html=True)
    st.markdown('• ', unsafe_allow_html=True)
    st.markdown('• ', unsafe_allow_html=True)
    	
	
elif add_selectbox == 'River Encroachment Detection':
	
    st.subheader('FIND THE ENCROACHMENT SPOTS')

	
elif add_selectbox == 'Visualizations':
    
    st.subheader('PROJECT VISUALIZATIONS')
    st.markdown('<h4>Topic1</h4>', unsafe_allow_html=True)
    st.image("Topic1.png", width=500)
    st.markdown('<h4>Topic2</h4>', unsafe_allow_html=True)
    st.image("Topic2.png", width=500)
    st.markdown('<h4>Topic3</h4>', unsafe_allow_html=True)
    st.image("Topic3.jpg", width=500)
    st.markdown('<h4>Topic4</h4>', unsafe_allow_html=True)
    st.image("Topic4.jpg", width=500)
 

elif add_selectbox == 'Conclusion':
    
    st.subheader('TECH STACK')

    st.markdown('• Data Collection - ', unsafe_allow_html=True)
    st.markdown('• Data Preprocessing - ', unsafe_allow_html=True)
    st.markdown('• Exploratory Data Analysis & Visualizations - ', unsafe_allow_html=True) 
    st.markdown('• Machine Learning - Python, Jupyter Notebook ()', unsafe_allow_html=True) 
    st.markdown('• Dashboard - Streamlit', unsafe_allow_html=True) 
    
    st.subheader('PROJECT SUMMARY')

    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    st.markdown('• ', unsafe_allow_html=True) 
    
    st.subheader('CONCLUSION')
    
    st.markdown('', unsafe_allow_html=True)

	
elif add_selectbox == 'Team':
    
    st.subheader('COLLABORATORS')
	
    st.markdown('<a href="https://www.linkedin.com/in//">Ricard Borras</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/prathima-kadari/">Prathima Kadari</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in//">Vaishnavi Kanagasabapathi</a>',
                unsafe_allow_html=True)

    st.subheader('PROJECT MANAGER')

    st.markdown('<a href="https://www.linkedin.com/in/galina-naydenova-msc-fhea-b89856196/">Shawon Kazi</a>', unsafe_allow_html=True)
