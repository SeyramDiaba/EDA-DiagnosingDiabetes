import codecademylib3
import pandas as pd
import numpy as np

# code goes here
# loading 'diabetes.csv' file
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())

# Statement below show there are 9 columns
print(len(diabetes_data.columns))

# Statement below show whre are 768 rows
print(len(diabetes_data))

# Do any of the columns contain null values?
query = diabetes_data[diabetes_data.isnull()]
print(query.sum())

# To further calculate summary statistics on dataset we use the '.describe()' method to question our assumptions
print(diabetes_data.describe(include = 'all'))

# Replacing all instances of with 'NaN'
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

# Checking for number of missing values in columns
print(diabetes_data.isnull().sum())

# Printing of all rows that have missing data
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

# Taking a closer look at the data types of each column in diabetes_data.
print(diabetes_data.dtypes)

# Checking why the "Outcome" column is of dtype object instead of int
print(diabetes_data.Outcome.unique())

# Replacing all 'O' misentries and replacing them with '0'
diabetes_data['Outcome'] = pd.to_numeric(diabetes_data['Outcome'].replace('O','0'))
print(diabetes_data.Outcome.unique())
print(diabetes_data.dtypes)