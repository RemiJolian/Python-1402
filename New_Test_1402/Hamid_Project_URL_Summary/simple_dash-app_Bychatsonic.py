# Import the necessary components from the Dash library
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Simple Dash App"),  # Create a header with the text "Simple Dash App"
    dcc.Input(id='input-box', type='text', value=''),  # Create an input box component with id 'input-box'
    html.Button('Click Me', id='button'),  # Create a button with the text "Click Me" and id 'button'
    html.Div(id='output-container-button', children='Enter a value and press the button')  # Create a div with id 'output-container-button' and initial text
])

# Define callback to update the output
@app.callback(
    Output('output-container-button', 'children'),  # Define the output property of the callback
    [Input('button', 'n_clicks')],  # Define the input property of the callback (button click)
    [Input('input-box', 'value')]  # Define another input property of the callback (value from input box)
)
def update_output(n_clicks, value):
    if n_clicks is not None:  # Check if the button has been clicked
        return f'The input value is "{value}"'  # Update the output with the input value

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)  # Start the Dash app server in debug mode
