import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from data import mail_county

fig = px.scatter(mail_county, x="Issued", y="Returned",
                 opacity=0.7,
                 hover_name="County",
                 color="Remaining",
                 log_x=True, log_y=True)

fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='black')),
                  selector=dict(mode='markers'))

fig2 = px.scatter(mail_county, x="Issued", y="Returned",
                  opacity=0.7,
                  hover_name="County",
                  color="Remaining")

fig2.update_traces(marker=dict(size=12,
                               line=dict(width=2,
                                         color='black')),
                   selector=dict(mode='markers'))

layout = html.Div(children=[
    html.Br(),
    html.H2(children='Counties by Ballots Issued and Ballots Returned (log)',
            style={'textAlign': 'center'}),
    dcc.Graph(id='issued-returned', figure=fig),
    html.Br(),
    html.H2(children='Same Graph, Unlogged, Reference',
            style={'textAlign': 'center'}),
    dcc.Graph(id='returned-issued', figure=fig2)
])
