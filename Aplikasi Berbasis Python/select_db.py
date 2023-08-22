import mysql.connector

nama_db={'user':'ostechnix', 
         'passwd':'Password123#@!',
         'host':'localhost',
         'database':'aset'}
sambungan=mysql.connector.connect(**nama_db)
arahin=sambungan.cursor()

arahin.execute("""select * from aset_kantor""")
print('Kode','Nama','Tanggal Beli','Merk','Nilai'),

for (column) in arahin:
    print(column[0],column[1],column[2],column[3],column[4]),
    
sambungan.close()