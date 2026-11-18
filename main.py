import pandas as pd
from src.extract import extract_raw_data
from src.transform import clean_raw_data
from src.load import load_to_sqlite

def main():
    
    raw_data = extract_raw_data("data/raw/raw_prices.csv")
    clean_data = clean_raw_data(raw_data)
    load_to_sqlite(clean_data)
    print("Pipeline complete")
    
if __name__=="__main__":
    main()