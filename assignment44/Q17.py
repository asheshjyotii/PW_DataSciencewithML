import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate two random arrays
x = np.random.uniform(-10, 10, 100)
y = np.random.uniform(-10, 10, 100)

# Determine the quadrant for each point
def get_quadrant(x, y):
    if x > 0 and y > 0:
        return 'Q1'
    elif x < 0 and y > 0:
        return 'Q2'
    elif x < 0 and y < 0:
        return 'Q3'
    elif x > 0 and y < 0:
        return 'Q4'

quadrants = [get_quadrant(xi, yi) for xi, yi in zip(x, y)]

# Create a DataFrame
df = pd.DataFrame({'x': x, 'y': y, 'quadrant': quadrants})

# Create a Seaborn scatter plot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(data=df, x='x', y='y', hue='quadrant', palette='Set1')

# Add labels, legend, and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Quadrant-wise Scatter Plot')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend(title='Quadrant')
plt.show()
