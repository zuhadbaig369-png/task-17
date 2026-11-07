import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Bestsellers with categories.csv")

print(data.isnull().sum())

data = data.dropna()

print(data["Genre"].value_counts())
print(data.select_dtypes(include="number").skew())
print(data.groupby("Genre")["User Rating"].mean())
print(data[["User Rating", "Price"]].corr())
sns.boxplot(data=data, x="Genre", y="User Rating")
plt.show()
sns.scatterplot(data=data, x="Price", y="User Rating")
plt.show()