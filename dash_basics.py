"""
Let's start creating dash application
Goal
Create a dashboard that displays the percentage of flights running under specific distance group. Distance group is the distance intervals, every 250 miles, for flight segment. If the flight covers to 500 miles, it will be under distance group 2 (250 miles + 250 miles).

Expected Output
Below is the expected result from the lab. Our dashboard application consists of three components:

Title of the application
Description of the application
Chart conveying the proportion of distance group by month


To do:
Import required libraries and read the dataset
Create an application layout
Add title to the dashboard using HTML H1 component
Add a paragraph about the chart using HTML P component
Add the pie chart above using core graph component
Run the app

Run the following commands on the terminal 
python3.8 -m pip install packaging
python3.8 -m pip install pandas dash
pip3 install httpx==0.20 dash plotly

"""
"""
TASK 1 - Data Preparation
Let’s start with

Importing necessary libraries
Reading and sampling 500 random data points
Get the chart ready
"""

# Import required packages
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

"""
TASK 2 - Create dash application and get the layout skeleton

Next, we create a skeleton for our dash application. Our dashboard application has three components as seen before:

Title of the application
Description of the application
Chart conveying the proportion of distance group by month
Mapping to the respective Dash HTML tags:

Title added using html.H1() tag
Description added using html.P() tag
Chart added using dcc.Graph() tag
"""
# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1(),
                                html.P(),
                                dcc.Graph(),
                                               
                    ])

# Run the application                   
if __name__ == '__main__':
    app.run_server()
"""
TASK 3 - Add the application title
Update the html.H1() tag to hold the application title.

Application title is Airline Dashboard
Use style parameter provided below to make the title center aligned, with color code #503D36, and font-size as 40


TASK 4 - Add the application description
Update the html.P() tag to hold the description of the application.

Description is Proportion of distance group (250 mile distance interval group) by flights.
Use style parameter to make the description center aligned and with color #F57241.

TASK 5 - Update the graph
Update figure parameter of dcc.Graph() component to add the pie chart.
 We have created pie chart and assigned it to fig. 
 Let’s use that to update the figure parameter.
"""
# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig),
                                               
                    ])

# Run the application                   
if __name__ == '__main__':
    app.run_server()



figure=fig

""" 
AFTER YOU RUN THE CODE, YOU WILL FIRST SEE THIS MESSAGE ON THE TERMINAL 
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8050
Press CTRL+C to quit" 

NAVIGATE TO 'LAUNCH APPLICATION ON THE SIDE MENU, PROVIDE PORT NUMBER (in this case 8050) THEN PRESS OK
The app wil open in a new browser tab 

"""

""" 
below is the Entire script
 
 # Import required packages
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig),
                                               
                    ])

# Run the application                   
if __name__ == '__main__':
    app.run_server()

    """