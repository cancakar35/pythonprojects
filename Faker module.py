from faker import Faker # modülleri dahil ediyoruz
from faker.providers import *

fake = Faker("tr_TR") # faker objesini çağırdık. İçine tr_TR yazarak dili belirtiyoruz.

print(fake.name()) # random sahte isim
print()

print(fake.address()) # random sahte adres
print()

print(fake.email()) # random sahte email
print()

print(fake.url()) # random sahte url
print()

print(fake.text()) # random sahte yazı
print()

# kendi kelime listemizi hazırlayıp random yazılar üretebiliriz.
my_word_list = [
    "kedi", "insan", "aşk", "okul", "iş", "arkadaş","uyumak", "gitmek", "sevmek", "python", "programlama", "gökyüzü", "hava",
]
print(fake.sentence(ext_word_list=my_word_list)) # kendi hazırladığımız kelime listesini giriyoruz
print()

print(fake.license_plate()) # araba plakası
print()

print(fake.iban()) # iban numarası
print()

print(fake.company()) # şirket
print()

# kredi kartı
print(fake.credit_card_full()) # kredi kartı bilgileri
print()
print(fake.credit_card_number()) # kart numarası
print()
print(fake.credit_card_provider) # kart sağlayıcısı (visa vb.)
print()

print(fake.job()) # random iş
print()

print(fake.password()) # şifre
print()

print(fake.phone_number()) # telefon numarası
print()

print(fake.profile()) # sahta insan (full bilgi)
print()


# Daha fazla özellik için -> https://faker.readthedocs.io/en/master/providers.html