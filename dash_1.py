# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:52:12 2020

@author: Hisham
"""
# =============================================================================
# https://anaconda.org/conda-forge/dash
# conda install -c conda-forge dash
# https://anaconda.org/conda-forge/dash-core-components
# conda install -c conda-forge dash-core-components
# https://anaconda.org/conda-forge/dash-html-components
# conda install -c conda-forge dash-html-components
# =============================================================================
import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div(
html.H1(children="Hello Dash!")
)

app.run_server(debug=True, use_reloader=False)
    


app.layout = html.Div([
    html.H1("Hello Dash!"),
    html.P("Let's add an ordered list"),
    html.Ol([
        html.Li("Item one"), html.Li("Item two"), html.Li("Item three")
        ])
])



app.layout = html.Div([
    html.Label('Select a country:'),
    dcc.Dropdown(
        options=[
            {'label': 'United Kingdom', 'value': 'GBR'},
            {'label': 'United States', 'value': 'USA'},
            {'label': 'France', 'value': 'FRA'}
        ],
        value='GBR'
    )
])

app.layout = html.Div([
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'United Kingdom', 'value': 'GBR'},
            {'label': 'United States', 'value': 'USA'},
            {'label': 'France', 'value': 'FRA'}
        ],
        value=['GBR', 'FRA'],
        multi=True
    ),
    dcc.DatePickerRange()
])


app.layout = html.Div([
    html.Label('Text Input'),
    dcc.Input(value='', type='text'),
    html.Label('Num Input '),
    dcc.Input(value='0', type='number'),
    
    html.Br(),html.Br(),
    dcc.Slider(
        min=0, max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5
    ),
    
    
    html.Br(),
    dcc.DatePickerSingle(),
    html.Br(),
    dcc.DatePickerRange(),
    
    
])



app.layout = html.Div([
    dcc.DatePickerSingle(),
    html.Br(),
    dcc.DatePickerRange(),
    html.Br(),
    dcc.Slider(
        min=0, max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5
    )
])

app.run_server(debug=True, use_reloader=False)
    






    
    
import dash
import dash_core_components as dcc
import dash_html_components as html
import webbrowser

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.H1(children='one'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

from threading import Timer

if __name__ == '__main__':
    Timer(1, webbrowser.open_new('http://127.0.0.1:8050/')).start();
    app.run_server(debug=True, use_reloader=False)
    
    
    
    
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),

    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5,
    ),
], style={'columnCount': 2})

if __name__ == '__main__':
    Timer(1, webbrowser.open_new('http://127.0.0.1:8050/')).start();
    app.run_server(debug=True, use_reloader=False)
        


print("ddddd")



import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app.layout = html.Div([
    dcc.Input(id='num1', value='0', type='number'),
    html.Div(id='out1'),    
])

@app.callback(
    Output(component_id='out1', component_property='children'),
    [Input(component_id='num1', component_property='value')]
)
def calc(val):
    if (val==None):
        return 0
    else:
        return int(val)*int(val)
app.run_server(debug=True, use_reloader=False)

# =============================================================================
# tips example1
# =============================================================================
import seaborn as sn; import plotly.express as px
import dash; import dash_core_components as dcc
import dash_html_components as html; from dash.dependencies import Input, Output
app = dash.Dash()
tips=sn.load_dataset("tips")
fig = px.scatter(tips, x="total_bill", y="tip")

app.layout = html.Div([
  dcc.RadioItems(id="gender1", options=[{'label': 'Female', 'value': 'Female'},{'label': 'Male', 'value': 'Male'}], value='Female'),
  dcc.Graph(id="fig1", figure=fig)])

@app.callback(Output('fig1', 'figure'),[Input('gender1', 'value')])
def updateGender(g):
    return  px.scatter(tips.query("sex=='"+g+"'"), x="total_bill", y="tip")
app.run_server(debug=True, use_reloader=False)



# =============================================================================
# tips example1-1
# =============================================================================
import seaborn as sn
import plotly.express as px
from dash.dependencies import Input, Output
app = dash.Dash()
tips=sn.load_dataset("tips")
fig = px.scatter(tips, x="total_bill", y="tip")

app.layout = html.Div([
  dcc.RadioItems(id="gender1",
               options=[{'label': 'Both', 'value': 'all'},{'label': 'Female', 'value': 'Female'},{'label': 'Male', 'value': 'Male'}], value='all'),
  dcc.Graph(id="fig1", figure=fig)])

@app.callback(Output('fig1', 'figure'),[Input('gender1', 'value')])
def updateGender(g):
    if g=="all":
        return fig
    else:
        return  px.scatter(tips.query("sex=='"+g+"'"), x="total_bill", y="tip")
app.run_server(debug=True, use_reloader=False)



# =============================================================================
# tips example2
# =============================================================================
import seaborn as sn
import plotly.express as px
from dash.dependencies import Input, Output
tips=sn.load_dataset("tips")
fig = px.scatter(tips, x="total_bill", y="tip")
app = dash.Dash()
app.layout = html.Div([
  dcc.RadioItems(id="gender1",
               options=[{'label': 'Both', 'value': 'both'},{'label': 'Female', 'value': 'Female'},{'label': 'Male', 'value': 'Male'}], value='both'), 
  html.Br(),html.Br(),html.Label("select day"),
  dcc.Dropdown(id="day1", options=[{'label': 'All', 'value': 'All'},{'label': 'Thur', 'value': 'Thur'},{'label': 'Fri', 'value': 'Fri'},
            {'label': 'Sat', 'value': 'Sat'},{'label': 'Sun', 'value': 'Sun'}], value='All'),
  dcc.Graph(id="fig1",figure=fig)])

@app.callback(Output('fig1', 'figure'),[Input('gender1', 'value'),Input('day1', 'value')])
def updatefig(g,d):
    if g=="both" and d=="All":
        return fig1
    elif g=="both" and d!="All":
        return  px.scatter(tips.query("day=='"+d+"'"), x="total_bill", y="tip")
    elif g!="both" and d=="All":
        return  px.scatter(tips.query("sex=='"+g+"'"), x="total_bill", y="tip")
    else:
        return  px.scatter(tips.query("sex=='"+g+"' & day=='"+d+"'"), x="total_bill", y="tip")

#@app.callback(Output('fig1', 'figure'), [Input('day1', 'value')])
#def updateDay(d):
 #   return  px.scatter(tips.query("day=='"+d+"'"), x="total_bill", y="tip")
app.run_server(debug=True, use_reloader=False)


#============


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



import dash_core_components as dcc
import plotly.express as px

df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")



app = dash.Dash()
app.layout = html.Div([
dcc.Graph(
    figure=fig
    )
 ])
app.run_server(debug=True, use_reloader=False)
