import pandas as pd
import numpy as np
import matplotlib as mp
# print("Imported")

dataset = pd.read_csv('dirty.csv')
# print("Read")

# print(dataset.tail())
# print(dataset.head())

# print(dataset.shape)

# dataset.info()

# print(dataset.isnull().sum() / dataset.shape[0]*100)

# print(dataset.duplicated().sum())

# for i in dataset.select_dtypes(include='object').columns:
#     dataset[i].value_counts()
#     print("*****"*3)

# dataset.describe().T

