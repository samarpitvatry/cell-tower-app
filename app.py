import dash
from dash import dcc, html
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Apply Plotly's built-in dark theme
pio.templates.default = "plotly_dark"

# Load the data
density_data_path = 'UK_Cell_Tower_Density.csv'
combined_data_path = 'UK_Cell_Tower_Combined.csv'
density_data = pd.read_csv(density_data_path)
combined_data = pd.read_csv(combined_data_path)
combined_data['Created'] = pd.to_datetime(combined_data['Created'], unit='s')

# Creating the Construction Date Distribution by Year figure
construction_date_counts = combined_data['Created'].dt.year.value_counts().sort_index()
construction_date_fig = px.bar(x=construction_date_counts.index, y=construction_date_counts.values,
                               labels={'x': 'Date (Year)', 'y': 'Count (M)'},
                               color_discrete_sequence=['#b8f331'])

# Creating the Signal Range bar graph
combined_data['Log10 Range'] = np.log10(combined_data['Range'])
log_range_bins = np.linspace(combined_data['Log10 Range'].min(), combined_data['Log10 Range'].max(), 10)
log_range_labels = [f'{round(b, 2)}-{round(log_range_bins[i+1], 2)}' for i, b in enumerate(log_range_bins[:-1])]
combined_data['Log10 Range Bins'] = pd.cut(combined_data['Log10 Range'], bins=log_range_bins, labels=log_range_labels, right=False)
log_range_counts = combined_data['Log10 Range Bins'].value_counts().sort_index()
signal_range_fig = px.bar(x=log_range_counts.index, y=log_range_counts.values,
                          labels={'x': 'Count', 'y': 'Log10(Range)'},
                          color_discrete_sequence=['#750ed5'])

# Geographical Graph for Cell Tower Density
density_fig = px.density_mapbox(density_data, lat='Latitude_rounded', lon='Longitude_rounded', z='Density', radius=10,
                                center=dict(lat=53.8, lon=-3.4), zoom=5, mapbox_style="carto-darkmatter")

# Custom color palette for donut chart
donut_colors = ["#f8c34e", "#3b2858", "#fc5434", "#bf8a6e"]
# Donut Chart for the "Radio Type" distribution
radio_type_counts = combined_data['Radio Type'].value_counts()
radio_type_fig = px.pie(values=radio_type_counts.values, names=radio_type_counts.index, hole=0.3, color_discrete_sequence=donut_colors)

# Define the layout of the app
app = dash.Dash(__name__)
server = app.server  # Required for Heroku deployment
app.layout = html.Div([
    html.H1("UK Cell Tower Dashboard", style={'background-color': 'black', 'color': 'white', 'font-family': 'Arial', 'text-align': 'center', 'margin': '20px', 'font-weight': 'bold'}),
    dcc.Graph(figure=density_fig, style={'background-color': 'black', 'color': 'white', 'height': '900px', 'margin-top': '-10px'}),
    html.H2("Distribution of Radio Type", style={'background-color': 'black', 'color': 'white', 'font-family': 'Arial', 'text-align': 'center', 'font-weight': 'normal'}),
    dcc.Graph(figure=radio_type_fig, style={'background-color': 'black', 'color': 'white', 'height': '600px'}),
    html.Div([
        html.Div([
            html.H2("Construction Date", style={'background-color': 'black', 'color': 'white', 'font-family': 'Arial', 'text-align': 'center', 'font-weight': 'normal'}),
            dcc.Graph(figure=construction_date_fig, style={'background-color': 'black', 'color': 'white', 'height': '500px'})
        ], style={'background-color': 'black', 'color': 'white', 'width': '50%', 'display': 'inline-block'}),
        html.Div([
            html.H2("Signal Range", style={'background-color': 'black', 'color': 'white', 'font-family': 'Arial', 'text-align': 'center', 'font-weight': 'normal'}),
            dcc.Graph(figure=signal_range_fig, style={'background-color': 'black', 'color': 'white', 'height': '500px'})
        ], style={'background-color': 'black', 'color': 'white', 'width': '50%', 'display': 'inline-block'})
    ], style={'background-color': 'black', 'color': 'white', 'display': 'flex', 'justify-content': 'space-around'}),
], style={'background-color': 'black', 'color': 'white', 'padding': '20px'})

if __name__ == '__main__':
    app.run_server(debug=True)
