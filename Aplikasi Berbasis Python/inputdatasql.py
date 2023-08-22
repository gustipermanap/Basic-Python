import mysql.connector

nama_db={'user':'ostechnix', 'passwd':'Password123#@!',
                                   'host':'localhost',
                                   'database':'aset'}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute("""insert ignore into aset_kantor values('131234','Monitor','2023-12-20','Rhino',500000.00),
                                                ('122341','Laptop','2023-12-20','HP',3500000.00);""")
koneksi.autocommit
print("data udah ditambahin !!!!!!!!!!!!!!!")
koneksi.close()
