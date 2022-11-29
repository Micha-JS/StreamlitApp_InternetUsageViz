
import stramlit as st
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import geojson
import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    return df

st.title("Internet usage per country in percentage")
st.header("Data Exploration")


with open('/Users/mjs/Documents/DS_Projects/My_first_streamlitapp/countries.geojson') as f:
    countries = geojson.load(f)
features = gj['features'][0]

internet_df = pd.read_csv('/Users/mjs/Documents/DS_Projects/My_first_streamlitapp/share-of-individuals-using-the-internet.csv')
internet_df.rename(columns={'Individuals using the Internet (% of population)':'usage_internet'}, inplace=True)




if st.checkbox("Show Dataframe"):
    st.subheader("This is my dataset:")
    st.dataframe(data=internet_df)


fig = px.choropleth(internet_df[internet_df['Year'] == 2010], geojson=countries, locations='Code', color='usage_internet',
                           color_continuous_scale="Viridis",
                           scope='world',
                           featureidkey="properties.ISO_A3",
                           labels={'usage_internet':'Individuals using the Internet in %'}
                          )

st.plotly_chart(fig)
