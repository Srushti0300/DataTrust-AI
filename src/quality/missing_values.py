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
empty_cities = data[data["city"].isnull() | (data["city"].str.strip() == "")]
print("\nEmpty City Names:")
print(empty_cities[["name", "city"]])
valid_email = data["email"].astype(str).str.match(
    r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"
)
print("\nInvalid Email Count:", (~valid_email).sum())
extra_spaces = data[
    data["email"].notnull() &
    (data["email"] != data["email"].str.strip())
]
print("\nEmails With Extra Spaces:")
print(extra_spaces[["name", "email"]])
numeric_age = pd.to_numeric(data["age"], errors="coerce")
print("\nNon-numeric Age Count:", (numeric_age.isnull() & data["age"].notnull()).sum())
numeric_amount = pd.to_numeric(data["purchase_amount"], errors="coerce")
print("\nInvalid Purchase Amount Count:", numeric_amount.isnull().sum())