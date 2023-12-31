# Building callbacks with single input & output
from dash import Dash, html, dcc, Input, Output

app = Dash()
# first way:
#app.layout = html.Div([
#     dcc.Input(id='input-text',value='Change this text',type='text'),
#     html.Div(id = 'output-text')
# ])

#second way:

input_text = dcc.Input(value='Change this text',type='text')
output_text = html.Div()

app.layout = html.Div([input_text, output_text])

@app.callback(
    # First way:
    # Output(component_id = 'output-text', component_property = 'children'),
    # Input(component_id = 'input-text', component_property = 'value')
    # second:
    Output(component_id = output_text, component_property = 'children'),
    Input(component_id = input_text, component_property = 'value')
)

def update_output_div(input_text):
    return f'Text : {input_text}'

if __name__ == '__main__':
    app.run_server(debug = True) 


