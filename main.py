import os
# TODO:bilgilendirme mesajlarının düzeltilmesi.
# TODO:DONE check edilmiş görevi düzelt.
print("**************to do list*****************")
cikis = ""
while cikis != "exit":
    # TODO:DONE KÜÇÜK BÜYÜK HARF İKİSİDE GİRİLMELİ İKİSİDE ÇALIŞMALI.
    islem = input("İşleminizi giriniz(add/delete/check/replace/list/exit):")
    #*****************add********************
    # TODO:DONE add komutundan sonra görev eklenmeden geçememeli.
    if islem.lower() == "add":
        adet = 0
        if os.path.isfile("belge.txt"):
            file = open("belge.txt","r")
            lines = file.readlines()
            file.close()
            adet = len(lines)
        file = open("belge.txt","a")
        inp = input("görev giriniz:")
        if len(inp) > 0:
            file.write("x "+f"{adet + 1}. " + inp + "\n") or file.write("v "+f"{adet + 1}. " + inp + "\n")
            file.close()
        else:
            print("yanlis islem...")
    #*****************delete****************
    # TODO:DONE boş görev numarası verilir ise hepsini siliyor. rakam zorunlu olmalı.
    # TODO:DONE eğer metin içerisinde de o rakam geciyor ise onu tiklemesi engellenmeli.
    elif islem.lower() == "delete":
        file = open("belge.txt","r")
        lines = file.readlines()
        file.close()
        c = True
        silinecek = input("silmek istediğiniz görev:")
        if len(silinecek) == 0:
            c = False
        for karakter in silinecek:
            if not karakter in "0123456789":
                c = False
        if c:
            file = open("belge.txt","w")
            tut1 = 1
            for line in lines:
                if not tut1 == int(silinecek):
                    file.write(line)
                tut1 += 1
            file.close()
        else:
            print("yanlış işlem...")
    #*****************check***************
    # TODO:DONE boşluk girildiğinde hepsine tik koyuyor. ve sadece görev numarası girilmeli.
    # TODO:DONE eğer metin içerisinde de o rakam geciyor ise onu tiklemesi engellenmeli.
    elif islem.lower() == "check":
        file = open("belge.txt","r")
        lines = file.readlines()
        file.close()
        a = True
        tik = input(" bitirdiğiniz görevi giriniz:")
        if tik == "":
            a = False
        for karakter1 in tik:
            if not karakter1 in "0123456789":
                a = False
        if a:
            file = open("belge.txt","w+")
            tut = 1
            for line in lines:
                if tut == int(tik):
                    file.write(line.replace("x","v"))
                else:
                    file.write(line)
                tut += 1
            file.close()
            a = False
        else:
            print("yanlış işlem...")
            a = False
    #*************replace***************
    elif islem.lower() == "replace":
        file = open("belge.txt","r")
        lines = file.readlines()
        file.close()
        a = True
        tik1 = input("düzeltilecek görevi giriniz:")
        if tik1 == "":
            a = False
        for karakter2 in tik1:
            if not karakter2 in "0123456789":
                a = False
        if a:
            file = open("belge.txt","w+")
            tut = 1
            for line in lines:
                if tut == int(tik1):
                    file.write(line.replace("v","x"))
                else:
                    file.write(line)
                tut += 1
            file.close()
            a = False
        else:
            print("yanlış işlem...")
            a = False
    #*************list***************
    elif islem.lower() == "list":
        file = open("belge.txt","r")
        for i in file:
            print(i)
        file.close()
    #************çıkış************
    elif islem.lower() == "exit":
        cikis = "exit"
    #*****************************
    else:
        print("yanlış işlem...")