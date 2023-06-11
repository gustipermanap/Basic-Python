#numerik            -   int, float, dan complex
#urutan (sekuens)   -   list,tuple,range
#mapping            -   dict
#set                -   set, frozenset
#Boolean            -   bool
#Biner              -   bytes, bytearray, memoryview
#tanpa tipe         -   none type

a="ini string"                          #==========================>str bisa menggunakan ', " atau ''' untuk text panjang
b=20                                    #==========================>int bilangan bulan bisa menggunakan -348
c=20.5                                  #==========================>float pecahan atau decimal + / - juga memfasilitasi 'e' sebagai 10 pangkat contoh : t=1e-2(maksudnya 1x10pangkat-2)
d=1j                                    #==========================>complex dua bilangan menjadi komponen real dan imajiner, 3+4j
e=["apple","lenovo", "asus"]            #==========================>list
f=("apple","lenovo", "asus")            #==========================>tuple
g=range(8)                              #==========================>range
h={"name":"Gusti","age":32}             #==========================>dict
i={"apple","lenovo", "asus"}            #==========================>set
j=frozenset({"apple","lenovo", "asus"}) #==========================>frozenset
k=True                                  #==========================>bool
l=b"hello"                              #==========================>bytes
m=bytearray(5)                          #==========================>bytearray
n=memoryview(bytes(5))                  #==========================>memoryview
o=None                                  #==========================>Nontype

print(type(a)) #ganti alfabet a-o yang sudah di definisikan