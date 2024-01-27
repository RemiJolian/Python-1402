# Import libs
from dash import dcc, html, Dash, Input, Output
from bs4 import BeautifulSoup
import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import IPython.display as ipd
import base64
import pyttsx3
#Instead of pyttsx3 lib, import gTTS from gtts

# Create a Dash app object
app = Dash()

# Define the layout of the app
app.layout = html.Div([
    # A title
    html.H1("Web Content Extractor"),
    html.H2("Inter your URL address, then wait a minute to summarize and speech it"),
    # A text input for the URL
    dcc.Input(id="url-input", type="text", placeholder="Enter a URL", value="Enter a URL"),
    # A button to submit the URL
    html.Button(id="submit-button", children="Submit"),
    # A div to display the summary output
    html.Div(id="output-summary-div"),
    # A div to display the Audio output
    html.Div(id="output-speech-div")
])

# Define a callback function to handle the button click
@app.callback(
    # The output is the div element
    Output("output-summary-div", "children"),
    # The input is the URL and the button
    Input(component_id="url-input",component_property="value"),
    Input(component_id="submit-button", component_property="n_clicks")
)

# Define a function to get text of body of website and extract it
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
                return summary_text
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
    
# Define a callback function to handle the the speech
@app.callback(
    Output("output-speech-div", "children"),
    Input("output-summary-div", "children")
)

# Define a function to convert summary text to speech file
def generate_speech(summary_text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.save_to_file(summary_text, "summary.mp3")
    engine.runAndWait()
    engine.say(summary_text)
    with open("summary.mp3", "rb") as audio_file:
        encoded_string = base64.b64encode(audio_file.read()).decode('utf-8')
    audio_final = html.Audio(src=f"data:audio/mp3;base64,{encoded_string}", controls=True)
    return audio_final

# Run the dash app 
if __name__ == "__main__":
    app.run_server(debug=True)