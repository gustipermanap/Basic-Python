#teks = "semuanya disebut "la vie en rose" adalah" --------->salah
teks = "semuanya disebut \"la vie en rose\" adalah" #---------> benar
teks = "semuanya disebut \'la vie en rose\' adalah" #---------> benar
teks = "semuanya disebut \?la vie en rose\? adalah" #---------> benar
teks = "semuanya disebut \\la vie en rose\\ adalah" #---------> benar
teks = "semuanya disebut \tla vie en rose\t adalah" #---------> benar
print(teks)