from dash.dependencies import Input, Output
from dash import dcc
from dash import html

from joblib import load
import numpy as np
import pandas as pd

from app import app

# cities = ['Belvedere',
#           'Bolinas',
#           'Corte Madera',
#           'Dillon Beach',
#           'Fairfax',
#           'Greenbrae',
#           'Inverness',
#           'Kentfield',
#           'Larkspur',
#           'Marshall',
#           'Mill Valley',
#           'Muir Beach',
#           'Nicasio',
#           'Novato',
#           'Point Reyes',
#           'Ross',
#           'San Anselmo',
#           'San Geronimo Valley',
#           'San Rafael',
#           'Sausalito',
#           'Stinson Beach',
#           'Tiburon',
#           'Tomales',
#           'Other'
#           ]

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### **NBA All-Star Predictor**
        
        Use the controls below to update your player will be an NBA All-Star, based on points,
        assists, rebounds, steals, and blocks.
        
    """),

    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),

    # html.Div([
    #     dcc.Markdown('###### Area'),
    #     dcc.Dropdown(
    #         id='area',
    #         options=[{'label': city, 'value': city} for city in cities],
    #         value=cities[10]
    #     ),
    # ], style=style),

    html.Div([
        dcc.Markdown('###### **Points Per Game**'),
        dcc.Slider(
            id='ppg',
            min=0,
            max=40,
            step=0.1,
            value=10,
            tooltip={"placement": "top", "always_visible": True},
            marks={n: str(n) for n in range(0, 40, 5)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### **Rebounds Per Game**'),
        dcc.Slider(
            id='rpg',
            min=0,
            max=25,
            step=0.1,
            value=10,
            tooltip={"placement": "top", "always_visible": True},
            marks={n: str(n) for n in range(0, 25, 5)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### **Assists Per Game**'),
        dcc.Slider(
            id='apg',
            min=0,
            max=20,
            step=0.1,
            value=8,
            tooltip={"placement": "top", "always_visible": True},
            marks={n: str(n) for n in range(0, 20, 4)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### **Steals Per Game**'),
        dcc.Slider(
            id='spg',
            min=0,
            max=8,
            step=0.1,
            value=1,
            tooltip={"placement": "top", "always_visible": True},
            marks={n: str(n) for n in range(0, 8, 2)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### **Blocks Per Game**'),
        dcc.Slider(
            id='bpg',
            min=0,
            max=8,
            step=0.1,
            value=1,
            tooltip={"placement": "top", "always_visible": True},
            marks={n: str(n) for n in range(0, 8, 2)}
        ),
    ], style=style),


])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('ppg', 'value'),
     Input('rpg', 'value'),
     Input('apg', 'value'),
     Input('spg', 'value'),
     Input('bpg', 'value')])
def predict(ppg, rpg, apg, spg, bpg):

    df = pd.DataFrame(
        columns=['PPG', 'RPG', 'APG', 'SPG', 'BPG'],
        data=[[ppg, rpg, apg, spg, bpg]]
    )

    clf = load('model/rfclf.joblib')
    y_pred_log = clf.predict(df)
    if y_pred_log == 1:
        results = 'Prediction: This Player is predicted to be an All-Star!'
    else:
        results = 'Prediction: This Player is not predicted to be an All-Star...'

    return results
