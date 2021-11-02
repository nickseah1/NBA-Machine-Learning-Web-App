import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html

from app import app, server
from tabs import predict, intro, salary, dashboard

style = {'maxWidth': '1440px', 'margin': 'auto', 'font-family': 'system-ui', 'height': '100vh', 'width': '100vw'}

app.layout = html.Div([
    dcc.Markdown('# NBA Machine Learning Hub'),
    dcc.Tabs(id='tabs', value='tab-intro', style={'font-weight': 'bold', 'padding': 10},
             children=[
                 dcc.Tab(label='Home', value='tab-intro'),
                 dcc.Tab(label='Predict NBA All-Stars', value='tab-predict'),
                 dcc.Tab(label='Predict NBA Salary', value='tab-salary'),
                 dcc.Tab(label='Visualize Diversity in the NBA', value='tab-dashboard'),
             ]),
    html.Div(id='tabs-content'),
], style=style)


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro':
        return intro.layout
    elif tab == 'tab-predict':
        return predict.layout
    elif tab == 'tab-salary':
        return salary.layout
    elif tab == 'tab-dashboard':
        return dashboard.layout


if __name__ == '__main__':
    app.run_server(debug=True)
