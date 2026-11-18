import logging
import os
import pandas as pd

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)
def extract_raw_data(file_path:str)->pd.DataFrame:
    logger.info(f"Extracting the raw data from {file_path}")
    try:
        df = pd.read_csv(file_path)
        logger.info(f"Successfully extracted {len(df)} raw records.")
        return df
    except FileNotFoundError as e:
        logger.error(f"File cannot be found:{file_path}")
        raise e
    except Exception as e:
        logger.error(f"Error occured during extraction:{file_path}")
        raise e
if __name__ == "__main__":
    path= "data/raw/raw_prices.csv"
    raw_df = extract_raw_data(path)
    print(raw_df.head())
        