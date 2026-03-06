import logging
import csv

def write_csv(file_path, data, fieldnames):
    try:
        with open(file_path, "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logging.error(f"Error writing {file_path}: {e}")
