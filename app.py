import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Title of the app centrado
st.title('Listados de anuncios de vehículos de EE. UU.')

# lectura vehicles.csv
df = pd.read_csv('vehicles_us.csv')

# Extraer la marca desde la columna 'model'
df['manufacturer'] = df['model'].str.split().str[0]

# mostrar datos 
st.write(df.head())

# Histograma de los tipos de vehículos por fabricante
st.subheader('Histograma de los tipos de vehículos por fabricante')
fig = px.histogram(df, x='fabricante', color='type', title="tipos de vehículos por fabricante")
st.plotly_chart(fig)

# Histograma de distribución de precios entre fabricantes
st.subheader('Histograma de distribución de precios entre fabricantes')
# Menús desplegables para seleccionar dos fabricantes
manufacturer_list = df['manufacturer'].dropna().unique()
manufacturer1 = st.selectbox('Manufacturer 1', manufacturer_list, index=0)
manufacturer2 = st.selectbox('Manufacturer 2', manufacturer_list, index=1)

# Casilla de verificación para normalización
normalized = st.checkbox('Normalized')

# Crear histograma
fig = go.Figure()
histnorm_value = 'percent' if normalized else None
fig.add_trace(go.Histogram(
    x=df[df['fabricante'] == manufacturer1]['precio'],
    name=manufacturer1,
    opacity=0.75,
    histnorm=histnorm_value
))
fig.add_trace(go.Histogram(
    x=df[df['fabricante'] == manufacturer2]['precio'],
    name=manufacturer2,
    opacity=0.75,
    histnorm=histnorm_value
))

# Superposición de histogramas si está normalizado
if normalized:
    fig.update_layout(barmode='overlay')

fig.update_xaxes(title_text='Price')
fig.update_yaxes(title_text='Percentage' if normalized else 'Count')

st.plotly_chart(fig)

#diagramam de dispersion
st.subheader('Diagrama de dispersion')
x_axis = st.selectbox('X axis', df.columns, index=0)
y_axis = st.selectbox('Y axis', df.columns, index=1)
color = st.selectbox('Color', df.columns, index=2)

st.subheader(f'diagrama de dispersion {x_axis} vs {y_axis} colored by {color}')
fig = px.scatter(df, x=x_axis, y=y_axis, color=color, title=f"{x_axis} vs {y_axis}")
st.plotly_chart(fig)


