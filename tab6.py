# tab6 presents a ranked list of 
# counties based on the number of 
# ballots that have been applied for 
# but have not been issued.
# the counties at the top of the list 
# have issued 0 ballots for a positive 
# number of applications.

import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc

from data import problem_county

# initialize ploty table
fig = go.Figure(data=[go.Table(
    header=dict(values=list(problem_county.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[problem_county.County,
                       problem_county.Applied,
                       problem_county.Issued,
                       problem_county.PercentIssued],
               fill_color='lavender',
               align='left'))
])

fig.update_layout(height=600)

# finalize tab layout 
layout = html.Div(children=[
    html.Br(),
    html.H2(children='Problem Counties',
            style={'textAlign': 'center'}),
    html.H5(children='By # of Applied but Unissued Ballots',
            style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])
