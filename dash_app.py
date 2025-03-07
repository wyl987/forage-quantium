from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

# initialize dash
app = Dash(__name__)

# load in data
df = pd.read_csv('data/formatted_output.csv')
df = df.sort_values(by='date')

app.layout = html.Div(
  children = [
    html.H1(
      children='Sales Data over time',
      style={
        'textAlign': 'center',
        'color': '#6A1B9A',  # Deep purple color
        'font-family': 'Arial, sans-serif',
        'font-size': '36px',
        'margin-bottom': '30px'
    }),
    dcc.RadioItems(
      options=[
        {'label': 'North', 'value': 'north'},
        {'label': 'East', 'value': 'east'},
        {'label': 'South', 'value': 'south'},
        {'label': 'West', 'value': 'west'},
        {'label': 'All', 'value': 'all'}
      ],
      value='all',
      style={
        'padding': '10px',
        'display': 'flex',
        'justify-content': 'center',
        'color': '#6A1B9A',  # Deep purple text color
        'font-family': 'Arial, sans-serif',
        'font-size': '18px',
        'border-radius': '5px',
        'background-color': '#E1BEE7',  # Light purple background
        'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)',
        'width': '300px',
        'margin-bottom': '20px'
      },
      id="region-selector"),
    
    dcc.Graph(
      id='visualization',
      style={
        'margin-top': '20px',
        'padding': '20px',
        'border-radius': '10px',
        'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)',
      }
    )
  ]
)

@callback(
  Output('visualization', 'figure'),
  Input('region-selector', 'value')
)
def update_graph(selected_region):
  filtered_df = df if selected_region == 'all' else df[df['region'] == selected_region]
  # create the visualization
  fig = px.line(filtered_df, x='date', y='sales', title="Pink Morsel Sales")
  fig.update_layout(
    transition_duration=500,
    title_font=dict(size=24, color='#6A1B9A'), 
    plot_bgcolor='#F3E5F5',  
    paper_bgcolor='#F3E5F5',  
    xaxis_title="Date",
    yaxis_title="Sales",
    yaxis=dict(color='#6A1B9A'),     
    font=dict(
        family="Arial, sans-serif",
        color="#6A1B9A" 
    ),
  )
  
  return fig



if __name__ == '__main__':
    app.run(debug=True)