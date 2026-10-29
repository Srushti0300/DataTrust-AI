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