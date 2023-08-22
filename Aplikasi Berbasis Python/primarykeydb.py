import mysql.connector

nama_db={'user':'gusti', 'passwd':'Password123#@!',
                                   'host':'localhost',
                                   'database':'aset'}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()
kursor.execute("""alter table aset_kantor add primary key(kode);""")

for (column) in kursor:
    print (column[0]),
    print (column[1]),
    print (column[2]),
    print (column[3]),

koneksi.close()