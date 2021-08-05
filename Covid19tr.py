from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import re

def print_result(gnldurum):
    print("Tarih: {}  Test Sayısı: {} Günlük Vaka Sayısı: {} Günlük Vefat Sayısı: {} Bugünkü İyileşen Sayısı: {}".format(
    gnldurum["tarih"], gnldurum["gunluk_test"], gnldurum["gunluk_vaka"],gnldurum["gunluk_vefat"],gnldurum["gunluk_iyilesen"]
    ))
    input()


def geneldurum():
    res = requests.get("https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html")
    soup = BeautifulSoup(res.content, "lxml")
    data = soup.find("form", {"id":"form2"}).find_all("script")[-1]
    json_data = re.search(r'geneldurumjson\s*=\s*(.*?}])', str(data))[1]
    gnldurumjson = json.loads(json_data)

    print("Bugünün tarihi: ",datetime.now())
    tarih = input("Covid-19 bilgileri için tarih giriniz. Bugün için bugün yazabilirsiniz. Geçerli biçim: 01.01.2021:  ")
    if tarih=="bugün":
        print_result(gnldurumjson[0])
    else:
        for j in gnldurumjson:
            if j["tarih"] == tarih:
                print_result(j)

def asilar():
    res = requests.get("https://covid19.saglik.gov.tr")
    soup = BeautifulSoup(res.content, "lxml")
    data = soup.find("g", {'id':'turkiye-tamamlanan'}).find_all('g')
    il = input("Sehir adi giriniz, tüm sehirler icin Türkiye yazabilirsiniz:  ").title()
    if il == "Türkiye":
        for i in range(len(data)):
            print("Sehir: {:15}  Aşılanma Yüzdesi: {}".format(data[i]["data-adi"], data[i]["data-yuzde"]))
        input()
    else:
        for i in range(len(data)):
            if data[i]["data-adi"] == il:
                print("Sehir: {:15}  Aşılanma Yüzdesi: {}".format(data[i]["data-adi"], data[i]["data-yuzde"]))
                input()
                break

def haftalikvaka():
    res = requests.get("https://covid19.saglik.gov.tr")
    soup = BeautifulSoup(res.content, "lxml")
    data = soup.find("g", {'id':'turkiye'}).find_all('g')
    tarih = soup.find("div", {'class':'info_box info_box_left shadow'}).find("p").text
    il = input("Sehir adi giriniz, tüm sehirler icin Türkiye yazabilirsiniz:  ").title()
    if il == "Türkiye":
        print("Veri tarihi: {}\n".format(tarih))
        for i in range(len(data)):
            print("Sehir: {:15}  Vaka Sayısı(100 binde): {}".format(data[i]["data-iladi"], data[i]["data-detay"]))
        input()
    else:
        print("Veri tarihi: {}\n".format(tarih))
        for i in range(len(data)):
            if data[i]["data-adi"] == il:
                print("Sehir: {:15}  Aşılanma Yüzdesi: {}".format(data[i]["data-iladi"], data[i]["data-detay"]))
                input()
                break

while True:
    print("\n1:Genel Tablo\n2:Haftalik 100 binde vaka sayisi\n3:Aşılanma Oranı\n4:Programı Kapat\n")
    inp = input("Seçim Yap: ")
    if inp == "4":
        break
    elif inp == "1":
        geneldurum()
    elif inp == "2":
        haftalikvaka()
    elif inp == "3":
        asilar()
    else:
        print("Hatalı seçim!\n")