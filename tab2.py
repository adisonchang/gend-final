import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html

from data import tot_tots

ttl_ret = sum(tot_tots['Returned'])
ttl_rem = sum(tot_tots['Remaining'])
dem_ret = tot_tots.loc[tot_tots['Party'] == 'DEMOCRAT', 'Returned'].item()
dem_rem = tot_tots.loc[tot_tots['Party'] == 'DEMOCRAT', 'Remaining'].item()

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=ttl_ret,
    title={'text': "Total Ballots Returned", 'align': 'center'},
    gauge={'axis': {'visible': False}},
    domain={'row': 1, 'column': 0}))

fig.add_trace(go.Indicator(
    mode="gauge+number",
    value=dem_ret,
    title={'text': "Total Dem Ballots Returned"},
    gauge={'axis': {'visible': False}},
    domain={'row': 1, 'column': 1}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=ttl_rem,
    title={'text': "Total Ballots Remaining"},
    domain={'row': 3, 'column': 0}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=dem_rem,
    title={'text': "Total Dem Ballots Remaining"},
    domain={'row': 3, 'column': 1}
))

fig.update_layout(
    grid={'rows': 4, 'columns': 2, 'pattern': "independent"},
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=50,
        pad=4)
)

layout = html.Div(children=[
    html.Br(),
    html.H2(
        children='Total Ballot Info',
        style={'textAlign': 'center'}),
    dcc.Graph(id='total-returned', figure=fig)
])
