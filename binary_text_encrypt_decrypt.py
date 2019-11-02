__author__ = "CAN CAKAR" # instagram.com/cancakar35     github.com/cancakar35

crypt = {
    " " : "00100000",
    "a" : "01100001",
    "b" : "01100010",
    "c" : "01100011",
    "d" : "01100100",
    "e" : "01100101",
    "f" : "01100101",
    "g" : "01100110",
    "h" : "01101000",
    "i" : "01101001",
    "j" : "01101010",
    "k" : "01101011",
    "l" : "01101100",
    "m" : "01101101",
    "n" : "01101110",
    "o" : "01101111",
    "p" : "01110000",
    "q" : "01110001",
    "r" : "01110010",
    "s" : "01110011",
    "t" : "01110100",
    "u" : "01110101",
    "v" : "01110110",
    "w" : "01110111",
    "x" : "01111000",
    "y" : "01111001",
    "z" : "01111010",
    "A" : "01000001",
    "B" : "01000010",
    "C" : "01000011",
    "D" : "01000100",
    "E" : "01000101",
    "F" : "01000110",
    "G" : "01000111",
    "H" : "01001000",
    "I" : "01001001",
    "J" : "01001010",
    "K" : "01001011",
    "L" : "01001100",
    "M" : "01001101",
    "N" : "01001110",
    "O" : "01001111",
    "P" : "01010000",
    "Q" : "01010001",
    "R" : "01010010",
    "S" : "01010011",
    "T" : "01010100",
    "U" : "01010101",
    "V" : "01010110",
    "W" : "01010111",
    "X" : "01011000",
    "Y" : "01011001",
    "Z" : "01011010",
}

def encrypt(text):
    crypted_text = ""
    for i in text:
        i = bin(ord(i))
        i = i.replace("b", "")
        crypted_text += i + " "
    return crypted_text

def decrypt(crypted_text):
    text = ""
    code = ""
    for i in crypted:
        code += i
        if len(code) == 8:
            get_key = [key for key, value in crypt.items() if value == code]
            text += get_key[0]
            code = ""
            get_key.clear()
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
