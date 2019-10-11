# -*- coding: utf-8 -*-
__author__ = "Can Çakar" # instagram.com/cancakar35

from PyQt5 import QtCore, QtGui, QtWidgets
import math
import sys

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 760)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(90, 90, 90);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(16777215, 110))
        self.label.setMargin(5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 10px;")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(2000, 2000))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_35.setFont(font)
        self.label_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_35.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 0, 4, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox)
        self.label_36.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_36.setFont(font)
        self.label_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_36.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 0, 5, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(20)
        self.label_27.setFont(font)
        self.label_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_27.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 1, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox)
        self.label_32.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_32.setFont(font)
        self.label_32.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_32.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox)
        self.label_33.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_33.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 0, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_34.setFont(font)
        self.label_34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_34.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 0, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_28.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 1, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_29.setFont(font)
        self.label_29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_29.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 1, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_31.setFont(font)
        self.label_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_31.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 1, 5, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox)
        self.label_30.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_30.setFont(font)
        self.label_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_30.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 1, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.label_13.setFont(font)
        self.label_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_13.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.label_21.setFont(font)
        self.label_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_21.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 6, 5, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_23.setFont(font)
        self.label_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_23.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 6, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_12.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.label_20.setFont(font)
        self.label_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_20.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 5, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 4, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_22.setFont(font)
        self.label_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_22.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_10.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.label_19.setFont(font)
        self.label_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_19.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.label_18.setFont(font)
        self.label_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_18.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_24.setFont(font)
        self.label_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_24.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_14.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setStyleSheet("background-color: rgb(238,238,238);\n"
"border-radius: 20px;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        self.label_17.setFont(font)
        self.label_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_17.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 5, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_26.setFont(font)
        self.label_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_26.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 2, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(20)
        self.label_25.setFont(font)
        self.label_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_25.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_15.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_16.setStyleSheet("background-color: rgb(189,189,189);\n"
"border-radius: 20px;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        list1 = MainWindow.findChildren(QtWidgets.QLabel)
        self.expression = self.label.text()
        self.phrase = 0
        self.curopr = ""
        self.labels = [i.objectName() for i in list1]
        for i in list1:
            if i.objectName() != "label":
                i.installEventFilter(self)
        self.retranslateUi(MainWindow)
        MainWindow.closeEvent = self.closeEvent
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def closeEvent(self, event):
        res = QtWidgets.QMessageBox.warning(self, "Programı Kapat", "Programı kapatmak istiyor musunuz?\n\n", QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.MouseButtonPress and event.button() == QtCore.Qt.LeftButton and object.isEnabled():
            listx = ["1","2","3","4","5","6","7","8","9","0"]
            if listx.count(object.text()) != 0:
                object.setStyleSheet("background-color: rgb(187,222,251); border-radius: 20px;")
            else:
                object.setStyleSheet("background-color: rgb(144,202,249); border-radius: 20px;")
            return True
        elif event.type() == QtCore.QEvent.MouseButtonRelease and event.button() == QtCore.Qt.LeftButton and object.isEnabled():
            listx = ["1","2","3","4","5","6","7","8","9","0"]
            a = "as"
            a.startswith
            if listx.count(object.text()) != 0:
                object.setStyleSheet("background-color: rgb(238,238,238); border-radius: 20px;")
                if self.label.text().startswith("0."):
                    self.label.setText(self.label.text() + object.text())
                elif self.label.text().endswith("-") or self.label.text().endswith("×") or self.label.text().endswith("÷") or self.label.text().endswith("+"):
                    self.label.setText(self.label.text() + object.text())
                elif self.label.text().startswith("0"):
                    self.label.setText(object.text())
                elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                    self.label.setText(object.text())
                else:
                    self.label.setText(self.label.text() + object.text())
            else:
                object.setStyleSheet("background-color: rgb(189,189,189); border-radius: 20px;")
                if object.text() == ".":
                    if self.label.text().endswith("-") or self.label.text().endswith("×") or self.label.text().endswith("÷") or self.label.text().endswith("+"):
                        pass
                    elif self.label.text().endswith("(") or self.label.text().endswith(")"):
                        pass
                    elif self.label.text().find(".") == -1:
                        self.label.setText(self.label.text() + ".")
                if object.text() == "C":
                    self.label.clear()
                    self.label.setText("0")
                    self.label_17.setEnabled(True)
                    self.label_18.setEnabled(True)
                    self.label_19.setEnabled(True)
                    self.label_20.setEnabled(True)
                    self.label_29.setEnabled(True)
                    self.label_33.setEnabled(True)
                    self.label_31.setEnabled(True)
                    self.label_34.setEnabled(True)
                    self.label_35.setEnabled(True)
                    self.label_36.setEnabled(True)
                    self.label_30.setEnabled(True)
                    self.curopr = ""
                if object.text() == "CE":
                    self.label.setText("0")
                if object == self.label_15:
                    if len(self.label.text()) == 1:
                        self.label.setText("0")
                    elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                        self.label.setText("0")
                    else:
                        self.label.setText(self.label.text()[:-1])
                if object.text() == "(":
                    if self.label.text().startswith("0."):
                        pass
                    elif self.label.text().endswith("-") or self.label.text().endswith("×") or self.label.text().endswith("÷") or self.label.text().endswith("+"):
                        self.label.setText(self.label.text() + object.text())
                        self.phrase += 1
                    elif self.label.text() == "Geçersiz İşlem":
                        self.label.setText(object.text())
                        self.phrase += 1
                    elif self.label.text().endswith("0"):
                        self.label.setText(self.label.text()[:-1] + object.text())
                        self.phrase += 1
                    else:
                        self.label.setText(self.label.text() + object.text())
                        self.phrase += 1
                if object.text() == ")":
                    if self.phrase == 0:
                        pass
                    elif self.phrase > 0:
                        if self.label.text().startswith("0."):
                            pass
                        elif self.label.text() == "Geçersiz İşlem":
                            self.label.setText(object.text())
                            self.phrase -= 1
                        else:
                            self.label.setText(self.label.text() + object.text())
                            self.phrase -= 1
                        
                if object.text() == "+":
                    if self.label.text().endswith(".") or self.label.text().endswith("(") or self.label.text().endswith(")"):
                        pass
                    elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                        pass
                    elif self.label.text().endswith("+") or self.label.text().endswith("-") or self.label.text().endswith("*") or self.label.text().endswith("/"):
                        pass
                    else:
                        self.curopr = "add"
                        self.label.setText(self.label.text() + "+")

                if object.text() == "-":
                    if self.label.text().endswith(".") or self.label.text().endswith("(") or self.label.text().endswith(")"):
                        pass
                    elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                        pass
                    elif self.label.text().endswith("+") or self.label.text().endswith("-") or self.label.text().endswith("*") or self.label.text().endswith("/"):
                        pass
                    else:
                        self.curopr = "subt"
                        self.label.setText(self.label.text() + "-")
                if object.text() == "×":
                    if self.label.text().endswith(".") or self.label.text().endswith("(") or self.label.text().endswith(")"):
                        pass
                    elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                        pass
                    elif self.label.text().endswith("+") or self.label.text().endswith("-") or self.label.text().endswith("*") or self.label.text().endswith("/"):
                        pass
                    else:
                        self.curopr = "multi"
                        self.label.setText(self.label.text() + "*")
                if object.text() == "÷":
                    if self.label.text().endswith(".") or self.label.text().endswith("(") or self.label.text().endswith(")"):
                        pass
                    elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                        pass
                    elif self.label.text().endswith("+") or self.label.text().endswith("-") or self.label.text().endswith("*") or self.label.text().endswith("/"):
                        pass
                    else:
                        self.curopr = "div"
                        self.label.setText(self.label.text() + "/")
                if object.text() == "=":
                    try:
                        if self.curopr == "":
                            self.label.clear()
                            self.label.setText("0")
                            self.label_17.setEnabled(True)
                            self.label_18.setEnabled(True)
                            self.label_19.setEnabled(True)
                            self.label_20.setEnabled(True)
                            self.label_29.setEnabled(True)
                            self.label_33.setEnabled(True)
                            self.label_31.setEnabled(True)
                            self.label_34.setEnabled(True)
                            self.label_35.setEnabled(True)
                            self.label_36.setEnabled(True)
                            self.label_30.setEnabled(True)
                        elif self.curopr == "log":
                            for i in self.label.text():
                                if i in ["+","*","/","-"]:
                                    self.label.setText("Geçersiz İşlem")
                            end = math.log(self.num1, float(self.label.text()))
                            end2 = str(end)
                            if end2.endswith(".0"):
                                self.label.setText(end2[:-2])
                            else:
                                self.label.setText(str(end))
                            self.label_17.setEnabled(True)
                            self.label_18.setEnabled(True)
                            self.label_19.setEnabled(True)
                            self.label_20.setEnabled(True)
                            self.label_31.setEnabled(True)
                            self.label_29.setEnabled(True)
                            self.label_33.setEnabled(True)
                            self.label_34.setEnabled(True)
                            self.label_35.setEnabled(True)
                            self.label_36.setEnabled(True)
                            self.label_30.setEnabled(True)
                        else:
                            self.expression = self.label.text()
                            self.label.setText(str(eval(self.expression)))
                    except (ValueError, OverflowError):
                        self.label.setText("Geçersiz İşlem")
                if object == self.label_25:
                    self.label.setText(str(math.pi))
                if object == self.label_24:
                    try:
                        end = math.factorial(float(self.label.text()))
                        if str(end).endswith(".0"):
                            self.label.setText(str(end)[:-2])
                        else:
                            self.label.setText(str(end))
                    except (ValueError, OverflowError):
                        self.label.setText("Geçersiz İşlem")
                if object == self.label_32:
                    if self.label.text().endswith(".") or self.label.text().endswith("(") or self.label.text().endswith(")"):
                        pass
                    elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                        pass
                    elif self.label.text().endswith("+") or self.label.text().endswith("-") or self.label.text().endswith("*") or self.label.text().endswith("/"):
                        pass
                    else:
                        self.curopr = "square"
                        self.label.setText(self.label.text() + "**2")
                if object == self.label_28:
                    try:
                        end = 10 ** float(self.label.text())
                        if str(end).endswith(".0"):
                            self.label.setText(str(end)[:-2])
                        else:
                            self.label.setText(str(end))
                    except (ValueError, OverflowError):
                        self.label.setText("Geçersiz İşlem")
                if object == self.label_33:
                    if self.label.text().endswith(".") or self.label.text().endswith("(") or self.label.text().endswith(")"):
                        pass
                    elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                        pass
                    elif self.label.text().endswith("+") or self.label.text().endswith("-") or self.label.text().endswith("*") or self.label.text().endswith("/"):
                        pass
                    else:
                        self.curopr = "x^y"
                        self.label.setText(self.label.text() + "**")
                if object == self.label_27:
                    if self.label.text().endswith(".") or self.label.text().endswith("(") or self.label.text().endswith(")"):
                        pass
                    elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                        pass
                    elif self.label.text().endswith("+") or self.label.text().endswith("-") or self.label.text().endswith("*") or self.label.text().endswith("/"):
                        pass
                    else:
                        self.curopr = "sqrroot"
                        self.label.setText(self.label.text() + "**0.5")
                if object == self.label_14: # negatif - pozitif sayı ayarlama düğmesi. Sorunlu çalışmaktadır.Düzeltilmesi gerekiyor.
                    if self.label.text().endswith("-"):
                        self.label.setText(self.label.text()[:-1] + "+")
                    elif self.label.text().endswith("+"):
                        self.label.setText(self.label.text()[:-1] + "-")
                    else:
                        self.label.setText(self.label.text() + "-")
                if object == self.label_29:
                    self.curopr = "log"
                    correct = True
                    for i in self.label.text():
                        if i in ["+","*","/","-"]:
                            self.label.setText("Geçersiz İşlem")
                            correct = False
                            break
                    if correct:
                        self.num1 = float(self.label.text())
                        self.label.setText("Taban Girin")
                        self.label_17.setEnabled(False)
                        self.label_18.setEnabled(False)
                        self.label_19.setEnabled(False)
                        self.label_20.setEnabled(False)
                        self.label_29.setEnabled(False)
                        self.label_33.setEnabled(False)
                        self.label_31.setEnabled(False)
                        self.label_34.setEnabled(False)
                        self.label_35.setEnabled(False)
                        self.label_36.setEnabled(False)
                        self.label_30.setEnabled(False)
                if object == self.label_31:
                    if self.label.text().endswith(".") or self.label.text().endswith("(") or self.label.text().endswith(")"):
                        pass
                    elif self.label.text() == "Geçersiz İşlem" or self.label.text() == "Taban Girin" or self.label.text() == "Üs Girin" or self.label.text() == "Mod Girin":
                        pass
                    elif self.label.text().endswith("+") or self.label.text().endswith("-") or self.label.text().endswith("*") or self.label.text().endswith("/"):
                        pass
                    else:
                        self.curopr = "mod"
                        self.label.setText(self.label.text() + "%")
                if object == self.label_34:
                    correct = True
                    for i in self.label.text():
                        if i in ["+","*","/","-"]:
                            self.label.setText("Geçersiz İşlem")
                            correct = False
                            break
                    if correct:
                        end = math.sin(math.radians(float(self.label.text())))
                        if str(end).endswith(".0"):
                            self.label.setText(str(end)[:-2])
                        else:
                            self.label.setText(str(end))
                if object == self.label_35:
                    correct = True
                    for i in self.label.text():
                        if i in ["+","*","/","-"]:
                            self.label.setText("Geçersiz İşlem")
                            correct = False
                            break
                    if correct:
                        end = math.cos(math.radians(float(self.label.text())))
                        if str(end).endswith(".0"):
                            self.label.setText(str(end)[:-2])
                        else:
                            self.label.setText(str(end))
                if object == self.label_36:
                    correct = True
                    for i in self.label.text():
                        if i in ["+","*","/","-"]:
                            self.label.setText("Geçersiz İşlem")
                            correct = False
                            break
                    if correct:
                        end = math.tan(math.radians(float(self.label.text())))
                        if str(end).endswith(".0"):
                            self.label.setText(str(end)[:-2])
                        else:
                            self.label.setText(str(end))
                if object == self.label_30:
                    correct = True
                    for i in self.label.text():
                        if i in ["+","*","/","-"]:
                            self.label.setText("Geçersiz İşlem")
                            correct = False
                            break
                    if correct:
                        end = math.exp(float(self.label.text()))
                        if str(end).endswith(".0"):
                            self.label.setText(str(end)[:-2])
                        else:
                            self.label.setText(str(end))

            self.label.setToolTip(self.label.text())
            return True
                    
        return False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scientific Calculator by Can Cakar"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_35.setText(_translate("MainWindow", "cos"))
        self.label_36.setText(_translate("MainWindow", "tan"))
        self.label_27.setText(_translate("MainWindow", "√"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">x</span><span style=\" font-size:20pt; vertical-align:super;\">2</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">x</span><span style=\" font-size:20pt; vertical-align:super;\">y</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "sin"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">10</span><span style=\" font-size:20pt; vertical-align:super;\">x</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "log"))
        self.label_31.setText(_translate("MainWindow", "Mod"))
        self.label_30.setText(_translate("MainWindow", "Exp"))
        self.label_13.setText(_translate("MainWindow", "."))
        self.label_21.setText(_translate("MainWindow", "="))
        self.label_23.setText(_translate("MainWindow", ")"))
        self.label_12.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.label_20.setText(_translate("MainWindow", "+"))
        self.label_5.setText(_translate("MainWindow", "3"))
        self.label_22.setText(_translate("MainWindow", "("))
        self.label_3.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "8"))
        self.label_9.setText(_translate("MainWindow", "7"))
        self.label_19.setText(_translate("MainWindow", "-"))
        self.label_7.setText(_translate("MainWindow", "5"))
        self.label_18.setText(_translate("MainWindow", "×"))
        self.label_8.setText(_translate("MainWindow", "6"))
        self.label_24.setText(_translate("MainWindow", "n!"))
        self.label_14.setText(_translate("MainWindow", "±"))
        self.label_6.setText(_translate("MainWindow", "4"))
        self.label_11.setText(_translate("MainWindow", "9"))
        self.label_17.setText(_translate("MainWindow", "÷"))
        self.label_26.setText(_translate("MainWindow", "↑"))
        self.label_25.setText(_translate("MainWindow", "π"))
        self.label_2.setText(_translate("MainWindow", "C"))
        self.label_15.setText(_translate("MainWindow", "⌫"))
        self.label_16.setText(_translate("MainWindow", "CE"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# ----------------Yapılacaklar Listesi----------------
# Yapılacaklar:
# 1 - Negatif - pozitif sayı tuşu sorunlu çalışmakta.
# 2 - Parantezler kullanımı şu anda gereksiz kalıyor ve kullanıcı parantezlerele hata meydana getirebilir.(hata ile programın kapanması engellendi)
# 4 - Yukarı ok tuşuna basılında fonksiyonel işlemler değiştirilecek ve yerlerine yenileri gösterilecek.
#       Örneğin log yerine ln gelecek, tan yerine cot gelecek, sin yerine 1/sin (csc) gelecek gibi.Ancak tekrar basıldığında eski haline dönecek.
#       farklı labellar tanımlayıp üstüne raise yapabiliriz veya self.log = True / False gibi işlemlerle aynı label(buton) üzerinden işlemi yapabiliriz.

# © 2019 CAN ÇAKAR | Open Source
