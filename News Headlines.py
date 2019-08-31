# -*- coding: utf-8 -*-

__author__ = "Can Çakar"

import locale
locale.setlocale(locale.LC_ALL, "")

import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 753)
        MainWindow.setMinimumSize(QtCore.QSize(465, 620))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(78, 78, 78);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255,213,79);")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_10.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
        self.label_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_12.setStyleSheet("background-color: rgb(255,213,79); color: rgb(0, 0, 0);")
        self.label_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_13.setStyleSheet("background-color: rgb(255,213,79); color: rgb(0, 0, 0);")
        self.label_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_14.setStyleSheet("background-color: rgb(255,213,79); color: rgb(0, 0, 0);")
        self.label_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_15.setStyleSheet("background-color: rgb(255,213,79); color: rgb(0, 0, 0);")
        self.label_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_16.setStyleSheet("background-color: rgb(255,213,79); color: rgb(0, 0, 0);")
        self.label_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_16.setScaledContents(False)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.retranslateUi(MainWindow)   
        self.horizontalLayout.addWidget(self.label_16)
        self.verticalLayout.addWidget(self.groupBox)
        self.now = datetime.now()
        self.label.setText(self.now.strftime("%d %B %A %X") + "  (Son güncelleme zamanı)")
        self.label_2.installEventFilter(self)
        self.label_3.installEventFilter(self)
        self.label_4.installEventFilter(self)
        self.label_5.installEventFilter(self)
        self.label_6.installEventFilter(self)
        self.label_7.installEventFilter(self)
        self.label_8.installEventFilter(self)
        self.label_9.installEventFilter(self)
        self.label_10.installEventFilter(self)
        self.label_11.installEventFilter(self)
        self.label_12.installEventFilter(self)
        self.label_13.installEventFilter(self)
        self.label_14.installEventFilter(self)
        self.label_15.installEventFilter(self)
        self.label_16.installEventFilter(self)

        self.url = "https://news.google.com/?hl=tr&gl=TR&ceid=TR:tr"
        self.res = requests.get(self.url)
        self.html = self.res.text
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.news = self.soup.find_all("h3",{"class", "ipQwMb ekueJc RD0gLb"})
        self.cnt = 0
        for i in self.news:
            if self.cnt < 10:
                if self.cnt == 0:
                    self.label_2.setText(i.text)
                elif self.cnt == 1:
                    self.label_3.setText(i.text)
                elif self.cnt == 2:
                    self.label_4.setText(i.text)
                elif self.cnt == 3:
                    self.label_5.setText(i.text)
                elif self.cnt == 4:
                    self.label_6.setText(i.text)
                elif self.cnt == 5:
                    self.label_7.setText(i.text)
                elif self.cnt == 6:
                    self.label_8.setText(i.text)
                elif self.cnt == 7:
                    self.label_9.setText(i.text)
                elif self.cnt == 8:
                    self.label_10.setText(i.text)
                elif self.cnt == 9:
                    self.label_11.setText(i.text)
                self.cnt += 1
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.Enter: # mouse üzerindeyken
            if object == self.label_12 or object == self.label_13 or object == self.label_14 or object == self.label_15 or object == self.label_16:
                object.setStyleSheet("background-color: rgb(255,179,0);")
            else:
                self.geo = QtCore.QRect.height(object.geometry())
                object.setFixedHeight(80)
                object.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255,245,157);")
            return True
        elif event.type() == QtCore.QEvent.Leave: # mouse üzerinden çekilince
            if object == self.label_12 or object == self.label_13 or object == self.label_14 or object == self.label_15 or object == self.label_16:
                object.setStyleSheet("background-color: rgb(255,213,79);")
            else:
                object.setFixedHeight(self.geo)
                object.setStyleSheet("background-color: rgb(120,144,156); color: rgb(255, 255, 255);")
            return False
        if event.type() == QtCore.QEvent.MouseButtonPress: # mouse butonu ile tıklanınca
            if event.button() == QtCore.Qt.LeftButton: # bu şekilde yazarsak sadece sol click ile event aktif olacaktır diğer mouse butonları ile çalışmayacaktır.
                if object == self.label_12 or object == self.label_13 or object == self.label_14 or object == self.label_15 or object == self.label_16:
                    object.setStyleSheet("background-color: rgb(255,87,34); color: rgb(255, 255, 255);")
                    self.now = datetime.now()
                    self.label.setText(self.now.strftime("%d %B %A %X") + "  (Son güncelleme zamanı)")
                return True
        elif event.type() == QtCore.QEvent.MouseButtonRelease: # mouse butonu bırakılınca
            if object == self.label_12 or object == self.label_13 or object == self.label_14 or object == self.label_15 or object == self.label_16:
                object.setStyleSheet("background-color: rgb(255,179,0);")
                if object == self.label_12:
                    self.url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FuUnlHZ0pVVWlnQVAB?hl=tr&gl=TR&ceid=TR%3Atr"
                    self.res = requests.get(self.url)
                    self.soup = BeautifulSoup(self.res.text, "html.parser")
                    self.news = self.soup.find_all("h3",{"class", "ipQwMb ekueJc RD0gLb"})
                    self.cnt = 0
                    for i in self.news:
                        if self.cnt < 10:
                            if self.cnt == 0:
                                self.label_2.setText(i.text)
                            elif self.cnt == 1:
                                self.label_3.setText(i.text)
                            elif self.cnt == 2:
                                self.label_4.setText(i.text)
                            elif self.cnt == 3:
                                self.label_5.setText(i.text)
                            elif self.cnt == 4:
                                self.label_6.setText(i.text)
                            elif self.cnt == 5:
                                self.label_7.setText(i.text)
                            elif self.cnt == 6:
                                self.label_8.setText(i.text)
                            elif self.cnt == 7:
                                self.label_9.setText(i.text)
                            elif self.cnt == 8:
                                self.label_10.setText(i.text)
                            elif self.cnt == 9:
                                self.label_11.setText(i.text)
                            self.cnt += 1
                elif object == self.label_13:
                    self.url = "https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREY2Ym1OZkVnSjBjaWdBUAE?hl=tr&gl=TR&ceid=TR%3Atr"
                    self.res = requests.get(self.url)
                    self.soup = BeautifulSoup(self.res.text, "html.parser")
                    self.news = self.soup.find_all("h3",{"class", "ipQwMb ekueJc RD0gLb"})
                    self.cnt = 0
                    for i in self.news:
                        if self.cnt < 10:
                            if self.cnt == 0:
                                self.label_2.setText(i.text)
                            elif self.cnt == 1:
                                self.label_3.setText(i.text)
                            elif self.cnt == 2:
                                self.label_4.setText(i.text)
                            elif self.cnt == 3:
                                self.label_5.setText(i.text)
                            elif self.cnt == 4:
                                self.label_6.setText(i.text)
                            elif self.cnt == 5:
                                self.label_7.setText(i.text)
                            elif self.cnt == 6:
                                self.label_8.setText(i.text)
                            elif self.cnt == 7:
                                self.label_9.setText(i.text)
                            elif self.cnt == 8:
                                self.label_10.setText(i.text)
                            elif self.cnt == 9:
                                self.label_11.setText(i.text)
                            self.cnt += 1
                elif object == self.label_14:
                    self.url = "https://news.google.com/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSjBjaG9DVkZJb0FBUAE?hl=tr&gl=TR&ceid=TR%3Atr"
                    self.res = requests.get(self.url)
                    self.soup = BeautifulSoup(self.res.text, "html.parser")
                    self.news = self.soup.find_all("h3",{"class", "ipQwMb ekueJc RD0gLb"})
                    self.cnt = 0
                    for i in self.news:
                        if self.cnt < 10:
                            if self.cnt == 0:
                                self.label_2.setText(i.text)
                            elif self.cnt == 1:
                                self.label_3.setText(i.text)
                            elif self.cnt == 2:
                                self.label_4.setText(i.text)
                            elif self.cnt == 3:
                                self.label_5.setText(i.text)
                            elif self.cnt == 4:
                                self.label_6.setText(i.text)
                            elif self.cnt == 5:
                                self.label_7.setText(i.text)
                            elif self.cnt == 6:
                                self.label_8.setText(i.text)
                            elif self.cnt == 7:
                                self.label_9.setText(i.text)
                            elif self.cnt == 8:
                                self.label_10.setText(i.text)
                            elif self.cnt == 9:
                                self.label_11.setText(i.text)
                            self.cnt += 1
                elif object == self.label_15:
                    self.url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FuUnlHZ0pVVWlnQVAB?hl=tr&gl=TR&ceid=TR%3Atr"
                    self.res = requests.get(self.url)
                    self.soup = BeautifulSoup(self.res.text, "html.parser")
                    self.news = self.soup.find_all("h3",{"class", "ipQwMb ekueJc RD0gLb"})
                    self.cnt = 0
                    for i in self.news:
                        if self.cnt < 10:
                            if self.cnt == 0:
                                self.label_2.setText(i.text)
                            elif self.cnt == 1:
                                self.label_3.setText(i.text)
                            elif self.cnt == 2:
                                self.label_4.setText(i.text)
                            elif self.cnt == 3:
                                self.label_5.setText(i.text)
                            elif self.cnt == 4:
                                self.label_6.setText(i.text)
                            elif self.cnt == 5:
                                self.label_7.setText(i.text)
                            elif self.cnt == 6:
                                self.label_8.setText(i.text)
                            elif self.cnt == 7:
                                self.label_9.setText(i.text)
                            elif self.cnt == 8:
                                self.label_10.setText(i.text)
                            elif self.cnt == 9:
                                self.label_11.setText(i.text)
                            self.cnt += 1
                elif object == self.label_16:
                    self.url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuUnlHZ0pVVWlnQVAB?hl=tr&gl=TR&ceid=TR%3Atr"
                    self.res = requests.get(self.url)
                    self.soup = BeautifulSoup(self.res.text, "html.parser")
                    self.news = self.soup.find_all("h3",{"class", "ipQwMb ekueJc RD0gLb"})
                    self.cnt = 0
                    for i in self.news:
                        if self.cnt < 10:
                            if self.cnt == 0:
                                self.label_2.setText(i.text)
                            elif self.cnt == 1:
                                self.label_3.setText(i.text)
                            elif self.cnt == 2:
                                self.label_4.setText(i.text)
                            elif self.cnt == 3:
                                self.label_5.setText(i.text)
                            elif self.cnt == 4:
                                self.label_6.setText(i.text)
                            elif self.cnt == 5:
                                self.label_7.setText(i.text)
                            elif self.cnt == 6:
                                self.label_8.setText(i.text)
                            elif self.cnt == 7:
                                self.label_9.setText(i.text)
                            elif self.cnt == 8:
                                self.label_10.setText(i.text)
                            elif self.cnt == 9:
                                self.label_11.setText(i.text)
                            self.cnt += 1
            else:
                pass
            return False
        return False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Haberler"))
        self.label.setText(_translate("MainWindow", "Sistem"))
        self.label_2.setText(_translate("MainWindow", "Haber"))
        self.label_3.setText(_translate("MainWindow", "Haber"))
        self.label_4.setText(_translate("MainWindow", "Haber"))
        self.label_5.setText(_translate("MainWindow", "Haber"))
        self.label_6.setText(_translate("MainWindow", "Haber"))
        self.label_7.setText(_translate("MainWindow", "Haber"))
        self.label_8.setText(_translate("MainWindow", "Haber"))
        self.label_9.setText(_translate("MainWindow", "Haber"))
        self.label_10.setText(_translate("MainWindow", "Haber"))
        self.label_11.setText(_translate("MainWindow", "Haber"))
        self.label_12.setText(_translate("MainWindow", "Dünya"))
        self.label_13.setText(_translate("MainWindow", "Türkiye"))
        self.label_14.setText(_translate("MainWindow", "Bilim ve Teknoloji"))
        self.label_15.setText(_translate("MainWindow", "Spor"))
        self.label_16.setText(_translate("MainWindow", "Ekonomi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
