import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Title of the app centered
st.title('US Vehicle Advertisement Listings')

# Read data from csv file vehicles.csv
df = pd.read_csv('vehicles_us.csv')

# Extraer la marca desde la columna 'model'
df['manufacturer'] = df['model'].str.split().str[0]

# Show data in the app
st.write(df.head())

# Histogram of the types of vehicles by manufacturer
st.subheader('Histogram of the types of vehicles by manufacturer')
fig = px.histogram(df, x='manufacturer', color='type', title="Vehicle Types by Manufacturer")
st.plotly_chart(fig)

# Histogram of price distribution between manufacturers
st.subheader('Histogram of price distribution between manufacturers')

# Dropdown menus for selecting two manufacturers
manufacturer_list = df['manufacturer'].dropna().unique()
manufacturer1 = st.selectbox('Manufacturer 1', manufacturer_list, index=0)
manufacturer2 = st.selectbox('Manufacturer 2', manufacturer_list, index=1)

# Checkbox for normalization
normalized = st.checkbox('Normalized')

# Create histogram
fig = go.Figure()
histnorm_value = 'percent' if normalized else None
fig.add_trace(go.Histogram(
    x=df[df['manufacturer'] == manufacturer1]['price'],
    name=manufacturer1,
    opacity=0.75,
    histnorm=histnorm_value
))
fig.add_trace(go.Histogram(
    x=df[df['manufacturer'] == manufacturer2]['price'],
    name=manufacturer2,
    opacity=0.75,
    histnorm=histnorm_value
))

# Overlay histograms if normalized
if normalized:
    fig.update_layout(barmode='overlay')

fig.update_xaxes(title_text='Price')
fig.update_yaxes(title_text='Percentage' if normalized else 'Count')

st.plotly_chart(fig)

# Scatter plot
st.subheader('Scatter plot')
x_axis = st.selectbox('X axis', df.columns, index=0)
y_axis = st.selectbox('Y axis', df.columns, index=1)
color = st.selectbox('Color', df.columns, index=2)

st.subheader(f'Scatter plot of {x_axis} vs {y_axis} colored by {color}')
fig = px.scatter(df, x=x_axis, y=y_axis, color=color, title=f"{x_axis} vs {y_axis}")
st.plotly_chart(fig)
