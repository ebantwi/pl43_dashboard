from dash import Dash, html, dcc
from dash.dependencies import Input, Output
#import dash_bootstrap_components as dbc

# Import pages
from pages.home import home_layout
from pages.atr_dashboard import atr_dashboard_layout
from pages.nopage import no_page_layout

# Initialize the Dash app
app = Dash(__name__, 
           external_scripts=[{'src': 'https://cdn.tailwindcss.com'}],
           suppress_callback_exceptions=True)

# Define the layout with a dcc.Location component
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/atr_dashboard':
        return atr_dashboard_layout
    elif pathname == '/':
        return home_layout
    else:
        return no_page_layout

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
