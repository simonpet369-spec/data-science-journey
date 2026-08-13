"""
water_potability.py
Exploring and analysing water quality data to determine
what factors influence whether water is safe to drink.

Dataset source: Kaggle Water Quality dataset
Author: Simon
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('water_potability.csv')

# First Look
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

# Find the Mess
print(df.isnull().sum())

df['ph'] = df['ph'].fillna(df['ph'].mean())
df['Sulfate'] = df['Sulfate'].fillna(df['Sulfate'].mean())
df['Trihalomethanes'] = df['Trihalomethanes'].fillna(df['Trihalomethanes'].mean())
# Confriming missing value
print(df.isnull().sum())


# Phase B
print(df['Potability'].mean())
print((df.groupby('Potability')['ph'].mean()))
print(df.groupby('Potability')['Hardness'].mean())
print(df.groupby('Potability')['Sulfate'].mean())

for col in ['Chloramines', 'Solids', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']:
    print(df.groupby('Potability')[col].mean())

correlation = df.corr()['Potability'].sort_values(ascending=False)
print(correlation)

# Chart 1
df['Potability'].value_counts().plot(kind='bar', color='blue')
plt.title('Water Potability Count (0=Not Safe, 1=Safe)')
plt.xlabel('Potability')
plt.ylabel('Count')
plt.savefig('potability_count.png', dpi=150, bbox_inches='tight')
plt.show()

# Chart 2
correlation.plot(kind='bar', color='purple')
plt.title('Correlation of Each Feature with Potability')
plt.xlabel('Feature')
plt.ylabel('Correlation')
plt.savefig('potability_correlation.png', dpi=150, bbox_inches='tight')
plt.show()