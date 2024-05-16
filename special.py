import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

years = list(range(2003, 2023))
temperature_anomalies = [0.56, 0.58, 0.62, 0.64, 0.67, 0.70, 0.75, 0.79, 0.84, 0.87, 0.90, 0.94, 0.98, 1.02, 1.06, 1.10, 1.15, 1.19, 1.22, 1.25]

colors = sns.color_palette("coolwarm", len(years))

fig, ax = plt.subplots(figsize=(10, 6))
for i in range(len(years) - 1):
    ax.plot(years[i:i+2], temperature_anomalies[i:i+2], color=colors[i], marker='o')

sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=plt.Normalize(vmin=min(years), vmax=max(years)))
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, ticks=np.linspace(min(years), max(years), len(years)//2 + 1))
cbar.set_label('Year')

ax.set_title('Global Temperature Anomalies (2003-2022)')
ax.set_xlabel('Year')
ax.set_ylabel('Temperature Anomaly (°C)')
ax.grid(True)
plt.show()
