try:
    sayi1=int (input("Lütfen 1. sayıyı giriniz: "))
    sayi2=int (input("Lütfen 2. sayıyı giriniz: "))
    sonuc=sayi1/sayi2
    print(f"işleminin sonucu {sonuc}")
except ZeroDivisionError:
    print("Hiçbir sayı sıfıra bölünemez.")
except ValueError:
    print("Lütfen bir tamsayı giriniz.")
except :
    print("Bir hata oluştu.")
else:
    print("İşlem başarılı.")
finally:
    print("Program sonlandırıldı...")
    