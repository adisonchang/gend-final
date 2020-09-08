# tab5 present a ranked list of counties based on 
# How many Democratic ballots have been issued 
# But not returned, i.e. remaining Democratic ballots

import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc

from data import target_county

# initialize plotly table
fig = go.Figure(data=[go.Table(
    header=dict(values=list(target_county.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[target_county.County,
                       target_county.Issued,
                       target_county.Returned,
                       target_county.Remaining],
               fill_color='lavender',
               align='left'))
])

fig.update_layout(height=600)

# finalize tab layout 
layout = html.Div(children=[
    html.Br(),
    html.H2(children='Counties to Target',
            style={'textAlign': 'center'}),
    html.H5(children='Based on # Dems Who Havent Returned Their Ballots',
            style={'textAlign': 'center'}),
    html.Div(children=dcc.Graph(figure=fig))
])
