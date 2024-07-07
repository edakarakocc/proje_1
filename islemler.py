#yeni bir katılımcı eklenmesini sağlayan fonksiyon
def yeni_katilimci(): 
    try:
        katilimci_bilgileri = open('MuhendisFest2024-Katılımcılar.txt','a') #MuhendisFest2024-Katılımcılar.txt dosyasını 'a' ekleme modunda açar
        kontrol = open('MuhendisFest2024-Katılımcılar.txt','r') #MuhendisFest2024-Katılımcılar.txt dosyasını 'r' okuma modunda açar
        
        katilimci_adi = input("Katılımcının Adı:")
        katilimci_soyadi = input("Katılımcının Soyadı:")
        katilimci_ID = input("Katılımcı ID:")
        
        IDler=kontrol.readlines() #kontrol değişkenine atanmış olan MuhendisFest2024-Katılımcılar.txt dosyasının satırlarını okur
        while True: #aynı ID'nin tekrardan kullanılmasını önlemek için break ile kırılana kadar çalışan bir döngü oluşturulur
            id_kontrolu = False #başlangıçta 'False' olduğu kabul edilen bir bayrak oluşturulur
            
            for satir in IDler: #IDler içerisindeki satırlara bakar
                if satir.strip().split(",")[2] == katilimci_ID: 
                    katilimci_ID=input("Başka bir ID giriniz:")
                    id_kontrolu = True #eğer aynı ID dosyanın içerisinde bulunuyorsa bayrak 'True' olur
                    break
            
            if id_kontrolu == False: #döngü içerisinde bayrak tekrardan 'False' olduğunda döngüyü sonlandırır
                break
        
        katilimci_dogum_ayi = input("Katılımcının Doğum Ayı (1-12):")
        katilimci_bilgileri.write(f"{katilimci_adi},{katilimci_soyadi},{katilimci_ID},{katilimci_dogum_ayi}\n") #alınan bilgileri MuhendisFest2024-Katılımcılar.txt dosyasına yazar
        print("Katılımcı eklendi.")

    except Exception as err: #herhangi bir hata durumunda hata mesajı yazdırır
        print(err)


#önceden kayıt olmuş bir katılımcının bilgilerini yazdıran fonksiyon
def katilimci_getir(girilen_ID):
    try:
        katilimci_bilgileri = open('MuhendisFest2024-Katılımcılar.txt','r') #MuhendisFest2024-Katılımcılar.txt dosyasını 'r' okuma modunda açar
        
        for satir in katilimci_bilgileri: #katilimci_bilgileri içerisindeki satırlara bakar
            kullanici_bilgileri=satir.strip().split(",") #satırlar içerisindeki boşlukları ve virgülleri kaldırır
            
            if kullanici_bilgileri[2] == girilen_ID: #okunan satırların 2.indexi olan katilimci_ID'si ile girilen_ID yi karşılaştırır
                print("\nKatılımcı Bilgileri") 
                #uygun olan satır bulunduktan sonra satır içerisindeki ögeler indexlerine göre ekrana yazdırılır
                print("Ad:",kullanici_bilgileri[0]) 
                print("Soyad:",kullanici_bilgileri[1])
                print("ID:",kullanici_bilgileri[2])
                print("Doğum Ayı:",kullanici_bilgileri[3])      
                break  
        
        else:
            print("Girilen ID'ye sahip katılımcı bulunamadı.")
    
    except Exception as err: #herhangi bir hata durumunda hata mesajı yazdırır
        print(err)


#önceden kayıt yaptırmış katılımcılar için şifre oluşturan fonksiyon
def girisKodu_sifre_uret(girilen_ID):
    try:
        katilimci_bilgileri = open('MuhendisFest2024-Katılımcılar.txt','r') #MuhendisFest2024-Katılımcılar.txt dosyasını 'r' okuma modunda açar
        sifre_dosyasi = open('girisKodu_sifre.txt','a') #girisKodu_sifre.txt dosyasını 'a' ekleme modunda açar
        
        for satir in katilimci_bilgileri: #katilimci_bilgileri içerisindeki satırlara bakar
            kullanici_bilgileri=satir.strip().split(",") #satırlar içerisindeki boşlukları ve virgülleri kaldırır
            
            if kullanici_bilgileri[2]== girilen_ID: #okunan satırların 2.indexi olan katilimci_ID'si ile girilen_ID yi karşılaştırır
                #katilimci_adi'nın ilk harfini, katilimci_soyadi'nın son harfini, katilimci_ID'si ile katilimci_dogum_ayi'nın çarpımını ve katilimci_ID'sinin ilk iki rakamını birleştirerek şifre oluşturur
                sifre = kullanici_bilgileri[0][0] + kullanici_bilgileri[1][-1] + str(int(kullanici_bilgileri[2])*int(kullanici_bilgileri[3]))+kullanici_bilgileri[2][:2]
                
                sifre_dosyasi.write(f"{kullanici_bilgileri[2]},{sifre}\n") #şifreyi katilimci_ID'si ile birlikte girisKodu_sifre.txt dosyasına yazar
                print("Şifre oluşturuldu.")
                break
        else:
            print("Girilen ID'ye sahip katılımcı bulunamadı.")
    
    except Exception as err: #herhangi bir hata durumunda hata mesajı yazdırır
        print(err)
        

#anlık olarak kullanıcıdan alınan bilgilere göre şifre üreten fonksiyon     
def anlik_uret(bilgiler):
    kullanici_bilgileri=bilgiler.lower().strip().split(",") #kullanıcıdan alınan aralarında virgül bulunan bilgilerin tüm harflerini küçük yapar,başlangıcında ve sonunda bulunan boşlukları siler ve aralarındaki virgülleri kaldırır
    
    #alınan bilgilerin 0.indexinin ilk harfi,1.indexinin son harfi,2.index ile 3.indexin çarpımı ve 2.indexin ilk 2 rakamı alınarak anlık bir şifre oluşturulur
    sifre = kullanici_bilgileri[0][0] + kullanici_bilgileri[1][-1] + str(int(kullanici_bilgileri[2])*int(kullanici_bilgileri[3]))+kullanici_bilgileri[2][:2]
    print(f"Oluşturulan şifre: {sifre}") #şifre ekrana yazdırılır