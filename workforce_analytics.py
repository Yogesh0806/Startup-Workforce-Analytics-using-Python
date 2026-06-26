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

# 1. Gender Analysis

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