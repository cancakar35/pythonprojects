# -*- coding: utf-8 -*-
# github.com/cancakar35

import sys
import os
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 215)
        MainWindow.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 441, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(153, 153, 156); background-color: rgb(32, 35, 42);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(21,101,192); border-radius: 25px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 140, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(121,134,203); border-radius: 25px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.closeEvent = self.closeEvent
        self.label_2.installEventFilter(self)
        self.label_3.installEventFilter(self)
        self.file = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Convert to webp"))
        self.label.setText(_translate("MainWindow", "Please choose a file!"))
        self.label_2.setText(_translate("MainWindow", "Choose File"))
        self.label_3.setText(_translate("MainWindow", "Convert"))

    def closeEvent(self, event):
        buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        res = QtWidgets.QMessageBox.warning(self, "Close", "Do you really want to close the application?", buttons)
        if res == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and event.button() == QtCore.Qt.LeftButton:
            if object == self.label_2:
                self.label_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(13,71,161); border-radius: 25px;")
            elif object == self.label_3:
                self.label_3.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(63,81,181); border-radius: 25px;")
            return True
        elif event.type() == QtCore.QEvent.MouseButtonRelease and event.button() == QtCore.Qt.LeftButton:
            if object == self.label_2:
                try:
                    self.label_2.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(21,101,192); border-radius: 25px;")
                    self.file = QtWidgets.QFileDialog.getOpenFileName(self, "Choose Image File","","Image Files (*.jpg *.jpeg *.png)")[0]
                    self.label.setText("File: "+str(self.file))
                except Exception as e:
                    self.label.setText(str(e))

            elif object == self.label_3:
                self.label_3.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(121,134,203); border-radius: 25px;")
                if self.file == "":
                    self.label.setText("Please choose a file!")
                else:
                    try:
                        im = Image.open(self.file)
                        name = QtCore.QFileInfo(self.file).fileName()
                        out = os.environ["HOMEPATH"] + os.path.sep + "Desktop" + os.path.sep
                        if not os.path.isfile(out+name):
                            if name.endswith("jpeg"):
                                out += name[:-4] + "webp"
                            else:
                                out += name[:-3] + "webp"
                        else:
                            if name.endswith("jpeg"):
                                out += name[:-5] + "x" + ".webp"
                            else:
                                out += name[:-4] + "x" + ".webp"
                        im.save(out, "webp",quality=90)
                        self.label.setText("Successfully Converted.\nFile:" + out)
                    except Exception as e:
                        self.label.setText(str(e))
            return True
        return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
