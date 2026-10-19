import pandas as pd

data = pd.read_csv("data/raw/customers.csv")

missing = data.isnull().sum()

print("Missing Values:")
print(missing[missing > 0])
duplicates = data.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")
duplicates = data.duplicated().sum()
print(f"Duplicate rows: {duplicates}")
invalid_age = data[(data["age"] < 0) | (data["age"] > 100)]

print("\nInvalid Ages:")
print(invalid_age[["name", "age"]])
invalid_email = data[
    ~data["email"].astype(str).str.match(r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$")
]

print("\nInvalid Emails:")
print(invalid_email[["name", "email"]])
negative_amounts = data[data["purchase_amount"] < 0]

print("\nNegative Purchase Amounts:")
print(negative_amounts[["name", "purchase_amount"]])