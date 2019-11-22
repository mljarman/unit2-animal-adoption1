# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        For this project I started out with data exploration which was fairly straight forward. I 
        decided to focus on only cats and dogs for this project although the data included livestock,
        birds, and even bats! (But it is Austin) I was able to remove missing values for the pertinent
        data through feature engineering.

        In particular, there were a few missing ages but strangely the date of birth was not missing
        any values. Odd for strays but I felt calculating the age based on the DOB was better than 
        simply dropping those observations or imputing with the mean.

        After cleaning up the data I tried both a Random Forest Classifier and a Logistic Regression model
        since this is a classification problem (will an animal be adopted, or not). I used the Majority Class
        as my baseline which was that 55% of animals would be adopted given no additional features.

        I performed a 3 way split based on years the data was collected and beat the baseline with my 
        validation set with an accuracy score of 85% with the Random Forest Classifier using a pipeline
        that included ordinal encoding since the majority of my features are categorical.

        Below are the permutation importances are the features. Initially I thought the features would be
        somewhat equally distributed, however, as mentioned in the Insights page, the most important
        feature in making these predictions is whether or not an animal is fixed.
        """
        ),
        # PDP plots visualization:
        html.Img(src='assets/pdp fixed.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
                # PDP plots visualization:
        html.Img(src='assets/pdp gender.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
                # PDP plots visualization:
        html.Img(src='assets/pdp age.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
                # PDP plots visualization:
        html.Img(src='assets/pdp season.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),

        dcc.Markdown(
        """
        I've also included several Partial Dependence Plots to demonstrate how a feature affects 
        predictions of a machine learning model. 
        """
        ),
    # permutation importances visualization:
        html.Img(src='assets/permutations.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
        dcc.Markdown(
        """
        The accuracy score for my test set came in at 87% which would mean my predictive model correctly
        identified 87% of dogs and cats that were adopted in this data set.

        To gain further insights into how the different features impacted my predictions, I created Shapley
        values on two examples: 
        * 1. A cat that was correctly predicted to be adopted and was:
        """
        ),
        # shapley visualization:
        html.Img(src='assets/correctshapley.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
         dcc.Markdown(
             """
        * 2. A dog that was unfortunately predicted to be adopted and wasn't:
             """
         ),
         # shapley visualization:
        html.Img(src='assets/wrongshapley.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}), 
        dcc.Markdown(
        """
        Each example interacts with the features differently. The first's young age helped
        the probability and most importantly (in each example) is that not being fixed worked against
        as well as the breed and it being a cat.

        In the second example the age was still young but lowered the probability and then being fixed,
        a dog, and the breed helped but unfortunately this animal was still not adopted.
        """
        ),                

    ],
)

layout = dbc.Row([column1])