# instagram.com/cancakar35
# Caesar cipher


def encrypt(text):
    crypted = ""
    for i in text:
        if i.isalpha():
            if i in ["X", "Y", "Z", "x", "y", "z"]:
                i = chr(ord(i)-23)
            else:
                i = chr(ord(i)+3)
        crypted += i
    return crypted

def decrypt(crypted):
    text = ""
    for j in crypted:
        if j.isalpha():
            if j in ["A", "B", "C", "a", "b", "c"]:
                j = chr(ord(j)+23)
            else:
                j = chr(ord(j)-3)
        text += j
    return text

op = input("Encrypt/Decrypt (E/D): ").lower()
if op == "e":
    text = input("Metni girin: ")
    print(encrypt(text))
elif op == "d":
    crypted = input("Sifrelenmis metin: ")
    print(decrypt(crypted))
else:
    print("Hatalı giriş!")
