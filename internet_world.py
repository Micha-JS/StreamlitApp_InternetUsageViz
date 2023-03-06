
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import geojson
import pandas as pd

# Load the data

with open('./data/countries.geojson') as f:
    countries = geojson.load(f)

internet_df = pd.read_csv('data/share-of-individuals-using-the-internet.csv')
internet_df.rename(columns={'Individuals using the Internet (% of population)':'internet_usage'}, inplace=True)

st.title("Internet usage per country in percent")
st.header("Data Exploration")




if st.checkbox("Show data"):
    st.subheader("Table with internet usage in percent per country:")
    st.dataframe(data=internet_df)

# Setting up columns
left_column, middle_column, right_column = st.columns([3, 1, 1])

# Widgets: selectbox years
years = sorted(pd.unique(internet_df['Year']))
year = left_column.selectbox("Choose a year", years)

# Flow control and plotting



fig = px.choropleth(internet_df[internet_df['Year'] == year], 
                    geojson=countries, locations='Code', 
                    color='internet_usage',
                    color_continuous_scale="thermal",
                    scope='world',
                    featureidkey="properties.ISO_A3",
                    labels={'internet_usage':'Individuals using the internet in %'},
                    width=800, 
                    height=400
                          )



st.plotly_chart(fig, width=1200, height=600)



fig_1 = px.line(internet_df[internet_df['Code'] == 'SAU'],
                x="Year",
                y="internet_usage",
                title='Population internet usage')


st.plotly_chart(fig_1)


