import dash
import dash_html_components as html
from flask import Flask
import subprocess
import dash_core_components as dcc
#/////////////////////////////////
server = Flask(__name__)
app = dash.Dash(__name__, server=server)
#/////////////////////////////////
app.layout = html.Div([
    html.H1('Run Python File'),
    html.Div([
        html.Label('Enter file name: '),
        html.Div([
            dcc.Input(id='input-box', type='text'),
            html.Button('Run', id='button')
        ])
    ]),
    html.Div(id='output-container')
])
#//////////////////////////////////////
@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def run_script(n_clicks, value):
    if n_clicks is not None:
        result = subprocess.run(['python', value], stdout=subprocess.PIPE)
        return html.Div([
            html.P(result.stdout.decode('utf-8'))
        ])