"""
water_potability.py
Exploring and analysing water quality data to determine
what factors influence whether water is safe to drink.

Dataset source: Kaggle Water Quality dataset
Author: Simon
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Part 1 - Load and Inspect
# ---------------------------------------------------------
df = pd.read_csv('water_potability.csv')

print("--- Shape and First Look ---")
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())
# Three columns have real missing data: ph (491), Sulfate (781),
# Trihalomethanes (162). None are unique identifiers (unlike
# Titanic's Cabin) - all are genuine numeric water measurements,
# so filling them is the right call rather than dropping.


# ---------------------------------------------------------
# Part 2 - Cleaning
# ---------------------------------------------------------
# Mean is used here rather than median since these are natural
# chemical measurements without dataset-specific outliers skewing
# the average (unlike, for example, a small sample of exam scores).
df['ph'] = df['ph'].fillna(df['ph'].mean())
df['Sulfate'] = df['Sulfate'].fillna(df['Sulfate'].mean())
df['Trihalomethanes'] = df['Trihalomethanes'].fillna(df['Trihalomethanes'].mean())

print("\n--- Confirming No Missing Values Remain ---")
print(df.isnull().sum())


# ---------------------------------------------------------
# Part 3 - Core Analysis
# ---------------------------------------------------------
print("\n--- Overall Potability Rate ---")
print(df['Potability'].mean())
# About 39% of samples are safe to drink (Potability = 1),
# the majority (about 61%) are not.

print("\n--- Feature Averages by Potability (All 9 Features) ---")
for col in ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate',
            'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']:
    print(df.groupby('Potability')[col].mean())
    print()
# Every single feature shows a difference of under 1% of its total
# range between potable and non-potable water. None of these
# individual measurements meaningfully distinguish safe from
# unsafe water on their own.


# ---------------------------------------------------------
# Part 4 - Correlation Check
# ---------------------------------------------------------
correlation = df.corr()['Potability'].sort_values(ascending=False)
print("\n--- Correlation of Each Feature with Potability ---")
print(correlation)
# All correlation values fall between -0.03 and +0.03 - essentially
# zero. This confirms the groupby finding above through a second,
# independent method: no single feature has a meaningful linear
# relationship with potability in this dataset.


# ---------------------------------------------------------
# Part 5 - Visualizations
# ---------------------------------------------------------
df['Potability'].value_counts().plot(kind='bar', color='blue')
plt.title('Water Potability Count (0=Not Safe, 1=Safe)')
plt.xlabel('Potability')
plt.ylabel('Count')
plt.savefig('potability_count.png', dpi=150, bbox_inches='tight')
plt.show()

correlation.plot(kind='bar', color='purple')
plt.title('Correlation of Each Feature with Potability')
plt.xlabel('Feature')
plt.ylabel('Correlation')
plt.savefig('potability_correlation.png', dpi=150, bbox_inches='tight')
plt.show()


# ---------------------------------------------------------
# Part 6 - Client Summary
# ---------------------------------------------------------
# Out of 3,276 water samples, about 39% (roughly 1,278) are safe
# to drink, while the majority (about 61%, roughly 1,998) are not.
# When checking correlation between each individual water quality
# feature and Potability, all values were close to zero (between
# -0.03 and +0.03), meaning no single feature strongly predicts on
# its own whether water is safe to drink. This suggests potability
# likely depends on a combination of factors working together,
# rather than any one measurement alone - exactly the kind of
# pattern Machine Learning models are designed to detect.
