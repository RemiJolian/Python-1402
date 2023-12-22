from dash import Dash, html, dcc
#import dash
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('Dash Course/world_happiness.csv')
line_fig = px.line(happiness[happiness['country']=='United States'],
                               x = 'year', y = 'happiness_score',
                               title = 'Happiness Score in the USA')

my_app = Dash()

# 2 main parts for dash App is Layout and interactivity
my_app.layout = html.Div([
    html.H1("World Happiness Dashboard"),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href = 'https://worldhappiness.report',
                   target = '_blank')]),
    dcc.RadioItems(options = happiness['region'].unique(),
                   value = 'North America'),
    dcc.Checklist(options = happiness['region'].unique(),
                   value = ['North America']),
    dcc.Dropdown(options = happiness['country'].unique(),
                   value = 'United States'),
    dcc.Graph(figure = line_fig)
                   ])

if __name__ == '__main__':
    my_app.run_server(debug = True)