import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Proyecto Final Sprint 7 TT')
st.markdown('**Esta es la aplicación desarrollada en este proyecto final, '
            'donde se trabaja con datos de anuncios de venta de coches durante el 2018 y 2019.**')

st.subheader("Base de Datos")
st.dataframe(car_data)

st.write(' ')
st.subheader("Grafica de linea")

car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])
year = car_data['date_posted'].value_counts().sort_index().reset_index()
fig = px.line(year, x='date_posted', y='count',
              title='Número de anuncios al día')
st.plotly_chart(fig, use_container_width=True)

st.subheader("Gráficos")
st.write(' ')
st.markdown('**Grafica de barras**')
bar_button = st.button('Crear gráfica de barras')
if bar_button:
    st.write('Puedara seleccionar algun tipo de combustible en especifico, '
             'da click en los demás para quitarlos del gráfico y solo deja el de tu interes')
    table = car_data.pivot_table(index='condition',
                                 columns='fuel',
                                 values='model',
                                 aggfunc='count')
    fig = px.bar(table, x=table.index, y=table.columns, color="fuel",
                 title="Clasificación de carros según condición y tipo de combustible")
    st.plotly_chart(fig, use_container_width=True)

st.write(' ')
st.markdown('**Grafica de pastel**')
pie_toggle = st.toggle('Grafica interactiva')
if pie_toggle:
    condition = car_data['condition'].value_counts().reset_index()
    fig = px.pie(condition, values='count', names='condition',
                 title='Condición de los carros')
    st.plotly_chart(fig, use_container_width=True)

st.write(' ')
st.markdown('**Bubble Chart**')
bubble_box = st.checkbox('Relación entre precio y dias de publicación')
if bubble_box:
    fig = px.scatter(car_data, x="days_listed", y="price",
                     size="price", color="type",
                     hover_name="model", log_x=True, size_max=60)
    st.plotly_chart(fig, use_container_width=True)
