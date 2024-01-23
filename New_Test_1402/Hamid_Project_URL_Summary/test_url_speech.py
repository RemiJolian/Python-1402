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
    dash.dependencies.Input("url-input", "value"),
    dash.dependencies.Input("submit-button", "n_clicks")
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

# ///////////////////////////////////////////////////////////////////////
    
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output, State
# from bs4 import BeautifulSoup
# import requests
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# from gtts import gTTS
# import IPython.display as ipd

# # Initialize the Dash app
# app = dash.Dash(__name__)

# # Define the layout of the web app
# app.layout = html.Div([
#     html.H1('URL Summarizer and Text-to-Speech'),
#     dcc.Input(id='input-url', type='text', placeholder='Enter URL'),
#     html.Button('Submit', id='submit-val', n_clicks=0),
#     html.Div(id='output-summary'),
#     html.Audio(id='output-audio', controls=True)
# ])

# # Callback to fetch data from the URL, summarize it, and convert to speech
# @app.callback(
#     [Output('output-summary', 'children'), Output('output-audio', 'src')],
#     [Input('submit-val', 'n_clicks')],
#     [State('input-url', 'value')]
# )
# def summarize_and_convert(n_clicks, url):
#     if n_clicks > 0:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         article_text = ' '.join([p.text for p in soup.find_all('p')])

#         parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
#         summarizer = LsaSummarizer()
#         summary = summarizer(parser.document, 5)
#         summary_text = ' '.join([str(sentence) for sentence in summary])

#         tts = gTTS(text=summary_text, lang='en', slow=False)
#         tts.save("summary.mp3")
#         audio_src = "/assets/summary.mp3"

#         return summary_text, audio_src
#     else:
#         return '', ''

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)

#///////////////////////////////////////////////////////////////////////////////
# #from bing
    
# # Import packages
# from dash import Dash, html, dcc, callback, Input, Output
# import dash_bootstrap_components as dbc
# import plotly.express as px
# import dash_ag_grid as dag
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from bs4 import BeautifulSoup
# import requests
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# from gtts import gTTS
# import IPython.display as ipd

# # Define helper functions
# def fetch_data_from_url(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     #The soup.find_all('p') method is used to find all the <p> tags in the HTML and return them as a list.
#     #See libs_needed file in this directory
#     article_text = ' '.join([p.text for p in soup.find_all('p')])
#     return article_text

# # 5 means allow to the function to generate a summary with a specific length, in this case, 5 sentences.
# def summarize_text(text, sentence_count=10):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = LsaSummarizer()
#     summary = summarizer(parser.document, sentence_count)
#     return [str(sentence) for sentence in summary]


# def text_to_speech(my_text):
#     my_language = 'en'
#     tts = gTTS(text=my_text, lang=my_language, slow=False)
#     tts.save("summary.mp3")
#     return ipd.Audio("summary.mp3", autoplay=True) # when running,it is False ,why?

# # Create the app
# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# # Define the app layout
# app.layout = html.Div([
#     html.H1("URL Summarizer and Text-to-Speech Converter"),
#     html.P("Enter a URL and get a summary of its content and an audio file of the summary."),
#     dbc.Input(id="url-input", type="url", placeholder="Enter a URL", debounce=True),
#     html.Div(id="summary-output"),
#     html.Div(id="audio-output")
# ])

# # Define the app callback
# @app.callback(
#     [Output("summary-output", "children"), Output("audio-output", "children")],
#     [Input("url-input", "value")]
# )
# def update_output(url):
#     if url:
#         try:
#             # Fetch, summarize, and read aloud
#             article_text = fetch_data_from_url(url)
#             summary_sentences = summarize_text(article_text)
#             summary_text = " ".join(summary_sentences)
#             text_to_speech(summary_text)
#             return [
#                 html.Div([
#                     html.H3("Summarized Article:"),
#                     html.P(summary_text)
#                 ]),
#                 html.Div([
#                     html.H3("Audio File:"),
#                     html.Audio(src="summary.mp3", controls=True)
#                 ])
#             ]
#         except:
#             return [html.P("Invalid URL or error occurred."), None]
#     else:
#         return [None, None]

# # Run the app
# if __name__ == "__main__":
#     app.run_server(debug=True)
