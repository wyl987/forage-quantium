from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# initialize dash
app = Dash(__name__)

# load in data
df = pd.read_csv('data/formatted_output.csv')
df = df.sort_values(by='date')

# create the visualization
fig = px.line(df, x='date', y='sales', title="Pink Morsel Sales")

app.layout = html.Div(
  children = [
    html.H1(children='Sales Data over time',
            style={
              'textAlign': 'center',
              'color': '#7FDBFF'
            }),
    
    dcc.Graph(
      id='visualization',
      figure=fig
    )
  ]
)



if __name__ == '__main__':
    app.run(debug=True)