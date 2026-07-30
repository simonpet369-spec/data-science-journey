"""
pandas_practice.py
Pandas practice covering DataFrame basics, selection, filtering,
column operations, missing values, and groupby.

Author: Simon
"""

import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Dataset used for Tasks 1-4, 6, 7
# ---------------------------------------------------------
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Watch', 'Earbuds', 'Camera'],
    'Price': [85000, 45000, 32000, 15000, 8000, 55000],
    'Stock': [10, 25, 15, 50, 100, 8],
    'Category': ['Electronics', 'Electronics', 'Electronics',
                 'Wearable', 'Wearable', 'Electronics'],
    'Rating': [4.5, 4.2, 3.8, 4.0, 4.3, 4.7]
}
df = pd.DataFrame(data)


# ---------------------------------------------------------
# Task 1 — DataFrame Basics
# ---------------------------------------------------------
print("--- Task 1: DataFrame Basics ---")
print(df.shape)
print(df.columns)
print(df[['Product', 'Rating']])


# ---------------------------------------------------------
# Task 2 — Selecting Rows
# ---------------------------------------------------------
print("\n--- Task 2: Selecting Rows ---")
print(df.head(3))
print(df.tail(2))
print(df.iloc[2])              # row at position 2 (Tablet)
print(df.iloc[4, 1])           # Price of item at position 4 (Earbuds)


# ---------------------------------------------------------
# Task 3 — Filtering
# ---------------------------------------------------------
print("\n--- Task 3: Filtering ---")
print(df[df['Price'] > 30000])
print(df[df['Category'] == 'Wearable'])
print(df[(df['Price'] > 20000) & (df['Rating'] > 4.0)])
print(df[df['Stock'] < 20][['Product', 'Price']])


# ---------------------------------------------------------
# Task 4 — Adding and Modifying Columns
# ---------------------------------------------------------
print("\n--- Task 4: Adding and Modifying Columns ---")
df['Total_Value'] = df['Price'] * df['Stock']
df['Discounted_Price'] = df['Price'] * 0.9
print(df[['Product', 'Discounted_Price']])
print(df.sort_values('Total_Value', ascending=False)[['Product', 'Total_Value']])


# ---------------------------------------------------------
# Task 5 — Missing Values
# (separate small dataset, on purpose, to practice this)
# ---------------------------------------------------------
print("\n--- Task 5: Missing Values ---")
data2 = {
    'Name': ['Ali', 'Sara', 'John', None],
    'Age': [22, None, 23, 21],
    'Score': [88, 92, None, 95]
}
df2 = pd.DataFrame(data2)

print(df2.isnull().sum())
df2['Age'] = df2['Age'].fillna(df2['Age'].mean())
df2['Score'] = df2['Score'].fillna(df2['Score'].median())
print(df2)

# Mean works well for Age here since there are no extreme outliers,
# so the average stays representative of the group.
# Median is used for Score as a safer default when a column could
# contain outliers, since median isn't pulled by extreme values.


# ---------------------------------------------------------
# Task 6 — GroupBy
# ---------------------------------------------------------
print("\n--- Task 6: GroupBy ---")
print(df.groupby('Category')['Price'].mean())
print(df.groupby('Category')['Rating'].mean())
print(df.groupby('Category')['Price'].agg(['mean', 'min', 'max']))
print(df['Category'].value_counts())


# ---------------------------------------------------------
# Task 7 — Putting It All Together
# ---------------------------------------------------------
print("\n--- Task 7: Putting It All Together ---")
print(df[df['Price'] == df['Price'].max()]['Product'])   # most expensive
print(df[df['Price'] == df['Price'].min()]['Product'])   # cheapest
print(df.sort_values('Rating', ascending=False))
print(df[(df['Category'] == 'Electronics') & (df['Rating'] > 4.0)][['Product', 'Price']])
