import logging
import os
from ingestion.ingest_sales import read_csv
from transformations.transform import transform_data
from validation.validate import validate_data
from storage.write import write_csv
from loading.load_postgres import load_sales_to_postgres


logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s"    )

#file paths
input_file = os.path.join("data", "sales.csv")
clean_file = os.path.join("data", "sales_clean.csv")
invalid_file = os.path.join("data", "sales_invalid.csv")



#pipeline work (execution)
# Read
raw_data = read_csv(input_file)

# Step 2: Transform
cleaned_data = transform_data(raw_data)

# Step 3: Validate
valid_rows, invalid_rows = validate_data(cleaned_data)

# Step 4: Write outputs
if valid_rows:
    valid_fieldnames = list(valid_rows[0].keys())
    write_csv(clean_file, valid_rows, valid_fieldnames)

if invalid_rows:
    invalid_fieldnames = list(valid_rows[0].keys()) + ['error_reason'] if valid_rows else ['order_id','customer','product','quantity','price','total_revenue','date','error_reason']
    write_csv(invalid_file, invalid_rows, invalid_fieldnames)


load_sales_to_postgres(valid_rows,"sales")
logging.info("Pipeline completed successfully")
