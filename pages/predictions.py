# Imports from 3rd party libraries
import dash
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd

# Imports from this application
from app import app
pipeline = load('assets/mypipeline.joblib')
all_options = {
            0 : ['Domestic Shorthair Mix', 'Domestic Longhair Mix', 'Manx Mix', 'Siamese Mix', 'Pit Bull Mix'],
            1 : ['Border Collie Mix', 'Boxer Mix', 'Chihuahua Shorthair Mix', 'Labrador Retriever Mix']
        }
breed_vals = {
            'Australian Cattle Dog Mix': 20,
            'Border Collie Mix': 17,
            'Boxer Mix': 22,
            'Chihuahua Shorthair Mix': 5,
            'Domestic Shorthair Mix': 76,
            'Domestic Longhair Mix': 78,
            'Labrador Retriever Mix': 8,
            'Manx Mix': 84,
            'Pit Bull Mix': 21,
            'Siamese Mix': 81,
}



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        # Animal Type dropdown (Dog, Cat)
        dcc.Markdown('##### What type of animal?'),
        dcc.Dropdown(
            id='animal_type', 
            options= [
                {'label': 'Dog', 'value': 1},
                {'label': 'Cat', 'value': 0},
            ],
            className = 'mb-3',
            value=0,
            placeholder='Select an animal'
        ),
    # Gender dropdown menu
        dcc.Markdown('##### Gender'), 
        dcc.Dropdown(
            id='gender', 
            options= [
                {'label': 'Male', 'value': 1},
                {'label': 'Female', 'value': 2},
            ],
            className = 'mb-3',
            value=1,
            placeholder='Select a gender'
        ), 
    # Fixed dropdown (Yes, No)
        dcc.Markdown('##### Fixed?'), 
        dcc.Dropdown(
            id='fixed_Fixed', 
            options= [
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0},
            ],
            className = 'mb-3',
            value=1,
            placeholder='Select yes or no'
        ), 
     # Age
        html.Div(  
            [
        dcc.Markdown('##### Age (years)'), 
        daq.Slider(              
            id='age', 
            min=.5, 
            max=11, 
            step=None,  
            marks={
                .5: '.5',
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8',
                9: '9',
                10: '10',
                11: '11+'
                }, 
            value=5,
            className='mb-4',
            handleLabel={
                'label': 'Current',
                'showCurrentValue': True
                },
            ),
            ],
            style={'marginTop': 15, 'marginBottom': 15},            
        ),
        dcc.Markdown('##### Color'), 
        dcc.Dropdown(
            id='color', 
            options= [
                {'label': 'Black', 'value': 17},
                {'label': 'Black/White', 'value': 3},
                {'label': 'Brown', 'value': 10},
                {'label': 'Brown/White', 'value': 6},
                {'label': 'Brown Tabby', 'value': 54},
                {'label': 'Calico', 'value': 49},
                {'label': 'Orange Tabby', 'value': 52},
                {'label': 'Tan', 'value': 2},
                {'label': 'Tan/White', 'value': 18},
                {'label': 'White', 'value': 20},
            ],
            className = 'mb-3',
            value=1,
            placeholder='Select a color' 
        ),
       dcc.Markdown('##### Breed'), 
        dcc.Dropdown(
            id='breed', 
            # options= [
            #     {'label': 'Australian Cattle Dog Mix', 'value': 20},
            #     {'label': 'Border Collie Mix', 'value': 17},
            #     {'label': 'Boxer Mix', 'value': 22},
            #     {'label': 'Chihuahua Shorthair Mix', 'value': 5},
            #     {'label': 'Domestic Shorthair Mix', 'value': 76},
            #     {'label': 'Domestic Longhair Mix', 'value': 78},
            #     {'label': 'Labrador Retriever Mix', 'value': 8},
            #     {'label': 'Manx Mix', 'value': 84},
            #     {'label': 'Pit Bull Mix', 'value': 21},
            #     {'label': 'Siamese Mix', 'value': 81},
            # ],
            className = 'mb-3',
            value=1,
            placeholder='Select a breed'
        ),  
        html.Div(  
            [
        dcc.Markdown('##### Season Arrived'), 
        daq.Slider(              
            id='season_arrived', 
            min=1, 
            max=4, 
            step=None,  
            marks={
                4: 'Spring',
                3: 'Summer',
                2: 'Fall',
                1: 'Winter',
                }, 
            value=3,
            className='mb-4',
            handleLabel={
                'label': 'Current',
                'showCurrentValue': False
                },
            ),
            ],
            style={'marginTop': 15, 'marginBottom': 15},            
        ),         
    ],
    md = 6,
)

 
column2 = dbc.Col(
    [
        html.H2('Probability of Adoption', className= 'mb-3'),
        html.Div(id='prediction-content', className='lead'),
        html.Div(id='image')
    ],
    md=6,
)
layout = dbc.Row([column1, column2])
@app.callback(
    Output('prediction-content', 'children'),
    [
    Input('animal_type', 'value'),
    Input('gender', 'value'),
    Input('fixed_Fixed', 'value'),
    Input('age', 'value'),
    Input('color', 'value'),
    Input('breed', 'value'),
    Input('season_arrived', 'value')
    ],
)
def predict(animal_type, gender, fixed_Fixed, age, color, breed, season_arrived):
    df = pd.DataFrame(
        columns=['animal_type', 'breed', 'color', 'season_arrived', 'age', 'fixed_Fixed', 'gender'],
        data=[[animal_type, breed, color, season_arrived, age, fixed_Fixed, gender]]
    )
    y_pred=pipeline.predict(df)[0]
    if y_pred == 'Adopted':
        y_pred_proba = pipeline.predict_proba(df)[0][0]
        return f'{y_pred_proba*100:.0f}% chance of {y_pred}'
    else:
        y_pred_proba = pipeline.predict_proba(df)[0][1]
        return f'{y_pred_proba*100:.0f}% chance of {y_pred}',
# trying to show an image of a dog if they select animal_type as dog and 
# then with cat if they select cat.
@app.callback(
    Output('image', 'children'),
    [Input('animal_type', 'value')],
)
def change_image(animal_type):
    if animal_type == 1:
        return html.Img(src='assets/dog.png', className='img-flud', style={'height': '400px'})
    else:
        return html.Img(src='assets/cat.png', className='img-flud', style={'height': '400px'})

@app.callback(
    [Output('breed', 'options')],
    [Input('animal_type', 'value')]
)
#This method generates a list of options for the breed selection dropdown
#It selects the animal from the all_options dict, then makes an option
#for each of the breeds in the list.
def gen_options(animal_type):
    opts = [{'label': i, 'value' : breed_vals[i]} for i in all_options[animal_type]]
    return [opts]