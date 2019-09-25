def score(val):
	val = val.lower()
	if val == 'a': return 4.0
	elif val == 'ab': return 3.5
	elif val == 'b': return 3.0
	elif val == 'bc': return 2.5
	elif val == 'c': return 2.0
	elif val == 'd': return 1.0
	elif val == 'e': return 0
kalkulus = score(input("Masukan nilai Kalkulus : "))
fisika = score(input("Masukan nilai fisika : "))
daspro = score(input("Masukan nilai Dasar Pemrograman : "))
daskom = score(input("Masukan nilai Dasar Komputer : "))
bing = score(input("Masukan nilai Bahasa Inggris : "))
agama = score(input("Masukan nilai Pendidikan Agama : "))
pti = score(input("Masukan nilai Pengantar Teknologi Informasi : "))
hitung = (kalkulus * 4 + fisika * 4 + daspro * 4 + daskom * 2 + bing * 2 + agama * 2 + pti * 2)/20
print("=========================================================")
print("IPK KAMU ADALAH : ", hitung)