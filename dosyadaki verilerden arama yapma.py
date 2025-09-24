DOSYA_YOLU = "C:\Users\ismet\Desktop\Deneme1.txt" # Dosyanın tam yolu

# Dosyayı yazma modunda aç (encoding kullanılmaz)
dosya = open(DOSYA_YOLU, "w")

i = 1
while i <= 5:  # 25 kayıt yapılacak
    print("\n" + str(i) + ". Kayıt:")

    ad = input("Ad: ").strip()
    soyad = input("Soyad: ").strip()

    # Telefon numarası kontrolü
    while True:
        telefon = input("Telefon (05XXXXXXXXX): ").strip()
        rakamlar = "0123456789"
        sadece_rakam = True
        for karakter in telefon:
            if karakter not in rakamlar:
                sadece_rakam = False
                break
        if telefon.startswith("05") and len(telefon) == 11 and sadece_rakam:
            break
        else:
            print("Hatalı telefon! 05 ile başlamalı, 11 hane ve sadece rakam olmalı.")

    # Doğum yeri kontrolü
    while True:
        dogum_yeri = input("Doğum Yeri: ").strip()
        sadece_harf = True
        for harf in dogum_yeri:
            if not ((harf >= "A" and harf <= "Z") or (harf >= "a" and harf <= "z")):
                sadece_harf = False
                break
        if sadece_harf and len(dogum_yeri) > 0:
            break
        else:
            print("Geçersiz doğum yeri! Sadece harflerden oluşmalı.")

    # Doğru kayıt dosyaya yazılır
    kayit = ad + "," + soyad + "," + telefon + "," + dogum_yeri + "\n"
    dosya.write(kayit)
    i += 1

dosya.close()  # Kayıt işlemi bitince dosya kapatılır

# --- Arama bölümü ---
while True:
    print("\nArama Türleri:")
    print("1. Ada göre")
    print("2. Soyada göre (tam eşleşme)")
    print("3. Telefon başlangıcına göre")
    print("4. Doğum yerine göre (tam eşleşme)")
    print("5. Çıkış")
    secim = input("Seçiminiz (1-5): ").strip()

    if secim == "5":
        print("Program sonlandırıldı.")
        break

    kriter = input("Arama kriterini girin: ").strip().lower()
    bulunanlar = []

    dosya = open(DOSYA_YOLU, "r")  # Dosya okuma modunda açılır
    for satir in dosya:
        satir = satir.strip()
        parcalar = satir.split(",")
        if len(parcalar) != 4:
            continue
        ad = parcalar[0].strip()
        soyad = parcalar[1].strip()
        telefon = parcalar[2].strip()
        dogum_yeri = parcalar[3].strip()

        # Kullanıcının seçimine göre eşleştirme yapılır
        if secim == "1" and kriter in ad.lower():
            bulunanlar.append(satir)
        elif secim == "2" and kriter == soyad.lower():
            bulunanlar.append(satir)
        elif secim == "3" and telefon.startswith(kriter):
            bulunanlar.append(satir)
        elif secim == "4" and kriter == dogum_yeri.lower():
            bulunanlar.append(satir)

    dosya.close()

    print("\nToplam " + str(len(bulunanlar)) + " kayıt bulundu.\n")
    for kayit in bulunanlar:
        print(kayit)

    tekrar = input("\nYeni bir arama yapmak ister misiniz? (e/h): ").strip().lower()
    if tekrar != "e":
        print("Arama işlemi sonlandırıldı.")
        break
