from dash import Dash, html, dcc, Input, Output
from bs4 import BeautifulSoup
import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from gtts import gTTS
import IPython.display as ipd


app = Dash()


app.layout = html.Div([
    dcc.Input(id='input-text',value='Change this text',type='text'),
    html.Div(id = 'output-text')
])


@app.callback(
    Output(component_id = 'output-text', component_property = 'children'),
    Input(component_id = 'input-text', component_property = 'value')
)

def update_output_div(input_text):
    return f'Your Text : {input_text}'


if __name__ == '__main__':
    app.run_server(debug = True) 