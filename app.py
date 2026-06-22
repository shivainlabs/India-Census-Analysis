import streamlit as st 
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("india.csv")

list_of_states = list(df['State'].unique())
list_of_states.insert(0,"Overall India")

st.sidebar.title("India's Data Viz")
select_state = st.sidebar.selectbox("Select a state",list_of_states)


primary = st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size represent Primary Parameter")
    st.text("Color represent Secondary Parameter")
    
    if select_state == "Overall India":
        # plot for india
        px.scatter_map(df,lat="Latitude",lon="Longitude")
        fig = px.scatter_map(df,lat="Latitude",lon="Longitude",zoom=4,size=primary,color=secondary,size_max=35,width=1200,height=700,hover_name="District")
        st.plotly_chart(fig,use_container_width=True)
        
    else:
        # plot for state
        state_df = df[df['State'] == select_state]
        px.scatter_map(state_df,lat="Latitude",lon="Longitude")
        fig = px.scatter_map(state_df,lat="Latitude",lon="Longitude",zoom=4,size=primary,color=secondary,size_max=35,width=1200,height=700,hover_name="District")
        st.plotly_chart(fig,use_container_width=True)