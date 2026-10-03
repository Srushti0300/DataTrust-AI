import pandas as pd


def load_csv(file_path):
    """Load a CSV dataset into a Pandas DataFrame."""
    return pd.read_csv(file_path, sep=",")


if __name__ == "__main__":
    data = load_csv("data/raw/customers.csv")

    print("Dataset loaded successfully!")
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")
    print("\nColumn names:")
    print(data.columns.tolist())

    print("\nFirst 5 rows:")
    print(data.head())