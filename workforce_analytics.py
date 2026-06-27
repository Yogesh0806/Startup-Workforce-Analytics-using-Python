# Import Libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\Desktop\Startup Workforce Analytics using Python\employee_data.csv")

# Data Understanding :-

# print(df.head())
        # ID Gender  Experience (Years)               Position  Salary
        # 0   1      F                   4        DevOps Engineer  109976
        # 1   2      M                   6        DevOps Engineer  120088
        # 2   3      M                  17          Web Developer  181301
        # 3   4      M                   7  Systems Administrator   77530
        # 4   5      F                  13  Systems Administrator  152397

# print(df.info())

# print(df.shape)
        # (400, 5)
    
# chack for null values 
# print(df.isnull().sum())

# duplicate values 
# print(df.duplicated().sum())

# chack data types of the column
# print(df.dtypes())

# Data Analysis with visualization and Statastics :-

''' 1. Gender Analysis'''

# Gender Distribution

# plt.figure(figsize=(6,4))
# sns.countplot(data=df, x='Gender',palette=['lightgreen','skyblue'])
# plt.title('Gender Distribution')
# plt.show()

gender_count = df['Gender'].value_counts()
# print(gender_count)

        # Gender
        # M    202
        # F    198
        # Name: count, dtype: int64

gender_percentage = round((df['Gender'].value_counts(normalize = True))*100,2)
# print(gender_percentage)

        # Gender
        # M    50.5
        # F    49.5
        # Name: proportion, dtype: float64

''' 2. Position Analysis '''


# plt.figure(figsize=(12,6))
# sns.countplot(data=df,y='Position', order=df['Position'].value_counts().index,hue='Position', palette='Set1')
# plt.title('Employee Count by Position')
# plt.show()

position_count = df['Position'].value_counts()
# print(position_count)

        # Position
        # Web Developer                   43
        # IT Manager                      40
        # IT Security Analyst             39
        # Database Administrator (DBA)    38
        # Systems Administrator           38
        # DevOps Engineer                 37
        # Systems Analyst                 37
        # Software Engineer               36
        # Network Administrator           31
        # IT Support Specialist           31
        # Cloud Solutions Architect       30
        # Name: count, dtype: int64
        

# print("Total Positions:", df["Position"].nunique())
        #Total Positions: 11
        
'''3. Salary Analysis'''

# plt.figure(figsize=(8,5))
# sns.histplot(df['Salary'],bins=20,kde=True,color='skyblue')
# plt.title('Salary Distribution')
# plt.show()


# Salary Statastics 
# print(df['Salary'].describe())

        # count       400.00000
        # mean     131701.19750
        # std       43351.50899
        # min       43643.00000
        # 25%      100484.75000
        # 50%      128561.50000
        # 75%      157735.00000
        # max      269950.00000
        # Name: Salary, dtype: float64
      
# Employee with Highest Salary  
highest_paid = df[df["Salary"] == df["Salary"].max()]
# print(highest_paid)
        # 115  116      M                  18  IT Manager  269950
        
        
# Employee with Lowest Salary 

lowest_paid = df[df["Salary"] == df["Salary"].min()]
# print(lowest_paid)
        # 111  112      F                   1  IT Support Specialist   43643
        
'''4. Experience Analysis'''

# plt.figure(figsize=(8,5))
# sns.histplot(df['Experience (Years)'],bins=15,kde=True,color='darkgray')
# plt.title('Experience Distribution')
# plt.show()

# Statastics of Experience's
# print(df['Experience (Years)'].describe())

        # count    400.000000
        # mean       9.670000
        # std        6.101571
        # min        0.000000
        # 25%        4.000000
        # 50%       10.000000
        # 75%       15.000000
        # max       20.000000
        # Name: Experience (Years), dtype: float64
        
        
# print(df['Experience (Years)'].value_counts().sort_index())

        # Experience (Years)
        # 0     17
        # 1     24
        # 2     24
        # 3     26
        # 4     18
        # 5     17
        # 6     18
        # 7     17
        # 8     13
        # 9     19
        # 10    22
        # 11    22
        # 12    18
        # 13    21
        # 14    20
        # 15    13
        # 16    21
        # 17    17
        # 18    15
        # 19    22
        # 20    16
        # Name: count, dtype: int64
        
# 5. Salary by Position

avg_Salary_Position = (df.groupby('Position')['Salary'].mean().sort_values(ascending=False))
# print(round(avg_Salary_Position,2))
        # Position
        # IT Manager                      170711.55     # Highest paying position
        # DevOps Engineer                 161859.08
        # Cloud Solutions Architect       160841.63
        # IT Security Analyst             134440.82
        # Database Administrator (DBA)    132864.55
        # Software Engineer               131357.42
        # Systems Analyst                 127658.19
        # Network Administrator           116865.06
        # Systems Administrator           113117.45
        # Web Developer                   108238.12
        # IT Support Specialist            87683.81     # Lowest paying position
        # Name: Salary, dtype: float64
        
'''6. Experience by Position'''

avg_Exp_Position = df.groupby('Position')['Experience (Years)'].mean().sort_values(ascending= False)
# print(round(avg_Exp_Position,2))

        # Position
        # Network Administrator           11.52
        # DevOps Engineer                 11.00
        # Database Administrator (DBA)    10.84
        # Systems Administrator            9.84
        # Systems Analyst                  9.68
        # Web Developer                    9.47
        # IT Manager                       9.22
        # Cloud Solutions Architect        9.00
        # IT Security Analyst              8.87
        # IT Support Specialist            8.52
        # Software Engineer                8.44
        # Name: Experience (Years), dtype: float64
        
'''7. Gender-wise Salary Analysis'''

gender_salary = (df.groupby("Gender")["Salary"].mean())
# print(round(gender_salary, 2))
        # Gender
        # F    132629.97
        # M    130790.81
        # Name: Salary, dtype: float64

'''8. Correlation Analysis'''
correlation = df[["Experience (Years)", "Salary"]].corr()
# print(correlation)
        #    Experience (Years)   Salary
        # Experience (Years)             1.00000  0.61853
        # Salary                         0.61853  1.00000



# Saved the important results of day 2 as csv
# avg_Salary_Position.to_csv(
#     "avg_salary_by_position.csv"
# )

# avg_Exp_Position.to_csv(
#     "avg_experience_by_position.csv"
# )
