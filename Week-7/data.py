import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Loads the Iris dataset
try:
    iris = load_iris()
    iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], 
                          columns=iris['feature_names'] + ['target'])
    
    # Displays the first few rows
    print("First 5 rows of the dataset:")
    print(iris_df.head())
    
    # Explores the structure
    print("\nDataset information:")
    print(iris_df.info())
    
    # Checks for missing values
    print("\nMissing values per column:")
    print(iris_df.isnull().sum())
    
    # Cleans the dataset
    iris_df_clean = iris_df.dropna()  
    
    # Maps target to species names for better readability
    iris_df_clean['species'] = iris_df_clean['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
except Exception as e:
    print(f"An error occurred: {e}")



# Basic statistics
print("\nBasic statistics of numerical columns:")
print(iris_df_clean.describe())

# Group by species and compute mean measurements
print("\nMean measurements by species:")
species_stats = iris_df_clean.groupby('species').mean()
print(species_stats)

# Interesting findings
print("\nInteresting findings:")
print("- Setosa has significantly smaller petal measurements than other species")
print("- Virginica has the largest measurements across all features")
print("- Versicolor is intermediate between setosa and virginica")


# Set style for better looking plots
sns.set(style="whitegrid")
plt.figure(figsize=(15, 10))

# 1. Line chart (simulating trends over time by using index as pseudo-time)
plt.subplot(2, 2, 1)
for species in iris_df_clean['species'].unique():
    subset = iris_df_clean[iris_df_clean['species'] == species]
    plt.plot(subset.index, subset['sepal length (cm)'], label=species)
plt.title('Sepal Length Trend by Species (Index as Pseudo-Time)')
plt.xlabel('Observation Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()

# 2. Bar chart - average petal length per species
plt.subplot(2, 2, 2)
sns.barplot(x='species', y='petal length (cm)', data=iris_df_clean, estimator=np.mean)
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')

# 3. Histogram - distribution of sepal width
plt.subplot(2, 2, 3)
sns.histplot(data=iris_df_clean, x='sepal width (cm)', hue='species', kde=True)
plt.title('Distribution of Sepal Width by Species')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Count')

# 4. Scatter plot - sepal length vs petal length
plt.subplot(2, 2, 4)
sns.scatterplot(data=iris_df_clean, x='sepal length (cm)', y='petal length (cm)', 
                hue='species', style='species', s=100)
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.tight_layout()
plt.show()


