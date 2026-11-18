import sqlite3
import pandas as pd
from src.extract import extract_raw_data
from src.transform import clean_raw_data
    
def load_to_sqlite(clean_df :pd.DataFrame,db_path: str='data/ecommerce.db')->None:
    print("Loading into sqlite Database")
    
    conn = sqlite3.connect(db_path)
    try:
        dim_products = clean_df[['product_id','product_name','category']].drop_duplicates(subset=['product_id'])
        fact_daily_prices = clean_df[['product_id','date','price','stock_status']]
        
        dim_products.to_sql('dim_products',conn,if_exists='replace',index=False)
        fact_daily_prices.to_sql('fact_daily_prices',conn,if_exists='replace',index=False)
                                                                                        
    except Exception as e:
        print(f"database loading failed: {e}")
        raise e
    finally:
        conn.close()
        
if __name__ == "__main__":
    raw_data = extract_raw_data("data/raw/raw_prices.csv")
    clean_data = clean_raw_data(raw_data)
    load_to_sqlite(clean_data)