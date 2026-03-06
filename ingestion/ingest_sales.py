import csv
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



def read_csv(file_path, delimiter=';'):
    try:
        with open(file_path,"r",newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            data = list(reader)
        logging.info(f"Successfully read {len(data)} rows from {file_path}")
        if data:
            logging.info(f"First row: {data[0]}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
        return []

