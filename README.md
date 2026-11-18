# ecommerce_tracker

A modular, end-to-end ETL (Extract, Transform, Load) pipeline built with Python to process raw e-commerce pricing data, clean and validate it, and store it in a local SQLite database.

This project was developed to practice core data engineering concepts, including data extraction, transformation, relational data modeling, modular programming, and automated testing.

## Project Overview

The pipeline consists of three main stages, coordinated by `main.py`:

1. **Extract (`src/extract.py`)**
   - Reads raw product and daily pricing data from CSV files.
   - Loads the data into Pandas DataFrames for further processing.
2. **Transform (`src/transform.py`)**
   - Cleans and standardizes raw data using Pandas.
   - Removes currency symbols and fixes inconsistent data types.
   - Handles missing values.
   - Separates static product information from daily pricing records.
3. **Load (`src/load.py`)**
   - Stores the cleaned data in a local SQLite database (`data/ecommerce.db`).
   - Organizes the data into a basic **Star Schema**:

| Table | Description |
| :--- | :--- |
| `dim_products` | Stores product details (`product_id`, `product_name`, `category`). |
| `fact_daily_prices` | Stores historical product prices and stock availability over time. |

## Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.14** | Core programming language |
| **Pandas** | Data cleaning and manipulation |
| **SQLite3** | Relational database storage |
| **Pytest** | Automated unit testing |
| **Logging** | Pipeline execution and error tracking |

## Project Structure

```text
ecommerce_tracker/
│
├── data/                  # Raw CSV files and SQLite database (Git-ignored)
├── src/
│   ├── extract.py         # Extracts raw CSV data
│   ├── transform.py       # Cleans and validates data
│   └── load.py            # Loads data into SQLite
├── tests/
│   └── test_transform.py  # Tests transformation logic
├── main.py                # Pipeline entry point
├── .gitignore
└── README.md