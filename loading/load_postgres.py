import psycopg2
from psycopg2 import sql
import logging

def load_sales_to_postgres(valid_rows,table_name):
    connexion = None
    cursor = None
    try:
        connexion=psycopg2.connect(
            dbname='sales_analytics',
            user='postgres',
            password='postgressql2003',
            host='localhost',
            port='5432'
        )
        cursor=connexion.cursor()
        
        create_table_query=sql.SQL(
                """CREATE TABLE IF NOT EXISTS {table} (
                    order_id INT PRIMARY KEY,
                    customer VARCHAR(100) NOT NULL,
                    product VARCHAR(100) NOT NULL,
                    quantity INT NOT NULL,
                    price FLOAT NOT NULL,
                    total_revenue FLOAT NOT NULL,
                    date DATE NOT NULL
                )
          """).format(table=sql.Identifier(table_name))
        cursor.execute(create_table_query)
        logging.info(f'table {table_name} created successfully')
        
        insert_table_query=sql.SQL(
                """INSERT INTO {table} (
                order_id,customer,product,quantity,price,total_revenue,date)
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (order_id) DO NOTHING"""
            ).format(table=sql.Identifier(table_name))

        for row in valid_rows:
                print(row)
                cursor.execute(insert_table_query, (
                    row['order_id'],
                    row['customer'],
                    row['product'],
                    row['quantity'],
                    row['price'],
                    row['total_revenue'],
                    row['date']
                ))
        
        connexion.commit()
        logging.info('New rows inserted, duplicated ignored')
        
    except Exception as error:
        logging.error(f"unexpected error: {error}")
        raise
    finally:
        if cursor:
             cursor.close()
        if connexion:
            connexion.close()
            print('Database connection closed')
