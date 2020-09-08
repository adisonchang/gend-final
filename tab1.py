# This file sets the layout for the 1st tab of the webpage
# Contains 4 large numbers with mail-in ballot info

import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html

from data import mail_tots

# GET DATA VALUES
ttl_ret = sum(mail_tots['Returned'])
ttl_rem = sum(mail_tots['Remaining'])
dem_ret = mail_tots.loc[mail_tots['Party'] == 'DEMOCRAT', 'Returned'].item()
dem_rem = mail_tots.loc[mail_tots['Party'] == 'DEMOCRAT', 'Remaining'].item()

# Initialize Dash Figure
fig = go.Figure()

# Adding first number
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=ttl_ret,
    title={'text': "Mail-in Ballots Returned", 'align': 'center'},
    gauge={'axis': {'visible': False}},
    domain={'row': 1, 'column': 0}))

# Second number
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=dem_ret,
    title={'text': "Dem Mail-In Ballots Returned"},
    gauge={'axis': {'visible': False}},
    domain={'row': 1, 'column': 1}
))

# Third number
fig.add_trace(go.Indicator(
    mode="number",
    value=ttl_rem,
    title={'text': "Mail-in Ballots Remaining"},
    domain={'row': 3, 'column': 0}
))

# Fourth number
fig.add_trace(go.Indicator(
    mode="number",
    value=dem_rem,
    title={'text': "Dem Mail-In Ballots Remaining"},
    domain={'row': 3, 'column': 1}
))

# Set some design information
fig.update_layout(
    grid={'rows': 4, 'columns': 2, 'pattern': "independent"},
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=50,
        pad=4)
)

# Finalize tab layout
layout = html.Div(children=[
    html.Br(),
    html.H2(
        children='Mail-In Ballot Info',
        style={'textAlign': 'center'}),
    dcc.Graph(id='total-returned', figure=fig)
])
