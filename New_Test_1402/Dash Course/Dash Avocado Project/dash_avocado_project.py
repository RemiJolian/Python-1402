from dash import Dash, html, dcc, Input, Output
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

#   - the output is the figure property of the graph component

#   - the input is the value property of the dropdown component:
@app.callback(
               Output(component_id= ..., component_property = 'figure?..'),
               Input(component_id= ..., component_property = 'value?')
)
def update_graph():
   pass
   return line_fig    

if __name__ == '__main__':
    app.run_server(debug=True)
    