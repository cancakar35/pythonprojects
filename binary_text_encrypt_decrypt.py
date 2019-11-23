#!/usr/bin/env python
# -*- coding: utf-8 -*-

# github.com/cancakar35

def encrypt(text):
    crypted_text = ""
    for i in text:
        i = bin(ord(i))
        i = i.replace("b", "")
        crypted_text += i + " "
    return crypted_text

def decrypt(crypted_text): # Şifre çözmek için her 8 binary kodu sonrası boşluk olmalıdır
    crypted_text = crypted_text.split(" ")
    text = ""
    for i in crypted_text:
        text += chr(int(i, 2))
    return text


while True:
    try:
        op = input("Çıkmak için q, Şifreleme için 0, Şifre çözümü için 1 giriniz: ")
        if op == "q":
            break
        elif op == "0":
            text = input("Şifrelenecek metni girin: ")
            print(encrypt(text))
        elif op == "1":
            crypted = input("Şifreyi çözmek için içeriği girin: ")
            print(decrypt(crypted))
            pass
        else:
            print("Lütfen geçerli bir işlem giriniz!")
            continue
    except (TypeError, ValueError):
        print("Hata oluştu. Lütfen türkçe karakter kullanmayın!")
