import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="Password123#@!"
)

cursor = db.cursor()
cursor.execute("create database toko_mainan")

print("Database berhasil dibuat!")