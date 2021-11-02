from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html

from joblib import load
import numpy as np
import pandas as pd

from app import app

style = {'display': 'inline-block'}

layout = html.Div([
    dcc.Markdown("""
        ### **NBA Salary Predictor**
        
        Enter the player statistics below and click submit to see the expected salary cap percentage of a player.
        This is not the salary the player earned but the expected value based on these statistics. Players that were paid higher than their expected value were likely on teams that performed badly.

        **Statistics Breakdown**
        
        PPG: Points Per Game in a season
        
        PER: Player Efficiency Rating
        
        TOV: Turnovers Per Game in a season
        
        WS: Win Shares in a season
        
        VORP: Value Over Replacement Player
        
        
    """),

    html.Div([
        dcc.Markdown('###### **PPG**'),
        dcc.Input(
            id='pts',
            value=20
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### **PER**'),
        dcc.Input(
            id='per',
            value=15
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### **TOV**'),
        dcc.Input(
            id='tov',
            value=2
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### **WS**'),
        dcc.Input(
            id='ws',
            value=5
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### **VORP **'),
        dcc.Input(
            id='vorp',
            value=5
        ),
    ], style={'display': 'inline-block', 'padding': 10}),

    html.Br(),
    html.Button(id='submit-val', n_clicks=0, children='Submit'),
    html.Br(),

    html.Div(id='salary_prediction-content', style={'fontWeight': 'bold'})

])




@app.callback(
    Output('salary_prediction-content', 'children'),
    [Input('submit-val', 'n_clicks'),
     State('pts', 'value'),
     State('per', 'value'),
     State('tov', 'value'),
     State('ws', 'value'),
     State('vorp', 'value')])
def salary_predict(n_clicks, pts, per, tov, ws, vorp):
    df = pd.DataFrame(
        columns=['PTS', 'PER', 'TOV', 'WS', 'VORP'],
        data=[[pts, per, tov, ws, vorp]]
    )
    df = df.reset_index(drop=True)
    clf = load('model/lr.joblib')
    y_pred_log = clf.predict(df)
    y_pred = y_pred_log[0]
    salary_cap_percentage = y_pred * 100

    results = f"The predicted salary cap for your player is {salary_cap_percentage:.2f}% of the team's salary cap"

    return results
