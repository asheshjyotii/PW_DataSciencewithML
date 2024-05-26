from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
import numpy as np
import pandas as pd

# Generate random categorical data
categories = ['A', 'B', 'C', 'D', 'E', 'F']
values = np.random.randint(1, 100, size=len(categories))

# Create a DataFrame
data = pd.DataFrame({'categories': categories, 'values': values})

# Create a ColumnDataSource
source = ColumnDataSource(data)

# Create a Bokeh figure
p = figure(x_range=categories, title="Random Categorical Bar Chart",
           toolbar_location=None, tools="")

# Add a bar chart
p.vbar(x='categories', top='values', width=0.9, source=source,
       legend_field='categories', line_color='white',
       fill_color=factor_cmap('categories', palette=Spectral6, factors=categories))

# Add hover tooltips
hover = HoverTool()
hover.tooltips = [("Category", "@categories"), ("Value", "@values")]
p.add_tools(hover)

# Label the axes
p.xaxis.axis_label = "Categories"
p.yaxis.axis_label = "Values"

# Customize the legend
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

# Output to a static HTML file
output_file('random_categorical_bar_chart.html')

# Show the results
show(p)
