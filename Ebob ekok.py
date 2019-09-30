__author__ = "CAN CAKAR"
# EBOB
def ebob(num1, num2):
    ebob = 1
    x = 1
    while x <= num1 and x <= num2:
        if not(num1 % x) and not(num2 % x):
            ebob = x
        x += 1
    return ebob

num1 = int(input("İlk sayıyı girin: "))
num2 = int(input("İkinci sayıyı girin: "))
print("{} ve {} sayılarının ebob'u".format(num1, num2), ebob(num1,num2))
print()
# EKOK
def ekok(num1, num2):
    ekok = 1
    x = 2
    while True:
        if num1 == 1 and num2 == 1:
            break
        else:
            if (num1 % x == 0 and num2 % x == 0):
                ekok *= x
                num1 //= x
                num2 //= x
            elif (num1 % x == 0 and num2 % x != 0):
                ekok *= x
                num1 //= x
            elif (num1 % x != 0 and num2 % x == 0):
                ekok *= x
                num2 //= x
            else:
                x += 1
    return ekok

num1 = int(input("İlk sayıyı girin: "))
num2 = int(input("İkinci sayıyı girin: "))
print("{} ve {} sayılarının ekok'u".format(num1, num2), ekok(num1, num2))
