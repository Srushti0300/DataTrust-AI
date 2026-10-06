import pandas as pd

data = pd.read_csv("data/raw/customers.csv")

missing = data.isnull().sum()

print("Missing Values:")
print(missing[missing > 0])