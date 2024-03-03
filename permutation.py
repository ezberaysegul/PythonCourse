def Faktoriyel (sayi1):
    if(sayi1==1):
        sonuc=1
    else:
        sonuc=sayi1*Faktoriyel(sayi1-1)
    return sonuc
        
    
def Permutation(n,r):
    sonuc = Faktoriyel(n)/Faktoriyel(n-r)
    return sonuc


print(Permutation(15,7))