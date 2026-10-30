# E01 — first look at the Delta Courier packages data.
# Same three steps as peek.ipynb, as a plain script.
import pandas as pd

df = pd.read_csv("../../data/packages.csv")

print("shape (rows, columns):")
print(df.shape)
print()
print("first rows:")
print(df.head())
print()
print("priority value counts:")
print(df["priority"].value_counts())
