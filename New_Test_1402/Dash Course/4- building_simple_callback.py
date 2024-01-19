# Building callbacks with single input & output
from dash import Dash, html, dcc, Input, Output

app = Dash()
# first way:
app.layout = html.Div([
    dcc.Input(id='input-text',value='Change this text',type='text'),
    html.Div(id = 'output-text')
])

#second way:

# input_text = dcc.Input(value='Change this text',type='text')
# output_text = html.Div()

# app.layout = html.Div([input_text, output_text])

@app.callback(
    # First way:
    # Notice last comment, that explain children and value difference
    Output(component_id = 'output-text', component_property = 'children'),
    Input(component_id = 'input-text', component_property = 'value')
    # second:
    # Output(component_id = output_text, component_property = 'children'),
    # Input(component_id = input_text, component_property = 'value')
)

def update_output_div(input_text):
    return f'Your Text : {input_text}'


if __name__ == '__main__':
    app.run_server(debug = True) 

# Value:
# Purpose: Stores a single value or piece of information associated with a component.
# Common uses:
# Holding the text content of input components like text boxes, sliders, dropdowns, etc.
# Setting options for components like radios or checkboxes.
# Example in code: The value property of the dcc.Input component holds the input text
# entered by the user.
    
# Children:
# Purpose: Represents the content or elements nested within a container component.
# Common uses:
# Grouping multiple components together within a layout.
# Dynamically updating the elements displayed within a container component.
# Example in code: The children property of the html.Div component is used to display the updated text based on the user's input.
# Key differences:

# Scope: value typically holds a single value within a component, while children can contain multiple elements or components.
# Mutability: value is often directly modifiable by the user (e.g., through input fields), while children are usually updated programmatically through callbacks.
# In the provided code:

# value: Used to store and retrieve the text entered by the user in the dcc.Input component.
# children: Used to dynamically update the content displayed within the html.Div component, based on the value retrieved from the input component.
# Summary:

# Use value to hold individual values or options within components.
# Use children to structure content and dynamically update elements within container components.
