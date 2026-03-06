from datetime import datetime
import logging


def transform_data(data):
    cleaned = []
    for row in data:
        try:
            quantity = int(row['quantity'])
            price = float(row['price'])
            total_revenue = quantity * price
            date_obj = datetime.strptime(row['date'], "%d/%m/%Y")
            formatted_date = date_obj.strftime("%Y-%m-%d")
            cleaned_row = {
                "order_id": row['order_id'],
                "customer": row['customer'],
                "product": row['product'],
                "quantity": quantity,
                "price": price,
                "total_revenue": total_revenue,
                "date": formatted_date
            }
            cleaned.append(cleaned_row)
        except Exception as e:
            logging.warning(f"Skipping row due to transformation error: {row}. Error: {e}")
    return cleaned