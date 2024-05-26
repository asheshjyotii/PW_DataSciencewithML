import plotly.graph_objects as go
import numpy as np

# Generate random data for the pie chart
np.random.seed(42)
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = np.random.randint(10, 100, size=len(categories))

# Create the Plotly pie chart
fig = go.Figure(data=[go.Pie(labels=categories, values=values, hole=0.3, textinfo='label+percent', insidetextorientation='radial')])

# Set the title
fig.update_layout(title_text='Interactive Pie Chart')

# Show the plot
fig.show()
