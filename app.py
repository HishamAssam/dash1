# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:22:54 2020

@author: Hisham
"""


import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div(
html.H1(children="Hello Dash!")
)

if __name__ == '__main__':
    app.run_server()