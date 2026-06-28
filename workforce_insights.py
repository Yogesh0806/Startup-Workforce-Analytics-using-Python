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


'''Insight 3: Gender Representation Across Positions'''

gender_position = pd.crosstab(df['Position'], df['Gender'])

# print(gender_position)

# Visualization

# gender_position.plot(kind='bar',figsize=(12,6))
# plt.title('Gender Distribution Across Positions')
# plt.ylabel('Employee Count')
# plt.xticks(rotation=30)
# plt.show()


# Top 2 Insights

gender_count = df['Gender'].value_counts()

majority_gender = gender_count.idxmax()
majority_count = gender_count.max()

if majority_gender == 'M':
    majority_gender = 'Male'
elif majority_gender == 'F':
    majority_gender = 'Female'
    
minority_gender = gender_count.idxmin()
minority_count = gender_count.min()

# print(f"Insight 1: {majority_gender} employees form the largest workforce group ({majority_count} employees).")

# print(f"Insight 2: Both genders are represented across multiple positions, indicating workforce diversity.")

'''Insight 4: Experience vs Salary Relationship'''

# plt.figure(figsize=(8,6))
# sns.scatterplot(data=df,x='Experience (Years)',y='Salary')
# plt.title('Experience vs Salary')
# plt.show()

correlation = df[['Experience (Years)', 'Salary']].corr().iloc[0,1]

# print(correlation)            0.618529862372841


# print(
#     f"Insight 1: There is a moderate positive relationship between "
#     f"experience and salary (correlation = {correlation:.3f}), "
#     "indicating that employees with more experience generally earn higher salaries."
# )

# print(
#     "Insight 2: Salary tends to increase with experience, "
#     "but variation among employees with similar experience levels suggests "
#     "that other factors such as position and responsibilities also affect compensation."
# )


'''Report: Dashboard'''

fig, axes= plt.subplots(2,2, figsize=(10,5))

# Gender
df['Gender'] = df['Gender'].replace({'M': 'Male','F': 'Female'})

df['Gender'].value_counts().plot(kind='pie',ax=axes[0,0],autopct='%1.1f%%')


# Position
sns.countplot(data=df,y='Position',ax=axes[0,1],  palette='Reds')


# Salary
sns.histplot(data=df,x='Salary',ax=axes[1,0])


# Experience vs Salary
sns.scatterplot(data=df, x='Experience (Years)', y='Salary', ax=axes[1,1])


plt.tight_layout()
# plt.show()


'''Dashboard Insights'''

print("1. Workforce Composition")
print("The workforce is nearly balanced by gender, with Male employees (50.5%) and Female employees (49.5%).")

print("\n2. Position Distribution")
print("Web Developer and IT Manager have the highest employee counts, while Cloud Solutions Architect has the lowest representation.")

print("\n3. Salary Distribution")
print("Most employee salaries are concentrated between 90,000 and 170,000, while a smaller number earn above 200,000.")

print("\n4. Experience vs Salary")
print("There is a moderate positive relationship between experience and salary (correlation = 0.619).")

print("\n5. Salary Variation")
print("Employees with similar experience levels often receive different salaries, indicating that job position and responsibilities also influence compensation.")

print("\n6. Business Insight")
print("Employee compensation is primarily influenced by experience and job role, with senior and specialized positions receiving higher salaries.")

