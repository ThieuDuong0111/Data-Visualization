import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path of the file to read
spotify_filepath = "Tutorial/spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Change the style of the figure
sns.set_style("darkgrid")

# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)

plt.show()



