import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path of the file to read
fifa_filepath = "Tutorial/fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)

plt.show()