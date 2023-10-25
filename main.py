import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
data = pd.read_csv('antarcticaMass.csv')

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['YEAR'], data['MASS'], c=data['MASS 1-SIGMA UNCERTAINTY'], cmap='viridis', alpha=0.6)
plt.colorbar(label='MASS 1-SIGMA UNCERTAINTY')
plt.xlabel('Year')
plt.ylabel('Antarctic Mass')
plt.title('Scatter Plot of Antarctic Mass over Time')
plt.show()

# Create a heatmap
correlation_matrix = data.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
