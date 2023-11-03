# Importing Modules
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd

# Reading the DataFrame from a CSV file
seeds_df = pd.read_csv("seeds-less-rows.csv")

# Remove the grain species from the DataFrame and save it for later
varieties = list(seeds_df.pop('grain_variety'))

# Extract the measurements as a NumPy array
samples = seeds_df.values

# Perform hierarchical clustering on samples using the linkage() function with the method='complete' keyword argument.
mergings = linkage(samples, method='complete')

# Plot a dendrogram using the dendrogram() function on mergings, specifying the keyword arguments labels=varieties, leaf_rotation=90, and leaf_font_size=6.
dendrogram(mergings, labels=varieties, leaf_rotation=90, leaf_font_size=6)

# Display the dendrogram
plt.show()
