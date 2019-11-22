import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Will an animal be adopted?
            Thousands of animals are brought to shelters every day across the country. Fortunately 
            many of them will be adopted, but a large number will not.
            This app will help to predict the probability a dog or cat will be adopted
            based on different traits gathered from data in the Austin, Texas area. 
            This app is purely for educational purposes but it would be interesting to see if shelters 
            could use it given more testing with incoming animals to perhaps take actions to help
            find certain animals their forever homes.
    
            """
        ),
        dcc.Link(dbc.Button('Predict Adoption', color='primary'), href='/predictions')
    ],
    md=4,
    align='center'
)


column2 = dbc.Col([html.Img(src='assets/dogs.png', className='img-fluid')
],
align='center'
)

layout = dbc.Row([column1, column2])