"""
titanic_analysis.py
Exploring and cleaning the Kaggle Titanic dataset - a real, messy
dataset (not made up), used to practice handling actual missing
data and drawing real conclusions with Pandas and Matplotlib.

Dataset source: Kaggle "Titanic - Machine Learning from Disaster"
Author: Simon
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Part 1 - First Look
# ---------------------------------------------------------
df = pd.read_csv('train.csv')

print("--- First Look ---")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())


# ---------------------------------------------------------
# Part 2 - Find the Real Mess
# ---------------------------------------------------------
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Cabin is missing for ~77% of passengers (687 out of 891).
# Cabin numbers are unique identifiers (e.g. "C85"), not values
# with a sensible "typical" answer, so filling them (even with
# mode) would mean fabricating specific, false information at
# massive scale. Dropping the column is the more honest choice.
df = df.drop(columns=['Cabin'])

# Age is missing for 177 passengers. Median is used instead of
# mean since it isn't pulled by outliers (very young or very old
# passengers) the way an average can be.
df['Age'] = df['Age'].fillna(df['Age'].median())

# Embarked is missing for only 2 passengers. Filling with the
# most common boarding port (mode) is a reasonable, low-risk fix
# for such a small number of missing values.
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

print("\n--- Confirming No Missing Values Remain ---")
print(df.isnull().sum())


# ---------------------------------------------------------
# Part 3 - Real Questions With GroupBy
# ---------------------------------------------------------
print("\n--- Overall Survival Rate ---")
print(df['Survived'].mean())

print("\n--- Survival Rate by Sex ---")
print(df.groupby('Sex')['Survived'].mean())

print("\n--- Survival Rate by Pclass ---")
print(df.groupby('Pclass')['Survived'].mean())

print("\n--- Survival Rate by Sex and Pclass Combined ---")
print(df.groupby(['Sex', 'Pclass'])['Survived'].mean())


# ---------------------------------------------------------
# Part 4 - Visualize the Findings
# ---------------------------------------------------------
survival_rate_sex = df.groupby('Sex')['Survived'].mean()
survival_rate_sex.plot(kind='bar', color='orange')
plt.title('Survival Rate by Sex/Gender')
plt.xlabel('Gender/Sex')
plt.ylabel('Survived')
plt.savefig('survival_by_sex.png', dpi=150, bbox_inches='tight')
plt.show()

survival_rate_pclass = df.groupby('Pclass')['Survived'].mean()
survival_rate_pclass.plot(kind='bar', color='orange')
plt.title('Survival Rate by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Survived')
plt.savefig('survival_by_pclass.png', dpi=150, bbox_inches='tight')
plt.show()

df['Age'].hist(bins=20, color='teal', edgecolor='black')
plt.title('Distribution of Passenger Age')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.savefig('age_distribution.png', dpi=150, bbox_inches='tight')
plt.show()


# ---------------------------------------------------------
# Part 5 - Client Summary
# ---------------------------------------------------------
# The overall survival rate was 38.4%. Female passengers survived
# at a much higher rate (74.2%) compared to male passengers
# (18.9%). First class passengers had the highest survival rate
# at 63.0%, followed by second class at 47.3%, while third class
# had the lowest survival rate at 24.2% - showing that passenger
# class had a clear impact on survival chances. One honest note:
# the Cabin column was dropped from this analysis, since 77% of
# its values were missing and cabin numbers are unique identifiers
# that can't be reasonably estimated or filled in.
