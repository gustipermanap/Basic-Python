import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="Password123#@!",
  database="toko_mainan"
)

cursor = db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)
