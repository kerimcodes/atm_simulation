###MİNİ PROJE ATM SİMÜLASYONU
bakiye= 0
dogru_pin = "1234"
giris_hakki = 3
dil_sözlugu=()
islem_gecmisi=[]
# Dil haznesi
TR = {"bakiye":"Bakiyeniz:",
      "yatirilacak_para":"Yatırmak istediğiniz tutarı giriniz:",
      "yatırım_onay":"Paranız yatırıldı.",
      "çekilecek_para":"Çekmek istediğiniz tutarı giriniz:",
      "yetersiz_bakiye":"Hesabınızda yeterli bakiye bulunmamaktadır.",
      "max_tutar":"Çekebileceğiniz max bakiye:",
      "çekim_onay":"Paranız çekildi,Kalan bakiye:",
      "pin":"Lütfen 4 haneli PIN kodunuzu giriniz:",
      "giriş_onay":"Giriş başarılı!",
      "giriş_hata":"Yanlış PIN,Kalan deneme hakkı:",
      "kitlenme":"Hesabınız kilitlendi.",
      "menü":"Ana menüye hoşgeldiniz",
      "seçim_1":"1. Bakiye Görüntüleme",
      "seçim_2":"2. Para Yatır",
      "seçim_3":"3. Para Çek",
      "seçim_4":"4. Geçmiş işlemleri görüntüleme",
      "seçim_5":"5. Çıkış",
      "seçim_yap":"Seçiminizi yapınız:",
      "çıkış_onay":"Çıkış yapılıyor",
      "seçim_hata":"Hatalı seçim yapıldı",
      "bakiye_goruntuleme":"Bakiye görüntülemesi yapıldı.",
      "geçmiş_yatırım":"tutarında para yatırıldı.",
      "geçmiş_çekme":" tutarında para çekildi.",
      "sayi_gir":"Lütfen sayı giriniz."
}
ENG ={
  "bakiye": "Your balance:",
  "yatirilacak_para": "Enter the amount you want to deposit:",
  "yatırım_onay": "Your money has been deposited.",
  "çekilecek_para": "Enter the amount you want to withdraw:",
  "yetersiz_bakiye": "Insufficient balance in your account.",
  "max_tutar": "Maximum amount you can withdraw:",
  "çekim_onay": "Your money has been withdrawn, Remaining balance:",
  "pin": "Please enter your 4-digit PIN:",
  "giriş_onay": "Login successful!",
  "giriş_hata": "Wrong PIN, Remaining attempts:",
  "kitlenme": "Your account is locked.",
  "menü": "Welcome to the main menu",
  "seçim_1": "1. View Balance",
  "seçim_2": "2. Deposit Money",
  "seçim_3": "3. Withdraw Money",
   "seçim_4":"4. View past transactions",
  "seçim_5": "5. Exit",
  "seçim_yap": "Make your selection:",
  "çıkış_onay": "Exiting...",
  "seçim_hata": "Invalid selection",
  "bakiye_goruntuleme": "Balance has been viewed.",
  "geçmiş_yatırım": "has been deposited.",
  "geçmiş_çekme": "has been withdrawn.",
  "sayi_gir":"Please enter number"
}
##Dil Seçim
while True:
 dil=input("Dili seçiniz/Select your language(tr/eng):")
 if dil.lower()=="tr":
   dil_sözlugu=TR
   break
 elif dil.lower()=="eng":
   dil_sözlugu=ENG
   break
 else:
   print("Hatalı tercih yaptınız/You made a wrong choice")
#Fonksiyonlarla işlemleri hazırlama 
def bakiye_göruntule():
   print(dil_sözlugu["bakiye"],bakiye)
   islem_gecmisi.append(dil_sözlugu["bakiye_goruntuleme"])

def para_yatir():
  global bakiye
  while True:
    try: 
      yatirilacak_para= int(input(dil_sözlugu["yatirilacak_para"]))
    except ValueError:
      print(dil_sözlugu["sayi_gir"])
      continue    
    bakiye+=yatirilacak_para
    islem_gecmisi.append(f'{yatirilacak_para} TL {dil_sözlugu["geçmiş_yatırım"]}')
    print(dil_sözlugu["yatırım_onay"])
    break

def para_cek():
  global bakiye
  while True:
      try:
        cekilecek_para=int(input(dil_sözlugu["çekilecek_para"]))
      except ValueError:
        print(dil_sözlugu["sayi_gir"])
        continue
      if bakiye<cekilecek_para:
        print(dil_sözlugu["yetersiz_bakiye"])
        print(dil_sözlugu["max_tutar"],bakiye)
        
      else:
        bakiye-=cekilecek_para
        islem_gecmisi.append(f'{cekilecek_para} TL {dil_sözlugu["geçmiş_çekme"]}')
        print(dil_sözlugu["çekim_onay"],bakiye)
        break

def islem_gecmis_goruntuleme():
   sayi=1
   for islem in islem_gecmisi:
      print(f"{sayi}-{islem}")
      sayi+=1

# Hesaba giriş
while giris_hakki > 0:
    pin = input(dil_sözlugu["pin"])
    if pin == dogru_pin:
        print(dil_sözlugu["giriş_onay"])
        break
    else:
        giris_hakki -= 1
        print(f"{dil_sözlugu['giriş_hata']} {giris_hakki}")
        if giris_hakki == 0:
            print(dil_sözlugu["kitlenme"])
            exit()

#Ana Menü ekranı
while True:
 print(dil_sözlugu["menü"])
 print(dil_sözlugu["seçim_1"])
 print(dil_sözlugu["seçim_2"]) 
 print(dil_sözlugu["seçim_3"])
 print(dil_sözlugu["seçim_4"])
 print(dil_sözlugu["seçim_5"])
#Seçime göre işlem yapma
 try:
  secim=int(input(dil_sözlugu["seçim_yap"]))
 except ValueError:
   print(dil_sözlugu["sayi_gir"])
   continue
 if secim==1:
   bakiye_göruntule()
 elif secim==2:
    para_yatir()
 elif secim==3:
   para_cek()
 elif secim==4:
   islem_gecmis_goruntuleme()
 elif secim==5:
   print(dil_sözlugu["çıkış_onay"]) 
   break
 else:
   print(dil_sözlugu["seçim_hata"])