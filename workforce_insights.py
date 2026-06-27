# FINAL INSIGHTS OF THIS PROJECT


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\Desktop\Startup Workforce Analytics using Python\employee_data.csv')

# print(df.head())

# File loaded successfully

'''Insight 1: Average Salary by Position'''

salary_position = df.groupby('Position')['Salary'].mean().sort_values(ascending=False)
# print(salary_position)

# Visualization

# plt.figure(figsize=(10,6))
# salary_position.plot(kind='barh')
# plt.title('Average Salary by Position')
# plt.xlabel('Average Salary')
# plt.yticks(rotation=45)
# plt.show()

highest_position= salary_position.idxmax()
highest_salary= salary_position.max()

lowest_position= salary_position.idxmin()
lowest_salary= salary_position.min()

# print(f"Insight 1: {highest_position} has the highest average salary (₹{highest_salary:,.2f}).")
# print(f"Insight 2: {lowest_position} has the lowest average salary (₹{lowest_salary:,.2f}), showing a clear salary difference across positions.")

'''Insight 2: Average Experience by Position'''

experience_position = df.groupby('Position')['Experience (Years)'].mean().sort_values(ascending=False)
# print(experience_position)

# Visualization

# plt.figure(figsize=(10,6))
# experience_position.plot(kind='barh')
# plt.title('Average Experience by Position')
# plt.xlabel('Experience of years')
# plt.yticks(rotation=45)
# plt.show()

# Top 2 Insights

highest_exp_position = experience_position.idxmax()
highest_exp = experience_position.max()

lowest_exp_position = experience_position.idxmin()
lowest_exp = experience_position.min()

# print(f"Insight 1: {highest_exp_position} has the highest average experience ({highest_exp:.1f} years).")

# print(f"Insight 2: {lowest_exp_position} has the lowest average experience ({lowest_exp:.1f} years), indicating that this role is generally filled by less experienced employees.")