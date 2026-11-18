import pandas as pd
import pytest
from src.transform import clean_raw_data

def test_clean_raw_data_removes_duplicates():
    raw_data = pd.DataFrame({
        'product_id': ['P001', 'P001', 'P002'],
        'product_name': ['Mouse', 'Mouse', 'Keyboard'],
        'category': ['Electronics', 'Electronics', 'Electronics'],
        'price': [25.99, 25.99, 79.99],
        'stock_status': ['In Stock', 'In Stock', 'In Stock'],
        'date': ['2026-11-01', '2026-11-01', '2026-11-01']
    })
    
    cleaned_df=clean_raw_data(raw_data)
    
    assert len(cleaned_df) == 2
    assert 'product_id' in cleaned_df.columns
    assert 'price' in cleaned_df.columns