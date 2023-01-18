from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 900))
        MainWindow.setMaximumSize(QtCore.QSize(900, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 70, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setObjectName("label")
        self.playboutton = QtWidgets.QPushButton(self.centralwidget)
        self.playboutton.setGeometry(QtCore.QRect(220, 600, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        self.playboutton.setFont(font)
        self.playboutton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.playboutton.setStyleSheet("border-radius: 12px;\n"
"background:  rgba(209, 50, 38, 199);\n"
"")
        self.playboutton.setObjectName("playboutton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 140, 391, 381))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("venv/Sans titre55.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 810, 355, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "puissance4_menu"))
        self.label.setText(_translate("MainWindow", "four in a row"))
        self.playboutton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.playboutton.setText(_translate("MainWindow", "Play"))
        self.label_3.setText(_translate("MainWindow", u'Copyright © 2023 par Khadija Jaoua'))


