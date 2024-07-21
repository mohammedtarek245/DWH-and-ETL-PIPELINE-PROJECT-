import pandas as pd
from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database info
DB_USER = ''
DB_PASSWORD = '' 
DB_HOST = ''
DB_PORT = ''
DB_NAME = ''

# 1 - Extracting process

file_path = ''

def extract_data(file_path):
    logger.info("Extracting data from %s", file_path)
    try:
        data = pd.read_csv(file_path)
        logger.info("Data extracted successfully.")
        return data
    except Exception as e:
        logger.error("Error extracting data: %s", e)
        raise

# 2 - Transformation process
# Transforming CSV file or editing data types or cleaning 

def transform_data(data):
    logger.info("Transforming data.")
    try:
        data = data.dropna()      # Remove rows with missing values
        logger.info("Data transformed successfully.")
        return data
    except Exception as e:
        logger.error("Error transforming data: %s", e)
        raise

# 3 - Loading process
# Loading data into the database

def load_data(data, table_name):
    logger.info("Loading data into %s table.", table_name)
    try:
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        with engine.connect() as connection:
            data.to_sql(table_name, connection, if_exists='replace', index=False)
        logger.info("Data loaded successfully.")
    except Exception as e:
        logger.error("Error loading data: %s", e)
        raise

def main():
    # ETL process
    file_path = ''
    table_name = 'sales_report'

    try:
        # Extract
        data = extract_data(file_path)
        
        # Transform
        data = transform_data(data)
        
        # Load
        load_data(data, table_name)
        
        logger.info("ETL process completed successfully.")
    except Exception as e:
        logger.error("ETL process failed: %s", e)

if __name__ == "__main__":
    main()
