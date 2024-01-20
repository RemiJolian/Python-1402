#Import the required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
from bs4 import BeautifulSoup

# Create a Dash app object
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # A title
    html.H1("Web Content Extractor"),
    # A text input for the URL
    dcc.Input(id="url-input", type="text", placeholder="Enter a URL", value=""),
    # A button to submit the URL
    html.Button(id="submit-button", children="Submit"),
    # A div to display the output
    html.Div(id="output-div")
])

# Define a callback function to handle the button click
@app.callback(
    # The output is the div element
    dash.dependencies.Output("output-div", "children"),
    # The input is the URL and the button
    [dash.dependencies.Input("url-input", "value"),
     dash.dependencies.Input("submit-button", "n_clicks")]
)
def extract_text(url, n_clicks):
    # If the button is clicked
    if n_clicks:
        # Try to get the response from the URL
        try:
            response = requests.get(url)
            # If the response is successful
            if response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(response.content, "html.parser")
                # Extract the text from the body tag
                text = soup.body.get_text()
                # Return the text as the output
                return text
            # If the response is not successful
            else:
                # Return an error message
                return f"Error: {response.status_code}"
        # If the URL is invalid or unreachable
        except requests.exceptions.RequestException as e:
            # Return an error message
            return f"Error: {e}"
    # If the button is not clicked
    else:
        # Return an empty output
        return ""

# Run the app on the local server
if __name__ == "__main__":
    app.run_server(debug=True)