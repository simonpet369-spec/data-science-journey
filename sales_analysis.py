"""
sales_analysis.py
A small sales data analysis project combining Pandas and Matplotlib:
cleaning, groupby analysis, and visualization.

Author: Simon
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Part 1 — Load, Inspect, and Clean
# ---------------------------------------------------------
data = {
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Apr', 'Apr'],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South', 'North', 'South'],
    'Product': ['Laptop', 'Phone', 'Laptop', 'Phone', 'Laptop', 'Phone', 'Laptop', 'Phone'],
    'Revenue': [120000, 85000, 135000, 90000, None, 95000, 150000, 88000],
    'Units_Sold': [12, 17, 14, 18, 11, 19, 15, 17]
}
df = pd.DataFrame(data)

print("--- Initial Inspection ---")
print(df.shape)
print(df.head())
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

# March's Revenue was missing, so it's filled with the average
# of the other months to keep the dataset usable for analysis.
df['Revenue'] = df['Revenue'].fillna(df['Revenue'].mean())

print("\n--- Cleaned DataFrame ---")
print(df)


# ---------------------------------------------------------
# Part 2 — Analyze With GroupBy
# ---------------------------------------------------------
print("\n--- Total Revenue by Region ---")
print(df.groupby('Region')['Revenue'].sum())

print("\n--- Total Revenue by Month ---")
print(df.groupby('Month')['Revenue'].sum())

print("\n--- Average Units Sold by Product ---")
print(df.groupby('Product')['Units_Sold'].mean())

print("\n--- Region with Highest Single Revenue Entry ---")
print(df.groupby('Region')['Revenue'].max())


# ---------------------------------------------------------
# Part 3 — Visualize With Matplotlib
# (Data is grouped/aggregated BEFORE charting, since the raw
#  rows have multiple entries per Month/Region/Product.)
# ---------------------------------------------------------

# Line chart — overall revenue trend across months
monthly_revenue = df.groupby('Month')['Revenue'].sum()
monthly_revenue.plot(kind='line', marker='o', color='green')
plt.title("Overall Revenue Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.savefig('revenue_by_month.png', dpi=150, bbox_inches='tight')
plt.show()

# Bar chart — total revenue by region
region_revenue = df.groupby('Region')['Revenue'].sum()
region_revenue.plot(kind='bar', color='orange')
plt.title("Region Performance")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.savefig('revenue_by_region.png', dpi=150, bbox_inches='tight')
plt.show()

# Pie chart — share of total units sold by product
product_units = df.groupby('Product')['Units_Sold'].sum()
product_units.plot(kind='pie', autopct='%1.1f%%')
plt.title("Product Share of Total Units Sold")
plt.ylabel('')
plt.savefig('units_by_product.png', dpi=150, bbox_inches='tight')
plt.show()


# ---------------------------------------------------------
# Part 4 — Client Summary
# ---------------------------------------------------------
# According to this data, the North region performed best overall,
# generating 514,000 in revenue compared to 358,000 in the South.
# April was the strongest month with 238,000 in revenue, while
# March was the weakest at 204,000 - though it's worth noting
# March's revenue included one missing value that was estimated
# using the average of the other months. In terms of units sold,
# Phone was the better-selling product overall with 71 units,
# compared to 52 units for Laptop, even though Laptop likely
# generates more revenue per unit sold.
