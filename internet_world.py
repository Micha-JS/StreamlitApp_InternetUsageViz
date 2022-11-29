
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import geojson
import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    return df

def load_geojson(path):
    gj = geojson.load(path)
    return gj

st.title("Internet usage per country in percentage")
st.header("Data Exploration")


with open('countries.geojson') as f:
    countries = geojson.load(f)


internet_df = pd.read_csv('share-of-individuals-using-the-internet.csv')
internet_df.rename(columns={'Individuals using the Internet (% of population)':'usage_internet'}, inplace=True)

#countries = load_geojson('/Users/mjs/Documents/DS_Projects/My_first_streamlitapp/countries.geojson')



if st.checkbox("Show Dataframe"):
    st.subheader("This is my dataset:")
    st.dataframe(data=internet_df)

# Setting up columns
left_column, middle_column, right_column = st.columns([3, 1, 1])

# Widgets: selectbox years
years = sorted(pd.unique(internet_df['Year']))
year = left_column.selectbox("Choose a Year", years)

# Flow control and plotting



fig = px.choropleth(internet_df[internet_df['Year'] == year], 
                    geojson=countries, locations='Code', 
                    color='usage_internet',
                    color_continuous_scale="thermal",
                    scope='world',
                    featureidkey="properties.ISO_A3",
                    labels={'usage_internet':'Individuals using the Internet in %'},
                    width=800, 
                    height=400
                          )



st.plotly_chart(fig, width=800, height=400)



fig_1 = px.line(internet_df[internet_df['Code'] == 'SAU'], x="Year", y="usage_internet", title='Population internet usage')


st.plotly_chart(fig_1)


