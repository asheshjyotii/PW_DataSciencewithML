import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = np.random.randn(1000)

# a) Plot a histogram of the data with 30 bins.
count, bins, ignored = plt.hist(data, 30, density=True)

# b) Overlay a line plot representing the normal distribution's probability density function (PDF).
pdf = (1/(np.sqrt(2 * np.pi))) * np.exp(-(bins**2) / 2)
plt.plot(bins, pdf, linewidth=2, color='r')
plt.xlabel('Value')
plt.ylabel('Frequency/Probability')
plt.title('Histogram with PDF Overlay')
plt.show()
