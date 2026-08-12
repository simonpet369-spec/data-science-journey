"""
ecommerce_dashboard.py
An e-commerce sales analysis project answering a real business
question: which product categories and regions should marketing
budget be focused on next quarter?

Dataset: ecommerce_sales_analytics_5000.csv (Kaggle)
Author: Simon
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Part 1 - Load and Inspect
# ---------------------------------------------------------
df = pd.read_csv('ecommerce_sales_analytics_5000.csv')

print("--- Shape and First Look ---")
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())
# Confirmed: dataset is fully clean, no missing values in any column.


# ---------------------------------------------------------
# Part 2 - Revenue by Product Category
# ---------------------------------------------------------
category_revenue = df.groupby('product_category')['revenue'].sum()
print("\n--- Revenue by Category ---")
print(category_revenue)
# Electronics is the clear leader at $1,829,899 - well ahead of
# Clothing ($1,531,932), Home ($982,084), and Beauty ($765,861).


# ---------------------------------------------------------
# Part 3 - Revenue by Region
# ---------------------------------------------------------
region_revenue = df.groupby('region')['revenue'].sum()
print("\n--- Revenue by Region ---")
print(region_revenue)
# West leads at $1,345,582, but all four regions are fairly close
# together ($1.24M-$1.35M) - region alone isn't a strongly
# differentiating factor here.


# ---------------------------------------------------------
# Part 4 - Category + Region Combined
# ---------------------------------------------------------
combo_revenue = df.groupby(['product_category', 'region'])['revenue'].sum()
print("\n--- Revenue by Category and Region Combined ---")
print(combo_revenue)
# The single highest combination is Electronics + South at
# $487,056 - the standout opportunity in the whole dataset.


# ---------------------------------------------------------
# Part 5 - Does Discount Level Affect Customer Rating?
# ---------------------------------------------------------
discount_rating = df.groupby('discount')['customer_rating'].mean()
print("\n--- Average Rating by Discount Level ---")
print(discount_rating)
# Ratings stay fairly flat (roughly 2.9-3.0) across nearly all
# discount levels, with no clear upward or downward trend.
# Conclusion: discount size has little meaningful effect on
# customer satisfaction in this dataset - it's not worth using
# discounts as a lever to improve ratings.


# ---------------------------------------------------------
# Part 6 - Visualizations
# ---------------------------------------------------------
category_revenue.plot(kind='bar', color='teal')
plt.title('Revenue by Product Category')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.savefig('category_revenue.png', dpi=150, bbox_inches='tight')
plt.show()

region_revenue.plot(kind='bar', color='orange')
plt.title('Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Revenue')
plt.savefig('region_revenue.png', dpi=150, bbox_inches='tight')
plt.show()


# ---------------------------------------------------------
# Part 7 - Client Summary
# ---------------------------------------------------------
# Electronics is our top-performing category, generating $1,829,899
# in total revenue - significantly ahead of other categories. By
# region, West leads overall at $1,345,582, though all four regions
# are fairly close together ($1.24M-$1.35M), suggesting region alone
# isn't a strongly differentiating factor. The standout opportunity
# is Electronics sold in the South region specifically, which
# generated $487,056 - the single highest category-region
# combination. The dataset had no missing values, so no data
# cleaning was required. Customer ratings remain fairly flat
# (roughly 2.9-3.0) across all discount levels, suggesting discount
# size has little meaningful effect on customer satisfaction.
# Recommendation: prioritize marketing budget on Electronics, with
# a particular focus on the South region, rather than relying on
# discounts to drive satisfaction.
