import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hits_df = pd.read_csv("hits.csv")
misses_df = pd.read_csv("miss.csv")
x = hits_df.set_index('Latency(cycles)')['Hits-Count']
y = misses_df.set_index('Latency(cycles)')['Miss-Count']

bins = np.linspace(0, 400, 401)

plt.hist(x.index, bins, weights=x, alpha=0.5, color='green', label='Hits')
plt.hist(y.index, bins, weights=y, alpha=0.5,  color='red', label='Misses')
plt.xlabel('Latency (cycles)')
plt.ylabel('Count')
plt.title('Cache Hits and Misses Histogram')
plt.xticks(np.arange(0, 401, 20))
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout() 
plt.show()