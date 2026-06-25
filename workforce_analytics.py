# Import Libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\Desktop\Startup Workforce Analytics using Python\employee_data.csv")

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
print(df.dtypes())