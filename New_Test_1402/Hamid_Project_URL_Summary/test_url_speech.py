#Import the required libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from bs4 import BeautifulSoup
import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from gtts import gTTS
import IPython.display as ipd
import base64

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
    html.Div(id="output-summary-div"),
    html.Div(id="output-speech-div")
])

# Define a callback function to handle the button click
@app.callback(
    # The output is the div element
    Output("output-summary-div", "children"),
    Output("output-speech-div", "children"),
    # The input is the URL and the button
    Input(component_id="url-input",component_property="value"),
    Input(component_id="submit-button", component_property="n_clicks")
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
                # Summarize the text of content
                sentence_count = 5
                parser = PlaintextParser.from_string(text, Tokenizer("english"))
                summarizer = LsaSummarizer()
                summary = summarizer(parser.document, sentence_count)
                summary_text =' '.join(str(sentence) for sentence in summary)
                my_language = 'en'
                tts = gTTS(text=summary_text, lang=my_language, slow=False)
                tts.save("summary.mp3")
                # Second method:
                #with open("summary.mp3", "rb") as audio_file:
                    #encoded_string = base64.b64encode(audio_file.read()).decode('utf-8')
                #audio_final = html.Audio(src=f"data:audio/mp3;base64,{encoded_string}", controls=True)
                #return summary_text and speech file
                audio_final = html.Audio(src='data:audio/mpeg;base64,{}'.format(base64.b64encode(open('summary.mp3', 'rb').read()).decode()), controls=True)
                return summary_text, audio_final
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