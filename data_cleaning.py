# src/data_cleaning.py
"""
This script cleans a messy sales dataset.
It standardizes column names, trims whitespace, handles missing values,
and removes invalid rows. The final cleaned dataset is saved as CSV.
"""

import csv

# --- Function 1: Load CSV data ---
def load_data(file_path: str):
    """
    Load data from a CSV file into a list of dictionaries.
    Each row is represented as a dictionary keyed by column name.
    """
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    print(f"Loaded {len(data)} rows from {file_path}")
    return data

# --- Function 2: Clean column names ---
def clean_column_names(data):
    """
    Standardize column names: lowercase and replace spaces with underscores.
    """
    if not data:
        return data
    old_columns = data[0].keys()
    new_columns = [col.strip().lower().replace(" ", "_") for col in old_columns]

    cleaned_data = []
    for row in data:
        new_row = {}
        for old, new in zip(old_columns, new_columns):
            new_row[new] = row[old]
        cleaned_data.append(new_row)
    print("Column names standardized.")
    return cleaned_data

# --- Function 3: Handle missing values ---
def handle_missing_values(data):
    """
    Fill missing prices and quantities with 0.
    This ensures calculations won't fail and missing values are consistent.
    """
    for row in data:
        for key in row:
            if row[key] == "" or row[key] is None:
                # Fill numeric fields with 0, text fields with 'Unknown'
                if key in ["price", "quantity"]:
                    row[key] = "0"
                else:
                    row[key] = "Unknown"
    print("Missing values handled.")
    return data

# --- Function 4: Remove invalid rows ---
def remove_invalid_rows(data):
    """
    Remove rows with negative quantity or negative price,
    since these are clearly data entry errors.
    Also trim whitespace from product and category names.
    """
    cleaned = []
    for row in data:
        try:
            price = float(row.get("price", 0))
            quantity = int(row.get("quantity", 0))
        except ValueError:
            continue  # skip rows with invalid numbers

        if price < 0 or quantity < 0:
            continue

        # Trim whitespace from product and category names if they exist
        for col in ["product_name", "category"]:
            if col in row:
                row[col] = row[col].strip()

        cleaned.append(row)
    print(f"Removed invalid rows. Remaining rows: {len(cleaned)}")
    return cleaned

# --- Main execution ---
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    data_raw = load_data(raw_path)
    data_clean = clean_column_names(data_raw)
    data_clean = handle_missing_values(data_clean)
    data_clean = remove_invalid_rows(data_clean)

    # Save cleaned data
    if data_clean:
        with open(cleaned_path, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data_clean[0].keys())
            writer.writeheader()
            writer.writerows(data_clean)
        print(f"Cleaning complete. Cleaned data saved to {cleaned_path}")
    else:
        print("No data to save.")  
