namirnica = ""
popis_namirnica=[]



print ("Za kraj unosa unesite broj 0")
while namirnica != "0" :
	namirnica=input("Unesi namirnicu: ")
	if namirnica != "0":
		popis_namirnica.append(namirnica)
print("Ovo je lista namirnica!")


for i,clan in enumerate(popis_namirnica):
	print (f"Pozicija: {i} - Brend: {clan}")
	

ukloniti=input("Da li zelite ukloniti neku namirnicu iz popisa? (da/ne)")

if ukloniti == "da" :
	pozicija = int(input("Sa koje pozicije zelite ukloniti namirnicu?(Unesite broj: ) "))

	print ("Uklanjamo ovaj element: ", pozicija)
	print ("Clan na poziciji je: ", popis_namirnica[pozicija])

	popis_namirnica.pop(pozicija)

print ("Finalni popis je: ",popis_namirnica)