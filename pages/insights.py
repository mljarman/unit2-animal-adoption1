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
            Shelter animals are near and dear to my heart. I adopted my dog, Crosby, when he was 2 months 
            old from a rescue who got him from a shelter in New Mexico that has a 98% kill rate. 
            There are thousands and thousands of animals all around the country that need homes and while 
            I knew choosing this as my project would by no means solve any problems I thought I could get 
            some better insights into what makes an animal “adoptable.”

            The dataset I used is from data.austintexas.gov and they keep an hourly updated database of 
            all the animals going into the shelter each day. Before getting started some of my initial 
            thoughts were:
            * Breed would be very important
            * Age would as well and the number of animals adopted in their older age would be low.
            * Fixed animals would have a higher percentage of adoption than those not fixed.
            * Maybe there would be a pattern depending on the time of year people adopted pets.
            
            …Pretty much every thing I assumed was incorrect. 

            Breed carried very little to no weight when it came to predicting adoption, nor did gender.
            However, below are the top 10 dog and cat breeds that most frequently come to the shelter.
            Some breeds, of dogs at least, fell into both the most highly adopted and least adopted which
            just illustrates that feature wasn't very important in this case.

            """
        ),
        # dog breeds visualization 
        html.Img(src='assets/dog breeds.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}), 
        # cat breeds visualization
        html.Img(src='assets/cat breeds.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
   dcc.Markdown(
        """
            There was some variation in the adoption numbers for different ages, which is shown below.
            It was refreshing to learn that there are still a large number of adopted animals that were
            11+ years old (the oldest being 22) I did bin the ages under 1 year and then over 11 years
            to make it more manageable.
       """
        ),
    # ages visualization:
        html.Img(src='assets/ages.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
    dcc.Markdown(
        """
            The biggest surprise came with discovering that although there were significantly larger
            numbers of fixed (neutered or spayed) animals that were adopted in the data, the overall percentage
            of animals adopted that were not fixed was higher. This counter-intuitive thinking can be further explained
            in the Process page along with additional information on features.

            It would be very interesting to conduct an experiment through Uplift Modeling with an animal shelter to see
            if various marketing techniques through social media and the community if advertisting certain dogs or cats that
            may not have the highest probability of being adopted would increase their probability of finding a home.
            That information wasn't available on this dataset but I think the potential is very much there.

            The biggest insight is of course that whenever possible, you should adopt!
            Shameless plug, this is Crosby
        """
    ),
    # shameless plug:
        html.Img(src='assets/crosby.png', 
                 className='img-fluid', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '60%'}),
    
    ],
)


layout = dbc.Row([column1])