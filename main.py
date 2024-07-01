# Import packages
from dash import Dash, html, dash_table
import pandas as pd

# Initialize the app
app = Dash()

# App layout
app.layout = [html.Div(children='My Dash Table')]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
