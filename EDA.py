"""Exploratory Data Analysis File"""

import pandas as pd
import warnings as wr

# cleaner output
wr.filterwarnings('ignore')

# Download latest version
df = pd.read_csv('diabetes.csv')

# 768 entries, 9 traits
print(df.shape)

# entries are either floats or ins
print(df.info())

# no null entries
print(df.isnull().sum())

# Traits:
# Number of Pregnancies
# Glucose level
# Blood pressure
# Thickness of skin
# Insulin level
# BMI
# Diabetes Pedigree Function = statistical risk of type 2 diabetes based on family history
# Age
# Outcome (1 = diabetes, 0 = no diabetes)
print(df.columns)

# outcomes are either 0 or 1
print(df.nunique())

# Correlation matrix
print(df.corr())
