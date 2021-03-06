# tab4.py builds two scatter plots for 
# counties by # Democratic ballots 
# Issued and Returned

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from data import dem_mail_county
from dash_app import colors

# Initialize Plotly Scatterplot
# Each county is a different bubble, and they are 
# Color-coded based on how many votes are remaining
# X-axis is log(Democratic Ballots Issued) and
# Y-axis is log(Democratic Ballots Returned)
fig = px.scatter(dem_mail_county, x="Issued", y="Returned",
                 opacity=0.7,
                 hover_name="County",
                 color="Remaining",
                 log_x=True, log_y=True)

fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='black')),
                  selector=dict(mode='markers'))

fig.update_layout(
    # font_family="Courier New",
    font_color=colors['text'],
#    title_font_family="Times New Roman",
    title_font_color=colors['text'],
    legend_title_font_color="green"
)

# Initialize Plotly Scatterplot
# Each county is a different bubble, and they are 
# Color-coded based on how many votes are remaining
# X-axis is Democratic Ballots Issued and
# Y-axis is Democratic Ballots Returned
fig2 = px.scatter(dem_mail_county, x="Issued", y="Returned",
                  opacity=0.7,
                  hover_name="County",
                  color="Remaining")

fig2.update_traces(marker=dict(size=12,
                               line=dict(width=2,
                                         color='black')),
                   selector=dict(mode='markers'))


# Finalize tab layout 
layout = html.Div(children=[
    html.Br(),
    html.H2(children='''Counties by Democratic Ballots Issued
                      and Democratic Ballots Returned (log)''',
            style={'textAlign': 'center', 'color': colors['text']}),
    dcc.Graph(id='issued-returned', figure=fig, style={
        'color': colors['text'],
        'backgroundColor': colors['background']
    }),
    html.Br(),
    html.H2(children='Same Graph, Unlogged, Reference',
            style={'textAlign': 'center'}),
    dcc.Graph(id='returned-issued', figure=fig2)],
    style={
        'paper_bgcolor': colors['background'],
        'color': colors['text']}
)
