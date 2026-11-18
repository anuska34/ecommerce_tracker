import pandas as pd
from src.extract import extract_raw_data

def clean_raw_data(raw_df:pd.DataFrame)->pd.DataFrame:
    df = raw_df.drop_duplicates()
    df= df.dropna(subset=['product_id','price'])
    return df

if __name__ == "__main__":
    path = 'data/raw/raw_prices.csv'
    raw_data = extract_raw_data(path)
    
    clean_data = clean_raw_data(raw_data)
    print(clean_data)