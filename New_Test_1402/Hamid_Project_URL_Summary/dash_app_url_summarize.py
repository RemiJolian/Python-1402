import dash
import requests
from bs4 import BeautifulSoup
import dash_html_components as html
from dash.dependencies import Input, Output
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from gtts import gTTS
from IPython.display import display
import IPython.display as ipd


# Your existing functions
def fetch_data_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
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
    return ipd.Audio("summary.mp3", autoplay=True)

app = dash.Dash(__name__)

# Dash app layout
app.layout = html.Div([
    dash.dcc.Input(id='url-input', type='text', placeholder='Enter URL'),
    html.Button('Fetch and Summarize', id='fetch-button'),
    html.Audio(id='audio-output', style={'display': 'none'}),
])

# Dash app callbacks
@app.callback(
    Output('audio-output', 'src'),
    Input('fetch-button', 'n_clicks'),
    [Input('url-input', 'value')],
    [dash.dependencies.State('audio-output', 'src')],
)
def fetch_and_summarize(n_clicks, url):
    if n_clicks is None:
        return
    article_text = fetch_data_from_url(url)
    summary_sentences = summarize_text(article_text)
    summary_text = " ".join(summary_sentences)
    tts = gTTS(text=summary_text, lang='en', slow=False)
    tts.save("summary.mp3")
    audio_data = open("summary.mp3", "rb").read()
    data_uri = f"data:audio/mpeg;base64,{base64.b64encode(audio_data).decode()}"
    return data_uri

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug = True)