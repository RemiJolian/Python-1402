import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from gtts import gTTS
import base64
import IPython.display as ipd


# Your existing functions
def fetch_data_from_url(url):
    #sends an HTTP GET request to URL
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

app.layout = html.Div([
    dcc.Input(id='url-input', type='text', placeholder='Enter URL'),
    html.Button('Fetch and Summarize', id='fetch-button'),
    html.Audio(id='audio-output', controls=True, style={'display': 'none'}),
])

@app.callback(
    Output('audio-output', 'src'),
    Input('fetch-button', 'n_clicks'),
    [State('url-input', 'value')]
)
def fetch_and_summarize(n_clicks, url):
    if n_clicks is None:
        return

    article_text = fetch_data_from_url(url)
    summary_sentences = summarize_text(article_text)
    summary_text = " ".join(summary_sentences)

    tts = gTTS(text=summary_text, lang='en', slow=False)
    tts.save("summary.mp3")

    with open("summary.mp3", "rb") as audio_file:
        encoded_audio = base64.b64encode(audio_file.read()).decode()

    return "data:audio/mpeg;base64,{}".format(encoded_audio)

if __name__ == '__main__':
    app.run_server(debug=True)
#-----------------------------------------------------------------------------------------

# #from bard
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State
# import requests
# from bs4 import BeautifulSoup
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# from gtts import gTTS
# import base64

# # Define functions
# def fetch_data_from_url(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     article_text = ' '.join([p.text for p in soup.find_all('p')])
#     return article_text

# def summarize_text(text, sentence_count=5):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = LsaSummarizer()
#     summary = summarizer(parser.document, sentence_count)
#     return [str(sentence) for sentence in summary]

# def text_to_speech(text):
#     tts = gTTS(text=text, lang='en', slow=False)
#     tts.save("summary.mp3")
#     with open("summary.mp3", "rb") as audio_file:
#         encoded_audio = base64.b64encode(audio_file.read()).decode()
#     return "data:audio/mpeg;base64,{}".format(encoded_audio)

# # Create Dash app
# app = dash.Dash(__name__)

# # App layout
# app.layout = html.Div([
#     dcc.Input(id='url-input', type='text', placeholder='Enter URL'),
#     html.Button('Fetch and Summarize', id='fetch-button'),
#     html.Audio(id='audio-output', controls=True, style={'display': 'none'}),
# ])

# # Callback
# @app.callback(
#     Output('audio-output', 'src'),
#     Input('fetch-button', 'n_clicks'),
#     [State('url-input', 'value')]
# )
# def fetch_and_summarize(n_clicks, url):
#     if n_clicks is None:
#         return

#     try:
#         article_text = fetch_data_from_url(url)
#         summary_sentences = summarize_text(article_text)
#         summary_text = " ".join(summary_sentences)
#         audio_src = text_to_speech(summary_text)
#         return audio_src
#     except Exception as e:
#         print(f"Error: {e}")  # Print error for debugging
#         return None  # Handle error gracefully in the app

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)


