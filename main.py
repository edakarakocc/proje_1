import islemler #islemler.py modülü main.py dosyasına dahil edilir

def menu_goruntule():
    print('''
    1.Yeni katılımcı ekle
    2.Kayıtlı katılımcı bilgilerini görüntüle
    3.Otomatik giriş kodu ve şifre oluştur
    4.Anlık giriş kodu ve şifre üret
    5.Çıkış''')

def main():
    while True:
        
        menu_goruntule() #oluşturulan menü menu_goruntule() fonksiyonu ile çağırılır
       
        tercih = input("Lütfen bir seçenek girin: ")
        
        if tercih== "5": #'5' girildiği zaman programın sonlanmasını sağlar
            break
        elif tercih == "1":
            islemler.yeni_katilimci()
        elif tercih == "2":
            girilen_ID = input("Katılımcı ID'sini giriniz:")
            islemler.katilimci_getir(girilen_ID)
        elif tercih == "3":
            girilen_ID = input("Katılımcı ID'sini giriniz:")
            islemler.girisKodu_sifre_uret(girilen_ID)
        elif tercih == "4":
            bilgiler=input("İsim,Soyisim,ID,Doğum ayı girişi yapınız (virgül kullanarak yazınız):")
            islemler.anlik_uret(bilgiler)
        else:
            print("Yanlış tercihte bulundunuz.")

if __name__ == "__main__":
    main()