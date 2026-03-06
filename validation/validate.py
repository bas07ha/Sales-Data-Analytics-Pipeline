def validate_data(data):
    valid_rows = []
    invalid_rows = []

    for row in data:
        try:
            if row['quantity'] > 0 and row['price'] > 0 and row['order_id'] and row['customer'] and row['product']and row['total_revenue'] and row['date']:
                valid_rows.append(row)
            else:
                invalid_rows.append({**row, "error_reason": "quantity or price <= 0"})
        except Exception as e:
            invalid_rows.append({**row, "error_reason": f"validation_error: {e}"})
    return valid_rows, invalid_rows
