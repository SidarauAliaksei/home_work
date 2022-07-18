import mysql.connector as mysql

db_orders = mysql.connect(
    host="localhost",
    user="root",
    passwd="Sdv290590",
    database='db_orders'
)
cursor = db_orders.cursor()
# cursor.execute("CREATE DATABASE test_db_orders")
# cursor.execute(
#     """CREATE TABLE orders (ord_number VARCHAR(255),purch_amt VARCHAR(255),ord_date VARCHAR(255),
#         customer_id VARCHAR(255), salesman_id VARCHAR(255))""")
# query = "INSERT INTO orders (ord_number, purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s)"
# values = [
#     (70001, 150.5, "2012-10-05", 3005, 5002),
#     (70009, 270.65, "2012-09-10", 3001, 5005),
#     (70002, 65.26, "2012-10-05", 3002, 5001),
#     (70004, 110.5, "2012-08-17", 3009, 5003),
#     (70007, 948.5, "2012-09-10", 3005, 5002),
#     (70005, 2400.6, "2012-07-27", 3007, 5001),
#     (70008, 5760, "2012-09-10", 3002, 5001),
#     (70010, 1983.43, "2012-10-10", 3004, 5006),
#     (70003, 2480.4, "2012-10-10", 3009, 5003),
#     (70012, 250.45, "2012-06-27", 3008, 5002),
#     (70011, 75.29, "2012-08-17", 3003, 5007),
#     (70013, 3045.6, "2012-04-25", 3002, 5001)
# ]
#
# cursor.executemany(query, values)
# db_orders.commit()

query = "SELECT ord_number, ord_date, purch_amt  FROM orders WHERE salesman_id = 5002"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT DISTINCT salesman_id FROM orders"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT ord_date, salesman_id, ord_number, purch_amt FROM orders ORDER BY ord_date ASC"
cursor.execute(query)
print(cursor.fetchall())

query = "SELECT * FROM orders WHERE ord_number BETWEEN 70002 AND 70006 ORDER BY ord_number ASC"
cursor.execute(query)
print(cursor.fetchall())

db_orders.close()
