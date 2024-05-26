import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
date_rng = pd.date_range(start='2023-01-01', end='2023-04-30', freq='D')
df = pd.DataFrame(date_rng, columns=['Date'])
df['Temperature'] = np.random.randint(20, 35, size=(len(date_rng)))
df['Humidity'] = np.random.randint(30, 50, size=(len(date_rng)))

# a) Plot the 'Temperature' and 'Humidity' on the same plot with different y-axes (left y-axis for 'Temperature' and right y-axis for 'Humidity').
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(df['Date'], df['Temperature'], 'g-')
ax2.plot(df['Date'], df['Humidity'], 'b-')

ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature', color='g')
ax2.set_ylabel('Humidity', color='b')
plt.title('Temperature and Humidity Over Time')

plt.show()
