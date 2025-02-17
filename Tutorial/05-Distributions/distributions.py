import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path of the files to read
cancer_filepath = "Tutorial/cancer.csv"

# Fill in the line below to read the file into a variable cancer_data
cancer_data = cancer_data = pd.read_csv(cancer_filepath, index_col="Id")

# Print the first five rows of the data
print(cancer_data.head())

# Histograms for benign and maligant tumors
plt.figure(figsize=(8, 6))
sns.histplot(data=cancer_data, x='Area (mean)', hue='Diagnosis')

# KDE plots for benign and malignant tumors
plt.figure(figsize=(8, 6))
sns.kdeplot(data=cancer_data, x='Radius (worst)', hue='Diagnosis', fill=True)

plt.show()