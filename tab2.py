# Tab2.py sets the layout for the 2nd tab of the webpage
# Four numbers that exhibit how many votes have been returned

import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html

from data import tot_tots

ttl_ret = sum(tot_tots['Returned'])
ttl_rem = sum(tot_tots['Remaining'])
dem_ret = tot_tots.loc[tot_tots['Party'] == 'DEMOCRAT', 'Returned'].item()
dem_rem = tot_tots.loc[tot_tots['Party'] == 'DEMOCRAT', 'Remaining'].item()

# Initialize Dash Figure
fig = go.Figure()

# Set 1st number: Total Ballots Returned
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=ttl_ret,
    title={'text': "Total Ballots Returned", 'align': 'center'},
    gauge={'axis': {'visible': False}},
    domain={'row': 1, 'column': 0}))

# 2nd number: Total Democratic Ballots Returned
fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=dem_ret,
    title={'text': "Total Dem Ballots Returned"},
    gauge={'axis': {'visible': False}},
    domain={'row': 1, 'column': 1}
))

# 3rd number: Total Ballots Remaining / Yet to be returned
fig.add_trace(go.Indicator(
    mode="number",
    value=ttl_rem,
    title={'text': "Total Ballots Remaining"},
    domain={'row': 3, 'column': 0}
))

# 4th Number: Total Democratic Ballot Remaining
fig.add_trace(go.Indicator(
    mode="number",
    value=dem_rem,
    title={'text': "Total Dem Ballots Remaining"},
    domain={'row': 3, 'column': 1}
))

# Set some design variables
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
        children='Total Ballot Info',
        style={'textAlign': 'center'}),
    dcc.Graph(id='total-returned', figure=fig)
])
