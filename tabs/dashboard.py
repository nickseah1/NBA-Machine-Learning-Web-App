import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pathlib
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc
from dash import html
from app import app
from dash.dependencies import Input, Output

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

data = pd.read_csv(DATA_PATH.joinpath("all_seasons.csv")).drop('Unnamed: 0', axis=1)

columns = ['Name', 'Team', 'Age', 'Height', 'Weight', 'College', 'Country', 'Draft Year', 'Draft Round', 'Draft Number',
           'Games Played', 'Points', 'Rebounds', 'Assists', 'Net Rating', 'ORB%', 'DRB%', 'USG%', 'TS%', 'AST%',
           'Season']
data.columns = columns

# Make Season column only the first year
data['Season'] = data['Season'].str.split('-').str[0]
data['Season'].astype(int)

seasons_list = data['Season'].unique().tolist()

count_list = []

for element in seasons_list:
    count = len(data[(data['Country'] == 'Canada') & (data['Season'] == element)])
    count_list.append(count)

fig1 = px.line(
    data,
    x=seasons_list,
    y=count_list,
    title='Number of Canadian Players in the NBA Over Time',
    labels={'x': 'Season', 'y': 'Count'}

)

fig1.update_layout(
    title=dict(x=0.5),  # set title in the center
)

# Uncomment to show figure
# fig1.show()

intro = dcc.Markdown("""
        ### **Visualize NBA Diversity**

        Select a country using the dropdown box below to visualize how the total number of players the given country has changed over time.

    """)

dropdown = dcc.Dropdown(
    id='country-dropdown',
    options=[
        {'label': 'USA', 'value': 'USA'},
        {'label': 'Jamaica', 'value': 'Jamaica'},
        {'label': 'Serbia and Montenegro', 'value': 'Serbia and Montenegro'},
        {'label': 'Ukraine', 'value': 'Ukraine'},
        {'label': 'Canada', 'value': 'Canada'},
        {'label': 'Croatia', 'value': 'Croatia'},
        {'label': 'Lithuania', 'value': 'Lithuania'},
        {'label': 'Nigeria', 'value': 'Nigeria'},
        {'label': 'Congo', 'value': 'Congo'},
        {'label': 'St. Vincent & Grenadines', 'value': 'St. Vincent & Grenadines'},
        {'label': 'US Virgin Islands', 'value': 'US Virgin Islands'},
        {'label': 'France', 'value': 'France'},
        {'label': 'Slovenia', 'value': 'Slovenia'},
        {'label': 'Dominican Republic', 'value': 'Dominican Republic'},
        {'label': 'Germany', 'value': 'Germany'},
        {'label': 'Georgia', 'value': 'Georgia'},
        {'label': 'New Zealand', 'value': 'New Zealand'},
        {'label': 'Belize', 'value': 'Belize'},
        {'label': 'England', 'value': 'England'},
        {'label': 'Argentina', 'value': 'Argentina'},
        {'label': 'U.S. Virgin Islands', 'value': 'U.S. Virgin Islands'},
        {'label': 'Greece', 'value': 'Greece'},
        {'label': 'Senegal', 'value': 'Senegal'},
        {'label': 'China', 'value': 'China'},
        {'label': 'Turkey', 'value': 'Turkey'},
        {'label': 'Finland', 'value': 'Finland'},
        {'label': 'Mali', 'value': 'Mali'},
        {'label': 'Puerto Rico', 'value': 'Puerto Rico'},
        {'label': 'Mexico', 'value': 'Mexico'},
        {'label': 'Yugoslavia', 'value': 'Yugoslavia'},
        {'label': 'Serbia', 'value': 'Serbia'},
        {'label': 'Venezuela', 'value': 'Venezuela'},
        {'label': 'Haiti', 'value': 'Haiti'},
        {'label': 'Russia', 'value': 'Russia'},
        {'label': 'Ireland', 'value': 'Ireland'},
        {'label': 'Brazil', 'value': 'Brazil'},
        {'label': 'Scotland', 'value': 'Scotland'},
        {'label': 'Poland', 'value': 'Poland'},
        {'label': 'Netherlands', 'value': 'Netherlands'},
        {'label': 'Czech Republic', 'value': 'Czech Republic'},
        {'label': 'Montenegro', 'value': 'Montenegro'},
        {'label': 'United Kingdom', 'value': 'United Kingdom'},
        {'label': 'Democratic Republic of the Congo', 'value': 'Democratic Republic of the Congo'},
        {'label': 'Latvia', 'value': 'Latvia'},
        {'label': 'South Korea', 'value': 'South Korea'},
        {'label': 'Uruguay', 'value': 'Uruguay'},
        {'label': 'Sudan (UK)', 'value': 'Sudan (UK)'},
        {'label': 'Australia', 'value': 'Australia'},
        {'label': 'USSR', 'value': 'USSR'},
        {'label': 'Italy', 'value': 'Italy'},
        {'label': 'Switzerland', 'value': 'Switzerland'},
        {'label': 'Gabon', 'value': 'Gabon'},
        {'label': 'Cameroon', 'value': 'Cameroon'},
        {'label': 'Iran', 'value': 'Iran'},
        {'label': 'Israel', 'value': 'Israel'},
        {'label': 'Sweden', 'value': 'Sweden'},
        {'label': 'Tanzania', 'value': 'Tanzania'},
        {'label': 'Panama', 'value': 'Panama'},
        {'label': 'Bosnia', 'value': 'Bosnia'},
        {'label': 'Great Britain', 'value': 'Great Britain'},
        {'label': 'Macedonia', 'value': 'Macedonia'},
        {'label': 'Bosnia & Herzegovina', 'value': 'Bosnia & Herzegovina'},
        {'label': 'Cabo Verde', 'value': 'Cabo Verde'},
        {'label': 'Tunisia', 'value': 'Tunisia'},
        {'label': 'South Sudan', 'value': 'South Sudan'},
        {'label': 'Bahamas', 'value': 'Bahamas'},
        {'label': 'Ghana', 'value': 'Ghana'},
        {'label': 'Austria', 'value': 'Austria'},
        {'label': 'Egypt', 'value': 'Egypt'},
        {'label': 'Japan', 'value': 'Japan'},
        {'label': 'Trinidad and Tobago', 'value': 'Trinidad and Tobago'},
        {'label': 'DRC', 'value': 'DRC'},
        {'label': 'Sudan', 'value': 'Sudan'},
        {'label': 'Angola', 'value': 'Angola'},
        {'label': 'Saint Lucia', 'value': 'Saint Lucia'},

    ],
    value='USA'
)

graph1 = dcc.Graph(
    id='graph1',
    figure=fig1,
    className='twelve columns')

row = html.Div(children=[intro, dropdown, graph1])

layout = html.Div(children=[row], style={'text-align': 'center'})


@app.callback(
    Output("graph1", "figure"),  # the output is the line
    [Input("country-dropdown", "value")],  # the input is the country
)
def update_charts(country):
    c_list = []

    for elements in seasons_list:
        counts = len(data[(data['Country'] == country) & (data['Season'] == elements)])
        c_list.append(counts)

    new_fig = px.line(data,
                      x=seasons_list,
                      y=c_list,
                      title='Number of ' + str(country) + ' Born NBA Players Over Time',
                      labels={'x': 'Season', 'y': 'NBA Players born in ' + str(country)},

                      )

    new_fig.update_layout(
        title=dict(x=0.5), title_font_size=30,  # set title in the center
    )

    return new_fig
