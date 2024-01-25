import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pyttsx3

# Create a Dash app object
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # A title
    html.H1("Text to Speech"),
    # A text input for the text
    dcc.Input(id="text-input", type="text", placeholder="Enter text"),
    # A button to submit the text
    html.Button(id="submit-button", children="Submit"),
    # A div to display the output
    html.Div(id="output-speech")
])

# Define a callback function to handle the button click
@app.callback(
    # The output is the div element
    Output("output-speech", "children"),
    # The input is the text and the button
    Input("text-input", "value"),
    Input("submit-button", "n_clicks")
)
def text_to_speech(text, n_clicks):
    if n_clicks:
        # Initialize the text to speech engine
        engine = pyttsx3.init()
        # Convert the text to speech
        engine.save_to_file(text, 'output.mp3')
        engine.runAndWait()
        # Return an audio element to play the speech
        return html.Audio(src="output.mp3", controls=True)
    else:
        # Return an empty output
        return ""

# Run the app on the local server
if __name__ == "__main__":
    app.run_server(debug=True)
