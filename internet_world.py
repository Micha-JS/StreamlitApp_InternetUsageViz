
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

gapminder_df = pd.read_csv('data/gapminder.csv')

st.title("Internet usage per country in percent")
st.header("Data Exploration")




if st.checkbox("Show data"):
    st.subheader("Table with internet usage in percent per country:")
    st.dataframe(data=internet_df)

# Setting up columns
left_column, middle_column, right_column = st.columns([3,1,1])


# Widgets: selectbox years
years = sorted(pd.unique(internet_df['Year']))
year = left_column.selectbox("Choose a year", years, index = 15)





fig_go = go.Figure(data=go.Choropleth(
    locations = internet_df[internet_df['Year'] == year]['Code'],
    z = internet_df[internet_df['Year'] == year]['internet_usage'].round(2),
    text = internet_df[internet_df['Year'] == year]['Entity'],
    colorscale = 'thermal',
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_ticksuffix = '%',
    colorbar_title = 'Internet <br>usage in %',
))

fig_go.update_layout(
    title = {'text':'Individuals using the internet per country in percent',
             'y': 0.9,
             'x': 0.5,
             'xanchor': 'center',
             'yanchor': 'top'
             },
    font={
        'family': "verdana, monospace",
        'size': 12},
    geo=dict(
        showframe=True,
        showcoastlines=True,
        projection_type='equirectangular'
    )
)

fig_go.update_coloraxes(colorbar_tickfont=dict(
        family = 'Verdana',
        size = 12
    )
)

st.plotly_chart(fig_go)



# Widgets: selectbox country
# Setting up columns
left_column, middle_column, right_column = st.columns([3,1,1])
country = sorted(pd.unique(internet_df['Entity']))
#cntr = left_column.selectbox("Choose a country", country)
cntr = left_column.multiselect("Choose a country",
                               country,
                               default=['Latvia','Andorra','Lebanon','Australia','Germany'],
                               max_selections = 5)



def add_trace_f(num = 1):
    fig_1.add_trace(go.Scatter(x=internet_df[internet_df['Entity']==cntr[num]]['Year'],
                             y=internet_df[internet_df['Entity']==cntr[num]]['internet_usage'],
                            mode='lines',
                            hovertemplate =
                            '<b>Internet usage: %{y:.2f} %</b><br>'+
                            '<b>Year: %{x}</b><br>',
                            name=cntr[num]))

fig_1 = go.Figure()

if len(cntr) == 5:
    for i in range(len(cntr)):
        add_trace_f(num = i)

if len(cntr) == 4:
    for i in range(len(cntr)):
        add_trace_f(num = i)

if len(cntr) == 3:
    for i in range(len(cntr)):
        add_trace_f(num = i)

if len(cntr) == 2:
    for i in range(len(cntr)):
        add_trace_f(num = i)

if len(cntr) == 1:
    for i in range(len(cntr)):
        add_trace_f(num = i)


fig_1.update_layout(
    title= {'text':"Individuals using the internet per country in percent",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
    xaxis_title="Year",
    yaxis_title="Internet usage in %",
    font={
        'family':"verdana, monospace",
        'size':12}
    )


st.plotly_chart(fig_1)


# Widgets: selectbox country
# Setting up columns
left_column, middle_column, right_column = st.columns([3,1,1])
country = sorted(pd.unique(gapminder_df['Entity']))
cntr = left_column.multiselect("Choose a country",
                               country,
                               default=['Brazil','Kuwait','Lebanon','United States','Germany'],
                               max_selections = 5)



def add_trace_f(num = 1):
    fig_2.add_trace(go.Scatter(x=gapminder_df[gapminder_df['Entity']==cntr[num]]['internet_usage'],
                             y=gapminder_df[gapminder_df['Entity']==cntr[num]]['co2_tonnes_per_person'],
                            mode='lines+markers',
                            hovertemplate =
                            '<b>CO2/pp: %{y:.2f} t</b><br>'+
                            '<b>Internet usage: %{x:.2f} %</b><br>'+
                            '<b>%{text}</b>',
                            text = ['Year: {}'.format(i + 1) for i in range(1989,2015,1)],
                            name=cntr[num]))

fig_2 = go.Figure()

if len(cntr) == 5:
    for i in range(len(cntr)):
        add_trace_f(num = i)

if len(cntr) == 4:
    for i in range(len(cntr)):
        add_trace_f(num = i)

if len(cntr) == 3:
    for i in range(len(cntr)):
        add_trace_f(num = i)

if len(cntr) == 2:
    for i in range(len(cntr)):
        add_trace_f(num = i)

if len(cntr) == 1:
    for i in range(len(cntr)):
        add_trace_f(num = i)


fig_2.update_layout(
    title= {'text':"CO2 emissions per person and internet usage between 1990-2015",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
    xaxis_title="Internet usage in %",
    yaxis_title="CO2 emissions per person in t",
    font={
        'family':"verdana, monospace",
        'size':12}
    )


st.plotly_chart(fig_2)