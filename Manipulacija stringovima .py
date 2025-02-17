ime_korisnika = input("Upisi svoje ime i prezime: ")  		#detekcija imena, ako ima razmak ocigledno su 2 "sloga"
email_korisnika = input("Unesi svoj e-mail: ")
sifra_korisnika = input("Unesi svoju lozinku: ")

#detekcija imena.Ime se sastoji od imena i prezimena i mora imati razmak.
#Moramo paziti na logicku grešku, ako korisnik napise ime i samo "lupi" razmak.
#Brojac razmaka i njegov uvjet će biti zadovoljeni, ali logički neće biti ispravno


ime_korisnika = ime_korisnika.strip()			# skida "lažne razmake"
broj_razmaka = ime_korisnika.count (" ")
ime_korisnika = ime_korisnika.lower()			#smanjiti sve na mala slova
ime_korisnika = ime_korisnika.title()			#title() sluzi za pocetna velika slova

if broj_razmaka > 0 :
	print("Ime je potpuno!")
else :
	print("Ime je nepotpuno!")



duzina_sifre =len(sifra_korisnika)				#mjerenje duzine sifre

#ovim if-om ispitivao duzinu na pocetku, kasnije prebacio ispod da pokrijem vise uvjeta
#if duzina_sifre > 8:							
#	print("Sifra zadovoljava uvijete!")
#else :
#	print("Sifra mora biti duza od 8 karaktera!")

#Zelimo postaviti pravilo da sifra ne smije sadrzavati ime korisnika radi sigurnosti
#Ako pretpostavimo da je ime uvijek prva riječ, a prezime druga, moramo izdvojiti prvu rijec.
#Kraj prve rijeci je zapravo razmak

razmak = ime_korisnika.find(" ")			# pronalazenje razmaka
ime = ime_korisnika[:razmak]				# prije : je prazno da podrazumjeva pocetak

lokacija_imena = sifra_korisnika.lower().find(ime.lower())	#ako je -1 rezulat, nema imena, svaka ostala vrijednost prikazuje poziciju imena

if lokacija_imena == -1 and duzina_sifre > 0:
	print("Sifra zadovoljava uvjete!")
else :
	print("Sifra ne zadovoljava uvjete!")


#VALIDACIJA E-MAIL ADRESE
#svaki mail mora imati @ i .

at = email_korisnika.find("@")
tocka = email_korisnika.find(".")

if at == -1 or tocka == -1:
	print("E-mail adresa nije ok.")
else :
	print("Email adresa je ok!")							