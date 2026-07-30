import matplotlib.pyplot as plt
# Basics Structure with Line chart with labels
days = [1, 2, 3, 4]
sales = [10, 20, 25, 30]

plt.plot(days, sales, marker='o', color='green')
plt.title("Daily Sales")
plt.xlabel("Days")
plt.ylabel("Sales (units)")
plt.show()

# Bar Chart
products =["Shirts", "Shoes", "Bags", "Hats"]
sales = [150, 200, 90, 60]

plt.bar(products, sales, color='orange')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Unit sold")
plt.show()

# Histogram Chart
ages = [18, 22, 25, 19, 21, 23, 20, 18, 24, 22,
        21, 19, 23, 25, 20, 18, 22, 24, 21, 19]

plt.hist(ages, bins=10, color='purple', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age Range")
plt.ylabel("Number of People")
plt.show()

# Scatter plots Chart
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
exam_scores = [50, 55, 60, 68, 72, 80, 85, 92]

plt.scatter(study_hours, exam_scores, color='red')
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours") 
plt.ylabel("Exam Score") 
plt.show()

# Pie Chart 
labels = ["Facebook", "Instagram", "TikTok", "Other"]
sizes = [40, 30, 20, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Social media Ad Spend")
plt.show()

# The use of pandas with matplotlib
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Revenue": [1000, 1500, 1300, 1800]
})
df.plot(x="Month", y="Revenue", kind="line", marker='o', color='green')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (PKR)")
plt.show()

# Practice Tasks

# Task 1
days = [1, 2, 3, 4, 5, 6, 7]
temperature = [23, 34, 33, 25, 38, 32, 29]

plt.plot(days, temperature, marker='o', color='green')
plt.title("Week Temperature Chart")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()

# Task 2 
Study_Hours = [3, 1.5, 2, 1]
Liberies = ["Python", "Numpy", "Pandas", "Matplotlib"]

plt.bar(Liberies, Study_Hours, color='orange')
plt.title("Comparing Liberies with Study Time")
plt.xlabel("Liberies")
plt.ylabel("Study Hours")
plt.show()

# Task 3
import random

exam_scores = [random.randint(40, 100) for _ in range(20)]
print(exam_scores)

plt.hist(exam_scores, bins=4, color='teal', edgecolor='black')
plt.title("Exam Score Distribution")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.show()

# Task 4 
Hour_slept = [8, 8.5, 9, 6, 5.5, 4.9, 7, 6.7, 8.4, 7.4]
Productivity_Score = [90, 92, 97, 67, 60, 53, 81, 66, 89, 71]

plt.scatter(Hour_slept, Productivity_Score, color='orange')
plt.title("Hours Slept vs Productivity Score")
plt.xlabel("Hours Slept")
plt.ylabel("Productivity Score")
plt.show()

# Task 5
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
"Product" : ["Watches", "Clothes", "Bottles", "Books", "Stationary"],
"Sales" : [54, 34, 50, 45, 31]
})
df.plot(x="Product", y="Sales", kind="bar", color='orange')
plt.title("Today's Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()


# # Task 6
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('Titanic-Dataset.csv')
# print(df)

# df.plot(x="Name", y="Ticket", kind= "hist") 
# plt.title("Todays Expense")
# plt.xlabel("Name")
# plt.ylabel("Expense")
# plt.show()


