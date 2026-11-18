import sqlite3

conn = sqlite3.connect("data/ecommerce.db")

cursor = conn.cursor()

cursor.execute("Select * from dim_products")

for row in cursor:
    print(row)
    
conn.close()