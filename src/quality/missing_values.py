import pandas as pd

data = pd.read_csv("data/raw/customers.csv")

# Check missing values
missing = data.isnull().sum()

print("Missing Values:")
print(missing[missing > 0])

# Check duplicate rows
duplicates = data.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

# Check empty email addresses
empty_emails = data[
    data["email"].isnull() |
    (data["email"].str.strip() == "")
]

print("\nEmpty Email Addresses:")
print(empty_emails[["name", "email"]])
invalid_age = data[
    (data["age"] < 0) | (data["age"] > 100)
]

print("\nInvalid Customer Ages:")
print(invalid_age[["name", "age"]])
negative_amounts = data[data["purchase_amount"] < 0]

print("\nNegative Purchase Amounts:")
print(negative_amounts[["name", "purchase_amount"]])
print("\nDuplicate Customer IDs:")
print(data[data["customer_id"].duplicated(keep=False)])
empty_names = data[data["name"].isnull() | (data["name"].str.strip() == "")]
print("\nEmpty Customer Names:")
print(empty_names)