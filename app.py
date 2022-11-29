# Streamlit live coding script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy


# First some MPG Data Exploration





# Add title and header
st.title("Introduction to Streamlit")
st.header("MPG Data Exploration")

@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df

mpg_df_raw = load_data(path="mpg.csv")
mpg_df = deepcopy(mpg_df_raw)

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if st.checkbox("Show Dataframe"):
    st.subheader("This is my dataset:")
    st.dataframe(data=mpg_df)
    # st.table(data=mpg_df)

# In Matplotlib
m_fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(mpg_df['displ'], mpg_df['hwy'], alpha=0.7)

ax.set_title("Engine Size vs. Highway Fuel Mileage")
ax.set_xlabel('Displacement (Liters)')
ax.set_ylabel('MPG')

means = mpg_df.groupby('class').mean()
ax.scatter(means['displ'], means['hwy'], alpha=0.7, color="red")

st.pyplot(m_fig)

# Widgets: selectbox
years = ["All"]+sorted(pd.unique(mpg_df['year']))
year = st.selectbox("Choose a Year", years)

# In Plotly
p_fig = px.scatter(mpg_df, x='displ', y='hwy', opacity=0.5,
                   range_x=[1, 8], range_y=[10, 50],
                   width=750, height=600,
                   labels={"displ": "Displacement (Liters)",
                           "hwy": "MPG"},
                   title="Engine Size vs. Highway Fuel Mileage")
p_fig.update_layout(title_font_size=22)

st.plotly_chart(p_fig)
