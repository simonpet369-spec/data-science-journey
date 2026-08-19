"""
titanic_classification.py
Real Machine Learning classification on the Titanic dataset -
predicting passenger survival using Logistic Regression and
Decision Trees, with proper train/test evaluation.

Dataset: Kaggle Titanic - Machine Learning from Disaster
Author: Simon
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# ---------------------------------------------------------
# Part 1 - Load and Clean
# (same verified cleaning steps as titanic_analysis.py)
# ---------------------------------------------------------
df = pd.read_csv('train.csv')
df = df.drop(columns=['Cabin'])
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Models need numbers, not text - convert Sex to 0/1
df['Sex_female'] = (df['Sex'] == 'female').astype(int)


# ---------------------------------------------------------
# Part 2 - Choose Features and Target
# ---------------------------------------------------------
X = df[['Sex_female', 'Pclass', 'Age']]
y = df['Survived']


# ---------------------------------------------------------
# Part 3 - Honest Train/Test Split
# 80% training ("homework"), 20% testing ("hidden exam")
# ---------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ---------------------------------------------------------
# Part 4 - Logistic Regression
# ---------------------------------------------------------
model = LogisticRegression()
model.fit(X_train, y_train)   # trained ONLY on X_train, y_train

accuracy = model.score(X_test, y_test)
print("Logistic Regression Accuracy:", accuracy)
# Result: 81.0% - clearly beats the 61.6% baseline of always
# guessing "did not survive"


# ---------------------------------------------------------
# Part 5 - Decision Tree (for comparison)
# ---------------------------------------------------------
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

tree_accuracy = tree_model.score(X_test, y_test)
print("Decision Tree Accuracy:", tree_accuracy)
# Result: 77.7% - lower than Logistic Regression. Decision Trees
# ask a series of yes/no questions, creating sharp rectangular
# splits that can fit the training data too closely (overfit),
# unlike Logistic Regression's single smooth boundary line.


# ---------------------------------------------------------
# Part 6 - Predict a New Passenger
# ---------------------------------------------------------
new_passenger = pd.DataFrame({
    'Sex_female': [1],
    'Pclass': [1],
    'Age': [30]
})
prediction = model.predict(new_passenger)
probability = model.predict_proba(new_passenger)
print("New passenger prediction:", prediction)
print("Probability [died, survived]:", probability)
# A female, 1st class, age 30 passenger: predicted survived,
# ~91% probability - consistent with the real historical finding
# that female + 1st class passengers survived at ~96.8%.


# ---------------------------------------------------------
# Part 7 - Confusion Matrix (Logistic Regression)
# ---------------------------------------------------------
predictions = model.predict(X_test)
cm = confusion_matrix(y_test, predictions)
print("\nConfusion Matrix:")
print(cm)
# [[91 14]
#  [20 54]]
#
#               Predicted Died   Predicted Survived
# Actually Died      91 (correct)    14 (false alarm)
# Actually Survived  20 (missed)     54 (correct)
#
# Correct predictions sit on the diagonal (91, 54).
# Mistakes sit off the diagonal (14, 20).


# ---------------------------------------------------------
# Part 8 - Precision and Recall
# ---------------------------------------------------------
print("\nClassification Report:")
print(classification_report(y_test, predictions))
# Precision for "survived" (54/68 = 0.79): of everyone the model
# predicted would survive, 79% actually did.
# Recall for "survived" (54/74 = 0.73): of everyone who actually
# survived, the model correctly caught 73% of them.
# Both manually verified by hand and confirmed to match sklearn's
# calculation exactly.
