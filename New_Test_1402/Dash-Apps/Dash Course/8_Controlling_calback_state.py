from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('Dash Course/world_happiness.csv')
line_fig = px.line(happiness[happiness['country']=='United States'],
                               x = 'year', y = 'happiness_score',
                               title = 'Happiness Score in the USA')

app = Dash()

app.layout = html.Div([
    html.H1("World Happiness Dashboard"),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href = 'https://worldhappiness.report',
                   target = '_blank')]),
    dcc.Checklist(options = happiness['region'].unique(),
                   value = ['North America']),
    dcc.RadioItems(id = 'region-radio',
                   options=happiness['region'].unique(),
                   value='North America'),
    dcc.Dropdown(id = 'country-dropdown'),
    dcc.RadioItems(id='data-radio',
                   # u can use also a list: options=['happiness_score', 'happiness_rank']
                   options={
                       'happiness_score': 'Happiness Score',
                       'happiness_rank': 'Happiness Rank'
                   },
                   value='happiness_score'),
    html.Br(),
    html.Button(id='summit-button',
                n_clicks = 0,
                children = 'Update the output'),
    dcc.Graph(id = 'happiness-graph'),
    html.Div(id='average-div')
                   ])

@app.callback(
        Output('country-dropdown','options'),
        Output('country-dropdown','value'),
        Input('region-radio','value')
)
def update_dropdown(selected_region):
    filtered_happiness = happiness[happiness['region']==selected_region]
    country_options = filtered_happiness['country'].unique()
    return country_options, country_options[0]


@app.callback(
    Output('happiness-graph','figure'),
    Output('average-div','children'),
    Input('summit-button', 'n_clicks'),
    State('country-dropdown', 'value'),
    State('data-radio', 'value')
)

def update_graph(button_click, selected_country, selected_data):
    filtered_happiness = happiness[happiness['country']==selected_country]
    #Is global nessecery?:
    global line_fig
    line_fig = px.line(filtered_happiness,
                       x='year', y=selected_data,
                       title = f'{selected_data} in {selected_country}')
    selected_avg = filtered_happiness[selected_data].mean()
    return line_fig, f'The average {selected_data} for {selected_country}'\
    f'is {selected_avg}'

if __name__ == '__main__':
    app.run_server(debug = True)  