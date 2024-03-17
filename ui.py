#from ui import UI

try:
     no=1
     while True:
         print(""" 
      --------------------------------
     |1....Ülke Bilgileri Getir       |
     |2....Telefon Kodundan Ülke Bul  |      
     |3....Kıtadaki Ülkeleri Say      |  
     |4....Para Biriminden Ülke Bul   |   
     |5....Çıkış                      |
     ---------------------------------
     """)
         secim=int(input("Lütfen seçiminizi giriniz[1-6] : "))
    
except ValueError:
    print("Lütfen bir tamsayı giriniz.")
except:
    print("Lütfen 1-5 arasında bir sayı giriniz.")
    
