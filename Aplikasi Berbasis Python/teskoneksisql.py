import mysql.connector

koneksi = mysql.connector.connect(user='ostechnix', passwd='Password123#@!',
                                   host='localhost',
                                   database='aset')

print ("koneksi telah berhasil dilakukan")
koneksi.close

