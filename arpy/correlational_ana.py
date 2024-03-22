import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('arduino_data.csv')

temperature_data = data['Temperature'].values
light_intensity_data = data['Light Intensity'].values
humidity_data = data['Humidity'].values

correlation_coefficient = np.corrcoef(temperature_data, light_intensity_data)[0, 1]
correlation_coefficient = np.corrcoef(humidity_data, light_intensity_data)[0, 1]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(temperature_data, light_intensity_data, color='blue')
plt.title('Temperature vs Light Intensity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Light Intensity')
plt.grid(True)
plt.savefig('data_collec/correlational_analysis/temperature_light_intensity_plot.png')

plt.subplot(1, 2, 2)
plt.scatter(humidity_data, light_intensity_data, color='green')
plt.title('Humidity vs Light Intensity')
plt.xlabel('Humidity (%)')
plt.ylabel('Light Intensity')
plt.grid(True)
plt.savefig('data_collec/correlational_analysis/humidity_light_intensity_plot.png')

if correlation_coefficient > 0:
    print("There is a positive correlation between temperature and light intensity.")
elif correlation_coefficient < 0:
    print("There is a negative correlation between temperature and light intensity.")
else:
    print("There is no significant correlation between temperature and light intensity.")

if correlation_coefficient > 0:
    print("There is a positive correlation between humidity and light intensity.")
elif correlation_coefficient < 0:
    print("There is a negative correlation between humidity and light intensity.")
else:
    print("There is no significant correlation between humidity and light intensity.")