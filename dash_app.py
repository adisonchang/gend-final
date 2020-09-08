# Author: Adison Chang
# Download the project folder and execute data.py, then dash_app.py
# and visit http://127.0.0.1:8050/ in your web browser to see the local webpage

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from datetime import datetime

import tab1, tab2, tab3, tab4, tab5, tab6

# Set some universal design variables
external_stylesheets = [dbc.themes.BOOTSTRAP]
colors = {
    'background': 'white',
    'text': 'black'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

td = datetime.today()

# Set the layout of the web app
app.layout = html.Div(children=[
    html.Br(),
    html.Br(),
    html.H1(children='GenData: Campaign Simulation',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),
    html.Br(),
    html.H4(children='Campaign Dashboard',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }),
    html.Br(),
    html.Div(children='''Adison Chang''',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }),
    html.Div(children=f'''Today's date: {td.strftime("%B %d, %Y")}''',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }),
    html.Br(),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Mail-In Ballot Count', value='tab-1'),
        dcc.Tab(label='Total Ballot Count', value='tab-2'),
        dcc.Tab(label='Mail-In Ballots Returned By County', value='tab-3'),
        dcc.Tab(label='Democratic Mail-In Ballots By County', value='tab-4'),
        dcc.Tab(label='Target Counties', value='tab-5'),
        dcc.Tab(label='Problem Counties', value='tab-6')],
        colors={
            "border": "gold",
            "primary": "royalblue",
            "background": "palegoldenrod"}
    ),
    html.Div(id='tabs-content')
], style={'backgroundColor': colors['background']})


# Set the callbacks for tab functionality
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab1.layout
    elif tab == 'tab-2':
        return tab2.layout
    elif tab == 'tab-3':
        return tab3.layout
    elif tab == 'tab-4':
        return tab4.layout
    elif tab == 'tab-5':
        return tab5.layout
    elif tab == 'tab-6':
        return tab6.layout


if __name__ == '__main__':
    app.run_server(debug=True)
