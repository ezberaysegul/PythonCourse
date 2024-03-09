class Araba():
    def __init__(self,marka,model,renk,durum=False): #yapıcı metot
        self.marka=marka
        self.model=model
        self.renk=renk
        self.durum=durum
        print("Nesne oluşturuldu...")
        
    def marka_atama(self,yeni_marka):
        self.marka=yeni_marka
    def renk_atama(self,yeni_renk):
        self.renk=yeni_renk
    def model_atama(self,yeni_model):
        self.model=yeni_model
    def durum_atama(self,yeni_durum):
        self.durum=yeni_durum
    def calistir(self):
        self.durum=True
        print("Araba çalıştı")
    def durdur(self):
        self.durum=False
        print("Araba durdu")
    def durumu_yazdir(self):
        print(self.durum)
    def __del__ (self):#yıkıcı fonksiyon
        print("Nesne silindi...")
         
"""
sedan=Araba() #araba sınıfına ait sedan nesnesi oluşturuldu.
print(sedan.marka)
sedan.durumu_yazdir()

sedan.marka_atama("Toyota")
sedan.calistir()
print(sedan.marka)
sedan.durumu_yazdir()

sedan.durdur()
print(sedan.marka)
sedan.durumu_yazdir()

"""

sedan=Araba("Toyota","Corolaa","Beyaz")
sedan.durumu_yazdir()

###

del sedan
sedan.durumu_yazdir()
