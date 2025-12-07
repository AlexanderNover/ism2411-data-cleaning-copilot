# ism2411-data-cleaning-copilot

Small data cleaning project for ISM2411.

## Project Overview
This project demonstrates a Python-based data cleaning workflow using a messy sales dataset.  
The goal is to load the raw CSV file (`sales_data_raw.csv`), clean it, and save a processed CSV (`sales_data_clean.csv`).  
Key cleaning steps include:

- Standardizing column names (lowercase, underscores)
- Stripping leading/trailing whitespace from text fields
- Handling missing values in numeric columns (price, quantity) using median imputation
- Removing rows with negative price or quantity
- Removing duplicate rows

This project also highlights responsible use of GitHub Copilot to generate and refine functions.

## Files
