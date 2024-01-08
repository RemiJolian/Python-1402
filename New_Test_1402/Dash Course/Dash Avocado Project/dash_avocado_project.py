from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

avocado = pd.read_csv('Dash Course/Dash Avocado Project/avocado.csv')

geo_dropdown = dcc.Dropdown(options=avocado['geography'].unique(),
                            value='New York')

app.layout = html.Div(children=[
    html.H1(children='Avocado Prices Dashboard'),
    geo_dropdown,
    dcc.Graph(id='price-graph')
])


# Step 4: Adding the callback function
@app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    return line_fig


# Step 5: Running the dashboard
if __name__ == '__main__':
    app.run_server(debug=True)

# -----------------------------------------------------------------------------

# app.layout = html.Div([html.H1('Avocado Prices Dashboard'),
#                     #    html.P(),
#                     #    html.Br(),
#                     #    html.A(),
#                        dcc.Dropdown(id = 'geo-dropdown',
#                                     options = avocado['geography'].unique(),
#                                     values = 'New York'),
#                     #    dcc.RadioItems(),
#                     #    dcc.Checklist(),
#                        dcc.Graph(id = "price-graph")
# ])

# #   - the output is the figure property of the graph component

# #   - the input is the value property of the dropdown component:
# @app.callback(
#                Output(component_id= ..., component_property = 'figure?..'),
#                Input(component_id= ..., component_property = 'value?')
# )
# def update_graph():
#    pass
#    return line_fig    

# if __name__ == '__main__':
#     app.run_server(debug=True)
    