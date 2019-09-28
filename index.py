def konverter(val):
	if 4 >= val > 3.5: return 'A' 
	elif 3.5 >= val > 3: return 'AB'
	elif 3 >= val > 2.5: return 'B'
	elif 2.5 >= val > 2: return 'BC'
	elif 2 >= val > 1.5: return 'C'
	elif 1.5 >= val > 1: return 'D'
	elif 1 >= val: return "E"
kalkulus = float(input("Masukan nilai Kalkulus : "))
fisika = float(input("Masukan nilai fisika : "))
daspro = float(input("Masukan nilai Dasar Pemrograman : "))
daskom = float(input("Masukan nilai Dasar Komputer : "))
bing = float(input("Masukan nilai Bahasa Inggris : "))
agama = float(input("Masukan nilai Pendidikan Agama : "))
pti = float(input("Masukan nilai Pengantar Teknologi Informasi : "))
total = (kalkulus * 4 + fisika * 4 + daspro * 4 + daskom * 2 + bing * 2 + agama * 2 + pti * 2)/20
print("\n=========================================================\n")

print("Nilai Kalkulus\t\t: {} ({})".format(kalkulus, konverter(kalkulus)))
print("Nilai fisika		: {} ({})".format(fisika, konverter(fisika)))
print("Nilai daspro		: {} ({})".format(daspro, konverter(daspro)))
print("Nilai daskom		: {} ({})".format(daskom, konverter(daskom)))
print("Nilai bing		: {} ({})".format(bing, konverter(bing)))
print("Nilai agama		: {} ({})".format(agama, konverter(agama)))
print("Nilai pti		: {} ({})".format(pti, konverter(pti)))
print("===========================")
print("Nilai IPK		: {} ({})".format(round(total, 2), konverter(total)))