from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

data_aset={
    'kode':'15235',
    'nama':'Meja Sekretaris',
    'tgl_beli': date(2023, 10, 14),
    'merk':'Champion',
    'nilai':'3250000'
}

nama_db={'user':'ostechnix', 
         'passwd':'Password123#@!',
         'host':'localhost',
         'database':'aset'}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

tambah_db = ("insert into aset_kantor "
             "(kode, nama, tgl_beli, merk, nilai)"
             "values(%(kode)s, %(nama)s, %(tgl_beli)s, %(merk)s, %(nilai)s)")
kursor.execute(tambah_db, data_aset)
koneksi.commit()
koneksi.close()