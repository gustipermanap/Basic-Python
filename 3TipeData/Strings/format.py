umur=31
kalimat="Nama saya Arif dan saya {} tahun"
print(kalimat.format(umur))


kuantitas = 3
no = 2
harga = 55500
order = "saya ingin order {} buah item nomor {} dengan harga {} rupiah."
print(order.format(kuantitas,no,harga))


kuantitas = 3
no = 2
harga = 55500
order = "saya ingin order {1} buah item nomor {0} dengan harga {2} rupiah."
print(order.format(no, kuantitas,harga))