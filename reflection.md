# ism2411-data-cleaning-copilot

Small data cleaning project for ISM2411.

## What
Loads `data/raw/sales_data_raw.csv`, standardizes column names, strips whitespace, coerces numeric fields, handles missing values (filled with median for price/quantity), removes rows with negative price/quantity and duplicates, and writes `data/processed/sales_data_clean.csv`.

## Run
From project root:
