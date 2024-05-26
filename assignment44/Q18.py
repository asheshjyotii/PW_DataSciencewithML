from bokeh.plotting import figure, show, output_file
import numpy as np

# Generate data for sine wave
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

# Create a Bokeh plot
p = figure(title='Sine Wave Function', x_axis_label='x', y_axis_label='y')

# Plot the sine wave
p.line(x, y, legend_label='Sine', line_width=2)

# Add grid lines
p.xgrid.grid_line_color = 'blue'
p.ygrid.grid_line_color = 'green'

# Output to a static HTML file
output_file('sine_wave.html')

# Show the results
show(p)
