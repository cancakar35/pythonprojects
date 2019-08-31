__author__ = "Can CAKAR"

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import sys
import os

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 678)
        MainWindow.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(78, 78, 78);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(158,158,158);")
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(158,158,158);")
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(158,158,158);")
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(158,158,158);")
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.fontComboBox = QtWidgets.QFontComboBox(self.groupBox)
        self.fontComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.fontComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.fontComboBox.setFont(font)
        self.fontComboBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fontComboBox.setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(158,158,158);")
        self.fontComboBox.setEditable(False)
        self.fontComboBox.setFrame(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout.addWidget(self.fontComboBox)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255); background-color:rgb(158,158,158);")
        self.comboBox.setEditable(False)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(245,245,245);")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(33,33,33); color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(33,33,33); color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 21))
        self.menubar.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(85, 170, 255);")
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuDuzen = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDuzen")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.actionKaydet = QtWidgets.QAction(MainWindow)
        self.actionKaydet.setObjectName("actionKaydet")
        self.actionYazd_r = QtWidgets.QAction(MainWindow)
        self.actionYazd_r.setObjectName("actionYazd_r")
        self.actionOrtala = QtWidgets.QAction(MainWindow)
        self.actionOrtala.setObjectName("actionOrtala")
        self.actionSola = QtWidgets.QAction(MainWindow)
        self.actionSola.setObjectName("actionSola")
        self.actionSaga = QtWidgets.QAction(MainWindow)
        self.actionSaga.setObjectName("actionSaga")
        self.actionJournal_Hakk_nda = QtWidgets.QAction(MainWindow)
        self.actionJournal_Hakk_nda.setObjectName("actionJournal_Hakk_nda")
        self.menuDosya.addAction(self.actionA)
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionKaydet)
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionYazd_r)
        self.menuDuzen.addAction(self.actionOrtala)
        self.menuDuzen.addSeparator()
        self.menuDuzen.addAction(self.actionSola)
        self.menuDuzen.addSeparator()
        self.menuDuzen.addAction(self.actionSaga)
        self.menuYard_m.addAction(self.actionJournal_Hakk_nda)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuDuzen.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())
        self.actionA.triggered.connect(self.openfl)
        self.actionKaydet.triggered.connect(self.savefl)
        self.actionYazd_r.triggered.connect(self.printfl)
        self.actionOrtala.triggered.connect(self.ortala)
        self.pushButton.clicked.connect(self.clall)
        self.pushButton_2.clicked.connect(self.savefl)
        self.fontComboBox.currentFontChanged.connect(self.chfont)
        self.comboBox.currentTextChanged.connect(self.chsize)
        self.actionJournal_Hakk_nda.triggered.connect(self.aboutrichtxt)
        self.actionOrtala.triggered.connect(self.ortala)
        self.actionSaga.triggered.connect(self.alignright)
        self.actionSola.triggered.connect(self.alignleft)
        self.label.installEventFilter(self)
        self.label_2.installEventFilter(self)
        self.label_3.installEventFilter(self)
        self.label_4.installEventFilter(self)
        self.isbold = False
        self.isitalic = False
        self.isunder = False
        self.retranslateUi(MainWindow)
        MainWindow.closeEvent = self.closeEvent
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def closeEvent(self, event):
        if not(self.textEdit.document().isModified()):
            event.accept()
        else:
            buttons = QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel
            res = QtWidgets.QMessageBox.warning(self,"Dosya Uyarısı", "Kaydetmeden Çıkmak İstiyor musunuz?\nYaptığınız değişiklikler silinecektir!", buttons)
            if res == QtWidgets.QMessageBox.Ok:
                event.accept()
            else:
                event.ignore()

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.Enter:
            if object == self.label:
                if self.isbold:
                    self.label.setStyleSheet("background-color: rgb(84,110,122); color: rgb(255,255,255);")
                else:
                    self.label.setStyleSheet("background-color: rgb(144,164,174); color: rgb(255,255,255);")
            elif object == self.label_2:
                if self.isitalic:
                    self.label_2.setStyleSheet("background-color: rgb(84,110,122); color: rgb(255,255,255);")
                else:
                    self.label_2.setStyleSheet("background-color: rgb(144,164,174); color: rgb(255,255,255);")
            elif object == self.label_3:
                if self.isunder:
                    self.label_3.setStyleSheet("background-color: rgb(84,110,122); color: rgb(255,255,255);")
                else:
                    self.label_3.setStyleSheet("background-color: rgb(144,164,174); color: rgb(255,255,255);")
            elif object == self.label_4:
                self.label_4.setStyleSheet("background-color: rgb(144,164,174); color: rgb(255,255,255);")
            return True
        elif event.type() == QtCore.QEvent.Leave:
            if object == self.label:
                if not(self.isbold):
                    self.label.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(158,158,158);")
                else:
                    self.label.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(96,125,139);")
            elif object == self.label_2:
                if not(self.isitalic):
                    self.label_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(158,158,158);")
                else:
                    self.label_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(96,125,139);")
            elif object == self.label_3:
                if not(self.isunder):
                    self.label_3.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(158,158,158);")
                else:
                    self.label_3.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(96,125,139);")
            elif object == self.label_4:
                self.label_4.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(158,158,158);")

            return False
        if event.type() == QtCore.QEvent.MouseButtonPress and event.button() == QtCore.Qt.LeftButton:
            object.setStyleSheet("background-color: rgb(38,50,56); color: rgb(255,255,255);")
            return True

        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            if object == self.label:
                if not(self.isbold):
                    self.textEdit.setFontWeight(QtGui.QFont.Bold)
                    object.setStyleSheet("background-color: rgb(84,110,122); color: rgb(255,255,255);")
                    self.isbold = True
                    return True
                elif self.isbold:
                    self.textEdit.setFontWeight(QtGui.QFont.Normal)
                    object.setStyleSheet("background-color: rgb(144,164,174); color: rgb(255,255,255);")
                    self.isbold = False
                    return False
            elif object == self.label_2:
                if not(self.isitalic):
                    self.textEdit.setFontItalic(True)
                    object.setStyleSheet("background-color: rgb(84,110,122); color: rgb(255,255,255);")
                    self.isitalic = True
                    return True
                elif self.isitalic:
                    self.textEdit.setFontItalic(False)
                    object.setStyleSheet("background-color: rgb(144,164,174); color: rgb(255,255,255);")
                    self.isitalic = False
                    return False
            elif object == self.label_3:
                if not(self.isunder):
                    self.textEdit.setFontUnderline(True)
                    object.setStyleSheet("background-color: rgb(84,110,122); color: rgb(255,255,255);")
                    self.isunder = True
                    return True
                elif self.isunder:
                    self.textEdit.setFontUnderline(False)
                    object.setStyleSheet("background-color: rgb(144,164,174); color: rgb(255,255,255);")
                    self.isunder = False
                    return False
            elif object == self.label_4:
                object.setStyleSheet("background-color: rgb(158,158,158); color: rgb(255,255,255);")
                color = QtWidgets.QColorDialog.getColor()
                self.textEdit.setTextColor(color)
            return True
        return False

    def clall(self):
        self.textEdit.clear()
    
    def openfl(self):
        try:
            filex = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Aç", os.getenv("HOME"),"Myrichtext File(*.myrichtext);;All Files(*.*)")
            with open(filex[0], "r", encoding="utf-8") as file1:
                text = file1.read()
                if text.startswith("<!DOCTYPE HTML"):
                    self.textEdit.setHtml(text)
                else:
                    self.textEdit.setText(text)
        except FileNotFoundError:
            msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning ,"Dosya Aç", "Dosya açma başarısız!")
            msgbox.exec_()

    def savefl(self):
        try:
            filey = QtWidgets.QFileDialog.getSaveFileName(self,"Kaydet",os.getenv("HOME"),"Myrichtext File(*.myrichtext);;All Files (*.*)")
            with open(filey[0], "w", encoding="utf-8") as file2:
                file2.write(self.textEdit.toHtml())
            msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Dosya Kaydet", "Dosya başarıyla kaydedildi!")
            msgbox.exec_()
        except (FileNotFoundError,FileExistsError):
            msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning ,"Dosya Kaydet", "Dosya kaydetme başarısız!")
            msgbox.exec_()
    
    def printfl(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self)
        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def chfont(self, font):
        self.textEdit.setFontFamily(font.family())
    
    def chsize(self, size):
        self.textEdit.setFontPointSize(float(size))
    
    def aboutrichtxt(self):
        a = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,"Rich Text Editor","Rich Text Editor v.1.0\nCan Çakar tarafından yazılmıştır."
            "\n© 2019 CAN CAKAR\nOpen Source projedir.")
        a.exec_()
    
    def ortala(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignHCenter)

    def alignleft(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignAbsolute)

    def alignright(self):
        self.textEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignAbsolute)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rich Text Editor"))
        self.label.setText(_translate("MainWindow", "Kalın"))
        self.label_2.setText(_translate("MainWindow", "İtalik"))
        self.label_3.setText(_translate("MainWindow", "Altı çizili"))
        self.label_4.setText(_translate("MainWindow", "Renk"))
        self.comboBox.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox.setItemText(1, _translate("MainWindow", "9"))
        self.comboBox.setItemText(2, _translate("MainWindow", "10"))
        self.comboBox.setItemText(3, _translate("MainWindow", "11"))
        self.comboBox.setItemText(4, _translate("MainWindow", "12"))
        self.comboBox.setItemText(5, _translate("MainWindow", "14"))
        self.comboBox.setItemText(6, _translate("MainWindow", "16"))
        self.comboBox.setItemText(7, _translate("MainWindow", "18"))
        self.comboBox.setItemText(8, _translate("MainWindow", "20"))
        self.comboBox.setItemText(9, _translate("MainWindow", "22"))
        self.comboBox.setItemText(10, _translate("MainWindow", "24"))
        self.comboBox.setItemText(11, _translate("MainWindow", "26"))
        self.comboBox.setItemText(12, _translate("MainWindow", "28"))
        self.comboBox.setItemText(13, _translate("MainWindow", "36"))
        self.comboBox.setItemText(14, _translate("MainWindow", "48"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Yazdıktan sonra kaydetmeyi unutmayın!"))
        self.pushButton_2.setText(_translate("MainWindow", "Kaydet"))
        self.pushButton.setText(_translate("MainWindow", "Temizle"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuDuzen.setTitle(_translate("MainWindow", "Düzen"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.actionA.setText(_translate("MainWindow", "Aç"))
        self.actionA.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionKaydet.setText(_translate("MainWindow", "Kaydet"))
        self.actionKaydet.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionYazd_r.setText(_translate("MainWindow", "Yazdır"))
        self.actionOrtala.setText(_translate("MainWindow", "Yazıyı Ortala"))
        self.actionSola.setText(_translate("MainWindow", "Yazıyı Sola Hizala"))
        self.actionSaga.setText(_translate("MainWindow", "Yazıyı Sağa Hizala"))
        self.actionJournal_Hakk_nda.setText(_translate("MainWindow", "Rich Text Editor Hakkında"))
        self.actionJournal_Hakk_nda.setShortcut(_translate("MainWindow", "F1"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
