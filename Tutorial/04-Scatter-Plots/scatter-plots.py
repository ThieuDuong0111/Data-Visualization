import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path of the file to read
candy_filepath = "Tutorial/candy.csv"

# Fill in the line below to read the file into a variable candy_data
candy_data = pd.read_csv(candy_filepath, index_col="id")

# Print the first five rows of the data
print(candy_data.head())

# Which candy was more popular with survey respondents:
# '3 Musketeers' or 'Almond Joy'?  (Please enclose your answer in single quotes.)
more_popular = '3 Musketeers'

# Which candy has higher sugar content: 'Air Heads'
# or 'Baby Ruth'? (Please enclose your answer in single quotes.)
more_sugar = 'Air Heads'

# Scatter plot showing the relationship between 'sugarpercent' and 'winpercent'
plt.figure(figsize=(8, 6))
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
# => The scatter plot does not show a strong correlation between the two variables. 
# Since there is no clear relationship between the two variables, this tells us that sugar content does not play a strong role in candy popularity.

# Scatter plot w/ regression line showing the relationship between 'sugarpercent' and 'winpercent'
plt.figure(figsize=(8, 6))
sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])

# Scatter plot showing the relationship between 'pricepercent', 'winpercent', and 'chocolate'
plt.figure(figsize=(8, 6))
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'], hue=candy_data['chocolate'])

# Scatter plot showing the relationship between 'chocolate' and 'winpercent'
plt.figure(figsize=(8, 6))
sns.swarmplot(x=candy_data['chocolate'], y=candy_data['winpercent'])

plt.show()