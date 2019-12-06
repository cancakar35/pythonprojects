#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# github.com/cancakar35
# instagram.com/cancakar35

"""
Deprem verilerini almak için sc3.koeri.boun.edu.tr/eqevents/events.html adresi kullanılmıştır.
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import requests

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(697, 749)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(78, 78, 78);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_12.setStyleSheet("background-color: rgb(100,181,246);\n"
"color: rgb(230,230,230);\n"
"border-radius: 10px;")
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("border-top-color: rgb(78, 78, 78);")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setStyleSheet("background-color: rgb(187,222,251);\n"
"border-radius: 20px;\n"
"color: rgb(39, 39, 39);")
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_10.setStyleSheet("background-color: rgb(187,222,251);\n"
"border-radius: 20px;\n"
"color: rgb(39,39,39);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        MainWindow.closeEvent = self.closeEvent
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.list1 = MainWindow.findChildren(QtWidgets.QLabel)
        for i in self.list1:
            i.installEventFilter(self)
        self.get_ertq()
    
    def closeEvent(self, event):
        buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        res = QtWidgets.QMessageBox.warning(self,"Kapat", "Uygulamayı kapatmak istiyormusunuz?", buttons)
        if res == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def get_ertq(self):
        try:
            self.res = requests.get("http://sc3.koeri.boun.edu.tr/eqevents/events.html")
            self.soup = BeautifulSoup(self.res.text, "html.parser")
            self.eq_soup = self.soup.findAll("tr")
            self.cnt = 0
            self.eq_list = []
            for i in self.eq_soup[1:]:
                if self.cnt < 10:
                    self.eq_list.append([i.findAll("td")[0].text, i.findAll("td")[6].text,i.findAll("td")[1].text])
                self.cnt += 1
            self.cnt = 0
            for j in self.eq_list:
                if self.cnt == 0:
                    self.label.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                elif self.cnt == 1:
                    self.label_2.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                elif self.cnt == 2:
                    self.label_4.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                elif self.cnt == 3:
                    self.label_3.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                elif self.cnt == 4:
                    self.label_8.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                elif self.cnt == 5:
                    self.label_5.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                elif self.cnt == 6:
                    self.label_7.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                elif self.cnt == 7:
                    self.label_6.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                elif self.cnt == 8:
                    self.label_11.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                elif self.cnt == 9:
                    self.label_12.setText("{}\t{}\t{}".format(j[0],j[2],j[1]))
                self.cnt += 1
        except requests.ConnectionError:
            QtWidgets.QMessageBox.warning(self, "ConnectionError", "Internet bağlantınızı kontrol edin!")
        
    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and event.button() == QtCore.Qt.LeftButton:
            if object in [self.label_9, self.label_10]:
                object.setStyleSheet("background-color: rgb(159,168,218); border-radius: 20px;color: rgb(39,39,39);")

            return True
        elif event.type() == QtCore.QEvent.MouseButtonRelease and event.button() == QtCore.Qt.LeftButton:
            if object in [self.label_9, self.label_10]:
                object.setStyleSheet("background-color: rgb(187,222,251);border-radius: 20px;color: rgb(39,39,39);")
                if object == self.label_9:
                    self.get_ertq()
                else:
                    MainWindow.close()
        
        return False
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anlık Deprem Bilgisi"))
        self.label.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_2.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_4.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_3.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_8.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_5.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_7.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_6.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_11.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_12.setText(_translate("MainWindow", "Lorem ipsum"))
        self.label_9.setText(_translate("MainWindow", "Yenile"))
        self.label_10.setText(_translate("MainWindow", "Kapat"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
