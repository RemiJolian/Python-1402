from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash()

avocado = pd.read_csv('Dash Course/Dash Avocado Project/avocado.csv')

app.layout = html.Div([html.H1('Avocado Prices Dashboard'),
                    #    html.P(),
                    #    html.Br(),
                    #    html.A(),
                       dcc.Dropdown(id = 'geo-dropdown',
                                    options = avocado['geography'].unique(),
                                    values = 'New Yourk'),
                    #    dcc.RadioItems(),
                    #    dcc.Checklist(),
                       dcc.Graph(id = "price-graph")
])

@app.callback()


if __name__ == '__main__':
    app.run_server(debug=True)