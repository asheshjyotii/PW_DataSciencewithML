import plotly.graph_objects as go
import numpy as np

# Generate a random dataset
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.random.rand(100)

# Create the Plotly line plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Random Data'))

# Add labels to the axes and set the title
fig.update_layout(
    title='Simple Line Plot',
    xaxis_title='X-axis',
    yaxis_title='Y-axis'
)

# Show the plot
fig.show()
