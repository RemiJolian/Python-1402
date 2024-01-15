# suggest by AI prxpl

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from bs4 import BeautifulSoup
import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from gtts import gTTS
import IPython.display as ipd

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    dcc.Input(id='url-input', type='text', placeholder='Enter the URL'),
    html.Button('Summarize and Convert to MP3', id='submit-button', n_clicks=0),
    html.Div(id='output-audio')
])

# Define the summarization and MP3 conversion process
@app.callback(
    Output('output-audio', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('url-input', 'value')]
)
def summarize_and_convert_to_mp3(n_clicks, url):
    if n_clicks > 0:
        # Fetch data from the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = ' '.join([p.text for p in soup.find_all('p')])

        # Summarize the text
        parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, 5)
        summarized_text = ' '.join([str(sentence) for sentence in summary])

        # Convert the summarized text to MP3
        tts = gTTS(text=summarized_text, lang='en', slow=False)
        tts.save("summary.mp3")

        # Return the audio player for the MP3 file
        return ipd.Audio("summary.mp3", autoplay=True)

    # If the button has not been clicked, return nothing
    return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)