import os
import time


uipath = input("ui dosya yolunu girin: ")
name = input("Dosya ismini girin(örneğin file.ui için file): ")

convert = "python -m PyQt5.uic.pyuic -x {} -o {}".format(name + ".ui",name + ".py")

os.chdir(uipath)
os.system(convert)
print("Çevirme işlemi başarıyla tamamlandı\nDosya yolu: {}\nDosya İsmi: {}".format(uipath,name + ".py"))
time.sleep(2)
