from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit_option_menu as menu
import os
import plotly.express as px


st.set_page_config(layout="wide")



with st.sidebar:
    selected = menu.option_menu("Streamlit demo", ["Inicio","Analisis datos Austin Trips"], 
        icons=['house', 'person-rolodex'], menu_icon="cast", default_index=0)
    selected

if selected == "Inicio":
    st.title("Shiny app demo para ejecutarse en contenedor")

    c=st.empty()
    c.image("docker_1.png")

if selected == "Analisis datos Austin Trips":
    
            
       
    if st.button("Carga"):
        df = pd.read_csv('trips_austin.csv')
        col1, col2 = st.columns(2)
        col1.text("Datos del sistema de bicicletas de la ciudad de Austin")
        col1.dataframe(df.head(10))

        grouped_data = df.groupby('trip_id')['duration_minutes'].sum().reset_index()
        grouped_data = grouped_data.sort_values(by='duration_minutes', ascending=False)
        fig = px.bar(grouped_data, x='trip_id', y='duration_minutes')
        col2.text("Grafico de la duracion de minutos de los viajes del sistema de bicicleta")
        col2.plotly_chart(fig)    

        with st.container():
        
            porcentajes = grouped_data['duration_minutes']/grouped_data['duration_minutes'].sum()*100
            grouped_data['percentage'] = porcentajes
            fig_pie = px.pie(grouped_data, names='trip_id', values='percentage', title='Gráfico de Torta')
            st.text("Grafico de la duracion de minutos de los viajes del sistema de bicicleta")
            st.plotly_chart(fig_pie) 