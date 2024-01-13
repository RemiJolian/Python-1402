""" #The code provided is a Python script that uses the Dash framework to
 create a web application that fetches an article from a given URL, summarizes it 
using the sumy library, and converts the summary to speech using the gTTS library.
The fetch_data_from_url function fetches the content from the given URL and extracts
the article text from the HTML using BeautifulSoup. The summarize_text function summarizes
the text using LsaSummarizer from the sumy library. The text_to_speech function converts the
summary to speech using gTTS and returns an HTML audio element. 
The summarize_and_read_aloud function is a Dash callback that takes a URL as input and
returns the summary as speech. The app object is a Dash application that contains an input field 
or the URL and a div for the summary. When the user enters a URL and presses enter,
the summarize_and_read_aloud function is called and the summary is displayed as speech. """

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from bs4 import BeautifulSoup
import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from gtts import gTTS
import IPython.display as ipd

def fetch_data_from_url(url):
    # Fetch the content from the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Assuming the article text is inside <p> HTML tags
    article_text = ' '.join([p.text for p in soup.find_all('p')])

    return article_text

def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return [str(sentence) for sentence in summary]


def text_to_speech(text):
    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("summary.mp3")
    return html.Audio(src="summary.mp3", autoplay=True)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='url', type='text'),
    html.Div(id='summary')
])

@app.callback(
    Output('summary', 'children'),
    Input('url', 'value')
)
def summarize_and_read_aloud(url):
    article_text = fetch_data_from_url(url)
    summary_sentences = summarize_text(article_text)
    return text_to_speech(" ".join(summary_sentences))

if __name__ == '__main__':
    app.run()