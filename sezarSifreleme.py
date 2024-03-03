alfabe=["a","b","c","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
deger = input("Lütfen kelimeyi giriniz")
sonuc=""

for i in deger:
    if alfabe.index(i)<26:
        sonuc+=alfabe[alfabe.index(i)+3]
    else:
        sonuc+=alfabe[alfabe.index(i)%25]
print(sonuc)
