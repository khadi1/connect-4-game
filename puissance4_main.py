from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 900)
        MainWindow.setMinimumSize(QtCore.QSize(800, 900))
        MainWindow.setMaximumSize(QtCore.QSize(800, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.r_circle_01 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_01.setVisible(False)
        self.r_circle_01.setGeometry(QtCore.QRect(120, 560, 66, 66))
        self.r_circle_01.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_01.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_01.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_01.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_01.setObjectName("r_circle_01")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 50, 631, 689))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("venv/moyenne.png"))
        self.label.setObjectName("label")
        self.r_circle_02 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_02.setVisible(False)
        self.r_circle_02.setGeometry(QtCore.QRect(120, 470, 66, 66))
        self.r_circle_02.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_02.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_02.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_02.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_02.setObjectName("r_circle_02")
        self.r_circle_03 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_03.setVisible(False)
        self.r_circle_03.setGeometry(QtCore.QRect(120, 382, 66, 66))
        self.r_circle_03.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_03.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_03.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_03.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_03.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_03.setObjectName("r_circle_03")
        self.r_circle_04 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_04.setVisible(False)
        self.r_circle_04.setGeometry(QtCore.QRect(120, 294, 66, 66))
        self.r_circle_04.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_04.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_04.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_04.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_04.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_04.setObjectName("r_circle_04")
        self.r_circle_05 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_05.setVisible(False)
        self.r_circle_05.setGeometry(QtCore.QRect(120, 208, 66, 66))
        self.r_circle_05.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_05.setMaximumSize(QtCore.QSize(70, 66))
        self.r_circle_05.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_05.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_05.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_05.setObjectName("r_circle_05")
        self.r_circle_06 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_06.setVisible(False)
        self.r_circle_06.setGeometry(QtCore.QRect(120, 120, 66, 66))
        self.r_circle_06.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_06.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_06.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_06.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_06.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_06.setObjectName("r_circle_06")
        self.r_circle_24 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_24.setVisible(False)
        self.r_circle_24.setGeometry(QtCore.QRect(292, 294, 66, 66))
        self.r_circle_24.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_24.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_24.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_24.setObjectName("r_circle_24")
        self.r_circle_26 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_26.setVisible(False)
        self.r_circle_26.setGeometry(QtCore.QRect(292, 119, 66, 66))
        self.r_circle_26.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_26.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_26.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_26.setObjectName("r_circle_26")
        self.r_circle_25 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_25.setVisible(False)
        self.r_circle_25.setGeometry(QtCore.QRect(292, 208, 66, 66))
        self.r_circle_25.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_25.setMaximumSize(QtCore.QSize(70, 66))
        self.r_circle_25.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_25.setObjectName("r_circle_25")
        self.r_circle_22 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_22.setVisible(False)
        self.r_circle_22.setGeometry(QtCore.QRect(292, 470, 66, 66))
        self.r_circle_22.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_22.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_22.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_22.setObjectName("r_circle_22")
        self.r_circle_23 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_23.setVisible(False)
        self.r_circle_23.setGeometry(QtCore.QRect(292, 382, 66, 66))
        self.r_circle_23.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_23.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_23.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_23.setObjectName("r_circle_23")
        self.r_circle_21 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_21.setVisible(False)
        self.r_circle_21.setGeometry(QtCore.QRect(292, 560, 66, 66))
        self.r_circle_21.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_21.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_21.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_21.setObjectName("r_circle_21")
        self.r_circle_34 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_34.setVisible(False)
        self.r_circle_34.setGeometry(QtCore.QRect(380, 294, 66, 66))
        self.r_circle_34.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_34.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_34.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_34.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_34.setObjectName("r_circle_34")
        self.r_circle_36 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_36.setVisible(False)
        self.r_circle_36.setGeometry(QtCore.QRect(380, 119, 66, 66))
        self.r_circle_36.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_36.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_36.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_36.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_36.setObjectName("r_circle_36")
        self.r_circle_35 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_35.setVisible(False)
        self.r_circle_35.setGeometry(QtCore.QRect(379, 208, 66, 66))
        self.r_circle_35.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_35.setMaximumSize(QtCore.QSize(70, 66))
        self.r_circle_35.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_35.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_35.setObjectName("r_circle_35")
        self.r_circle_32 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_32.setVisible(False)
        self.r_circle_32.setGeometry(QtCore.QRect(380, 470, 66, 66))
        self.r_circle_32.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_32.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_32.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_32.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_32.setObjectName("r_circle_32")
        self.r_circle_33 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_33.setVisible(False)
        self.r_circle_33.setGeometry(QtCore.QRect(380, 382, 66, 66))
        self.r_circle_33.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_33.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_33.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_33.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_33.setObjectName("r_circle_33")
        self.r_circle_31 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_31.setVisible(False)
        self.r_circle_31.setGeometry(QtCore.QRect(379, 559, 66, 66))
        self.r_circle_31.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_31.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_31.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_31.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_31.setObjectName("r_circle_31")
        self.r_circle_44 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_44.setVisible(False)
        self.r_circle_44.setGeometry(QtCore.QRect(465, 294, 66, 66))
        self.r_circle_44.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_44.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_44.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_44.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_44.setObjectName("r_circle_44")
        self.r_circle_46 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_46.setVisible(False)
        self.r_circle_46.setGeometry(QtCore.QRect(465, 118, 66, 66))
        self.r_circle_46.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_46.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_46.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_46.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_46.setObjectName("r_circle_46")
        self.r_circle_45 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_45.setVisible(False)
        self.r_circle_45.setGeometry(QtCore.QRect(465, 208, 66, 66))
        self.r_circle_45.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_45.setMaximumSize(QtCore.QSize(70, 66))
        self.r_circle_45.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_45.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_45.setObjectName("r_circle_45")
        self.r_circle_42 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_42.setVisible(False)
        self.r_circle_42.setGeometry(QtCore.QRect(465, 470, 66, 66))
        self.r_circle_42.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_42.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_42.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_42.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_42.setObjectName("r_circle_42")
        self.r_circle_43 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_43.setVisible(False)
        self.r_circle_43.setGeometry(QtCore.QRect(465, 382, 66, 66))
        self.r_circle_43.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_43.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_43.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_43.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_43.setObjectName("r_circle_43")
        self.r_circle_41 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_41.setVisible(False)
        self.r_circle_41.setGeometry(QtCore.QRect(465, 559, 66, 66))
        self.r_circle_41.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_41.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_41.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_41.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_41.setObjectName("r_circle_41")
        self.r_circle_51 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_51.setVisible(False)
        self.r_circle_51.setGeometry(QtCore.QRect(552, 558, 66, 66))
        self.r_circle_51.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_51.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_51.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_51.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_51.setObjectName("r_circle_51")
        self.r_circle_55 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_55.setVisible(False)
        self.r_circle_55.setGeometry(QtCore.QRect(550, 208, 66, 66))
        self.r_circle_55.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_55.setMaximumSize(QtCore.QSize(70, 66))
        self.r_circle_55.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_55.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_55.setObjectName("r_circle_55")
        self.r_circle_52 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_52.setVisible(False)
        self.r_circle_52.setGeometry(QtCore.QRect(550, 470, 66, 66))
        self.r_circle_52.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_52.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_52.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_52.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_52.setObjectName("r_circle_52")
        self.r_circle_53 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_53.setVisible(False)
        self.r_circle_53.setGeometry(QtCore.QRect(550, 382, 66, 66))
        self.r_circle_53.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_53.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_53.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_53.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_53.setObjectName("r_circle_53")
        self.r_circle_56 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_56.setVisible(False)
        self.r_circle_56.setGeometry(QtCore.QRect(551, 119, 66, 66))
        self.r_circle_56.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_56.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_56.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_56.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_56.setObjectName("r_circle_56")
        self.r_circle_54 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_54.setVisible(False)
        self.r_circle_54.setGeometry(QtCore.QRect(550, 294, 66, 66))
        self.r_circle_54.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_54.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_54.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_54.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_54.setObjectName("r_circle_54")
        self.r_circle_64 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_64.setVisible(False)
        self.r_circle_64.setGeometry(QtCore.QRect(638, 294, 66, 66))
        self.r_circle_64.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_64.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_64.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_64.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_64.setObjectName("r_circle_64")
        self.r_circle_66 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_66.setVisible(False)
        self.r_circle_66.setGeometry(QtCore.QRect(638, 120, 66, 66))
        self.r_circle_66.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_66.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_66.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_66.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_66.setObjectName("r_circle_66")
        self.r_circle_65 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_65.setVisible(False)
        self.r_circle_65.setGeometry(QtCore.QRect(638, 208, 66, 66))
        self.r_circle_65.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_65.setMaximumSize(QtCore.QSize(70, 66))
        self.r_circle_65.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_65.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_65.setObjectName("r_circle_65")
        self.r_circle_62 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_62.setVisible(False)
        self.r_circle_62.setGeometry(QtCore.QRect(638, 470, 66, 66))
        self.r_circle_62.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_62.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_62.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_62.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_62.setObjectName("r_circle_62")
        self.r_circle_63 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_63.setVisible(False)
        self.r_circle_63.setGeometry(QtCore.QRect(638, 382, 66, 66))
        self.r_circle_63.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_63.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_63.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_63.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_63.setObjectName("r_circle_63")
        self.r_circle_61 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_61.setVisible(False)
        self.r_circle_61.setGeometry(QtCore.QRect(638, 558, 66, 66))
        self.r_circle_61.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_61.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_61.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_61.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_61.setObjectName("r_circle_61")
        self.r_circle_14 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_14.setVisible(False)
        self.r_circle_14.setGeometry(QtCore.QRect(208, 294, 66, 66))
        self.r_circle_14.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_14.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_14.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_14.setObjectName("r_circle_14")
        self.r_circle_16 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_16.setVisible(False)
        self.r_circle_16.setGeometry(QtCore.QRect(208, 120, 66, 66))
        self.r_circle_16.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_16.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_16.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_16.setObjectName("r_circle_16")
        self.r_circle_15 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_15.setVisible(False)
        self.r_circle_15.setGeometry(QtCore.QRect(208, 208, 66, 66))
        self.r_circle_15.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_15.setMaximumSize(QtCore.QSize(70, 66))
        self.r_circle_15.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_15.setObjectName("r_circle_15")
        self.r_circle_12 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_12.setVisible(False)
        self.r_circle_12.setGeometry(QtCore.QRect(208, 470, 66, 66))
        self.r_circle_12.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_12.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_12.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_12.setObjectName("r_circle_12")
        self.r_circle_13 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_13.setVisible(False)
        self.r_circle_13.setGeometry(QtCore.QRect(207, 383, 66, 66))
        self.r_circle_13.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_13.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_13.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_13.setObjectName("r_circle_13")
        self.r_circle_11 = QtWidgets.QFrame(self.centralwidget)
        self.r_circle_11.setVisible(False)
        self.r_circle_11.setGeometry(QtCore.QRect(208, 560, 66, 66))
        self.r_circle_11.setMinimumSize(QtCore.QSize(66, 66))
        self.r_circle_11.setMaximumSize(QtCore.QSize(66, 66))
        self.r_circle_11.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.r_circle_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.r_circle_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.r_circle_11.setObjectName("r_circle_11")
        self.c_circle_15 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_15.setVisible(False)
        self.c_circle_15.setGeometry(QtCore.QRect(208, 208, 66, 66))
        self.c_circle_15.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_15.setMaximumSize(QtCore.QSize(70, 66))
        self.c_circle_15.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_15.setObjectName("c_circle_15")
        self.c_circle_04 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_04.setVisible(False)
        self.c_circle_04.setGeometry(QtCore.QRect(120, 294, 66, 66))
        self.c_circle_04.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_04.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_04.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_04.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_04.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_04.setObjectName("c_circle_04")
        self.c_circle_06 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_06.setVisible(False)
        self.c_circle_06.setGeometry(QtCore.QRect(120, 120, 66, 66))
        self.c_circle_06.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_06.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_06.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_06.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_06.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_06.setObjectName("c_circle_06")
        self.c_circle_12 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_12.setVisible(False)
        self.c_circle_12.setGeometry(QtCore.QRect(208, 470, 66, 66))
        self.c_circle_12.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_12.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_12.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_12.setObjectName("c_circle_12")
        self.c_circle_11 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_11.setVisible(False)
        self.c_circle_11.setGeometry(QtCore.QRect(208, 560, 66, 66))
        self.c_circle_11.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_11.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_11.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_11.setObjectName("c_circle_11")
        self.c_circle_13 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_13.setVisible(False)
        self.c_circle_13.setGeometry(QtCore.QRect(207, 383, 66, 66))
        self.c_circle_13.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_13.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_13.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_13.setObjectName("c_circle_13")
        self.c_circle_16 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_16.setVisible(False)
        self.c_circle_16.setGeometry(QtCore.QRect(208, 120, 66, 66))
        self.c_circle_16.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_16.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_16.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_16.setObjectName("c_circle_16")
        self.c_circle_05 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_05.setVisible(False)
        self.c_circle_05.setGeometry(QtCore.QRect(120, 208, 66, 66))
        self.c_circle_05.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_05.setMaximumSize(QtCore.QSize(70, 66))
        self.c_circle_05.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_05.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_05.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_05.setObjectName("c_circle_05")
        self.c_circle_02 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_02.setVisible(False)
        self.c_circle_02.setGeometry(QtCore.QRect(120, 470, 66, 66))
        self.c_circle_02.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_02.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_02.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_02.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_02.setObjectName("c_circle_02")
        self.c_circle_14 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_14.setVisible(False)
        self.c_circle_14.setGeometry(QtCore.QRect(208, 294, 66, 66))
        self.c_circle_14.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_14.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_14.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_14.setObjectName("c_circle_14")
        self.c_circle_03 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_03.setVisible(False)
        self.c_circle_03.setGeometry(QtCore.QRect(120, 382, 66, 66))
        self.c_circle_03.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_03.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_03.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_03.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_03.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_03.setObjectName("c_circle_03")
        self.c_circle_25 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_25.setVisible(False)
        self.c_circle_25.setGeometry(QtCore.QRect(292, 208, 66, 66))
        self.c_circle_25.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_25.setMaximumSize(QtCore.QSize(70, 66))
        self.c_circle_25.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_25.setObjectName("c_circle_25")
        self.c_circle_36 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_36.setVisible(False)
        self.c_circle_36.setGeometry(QtCore.QRect(379, 119, 66, 66))
        self.c_circle_36.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_36.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_36.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_36.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_36.setObjectName("c_circle_36")
        self.c_circle_31 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_31.setVisible(False)
        self.c_circle_31.setGeometry(QtCore.QRect(378, 559, 66, 66))
        self.c_circle_31.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_31.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_31.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_31.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_31.setObjectName("c_circle_31")
        self.c_circle_32 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_32.setVisible(False)
        self.c_circle_32.setGeometry(QtCore.QRect(379, 469, 66, 66))
        self.c_circle_32.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_32.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_32.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_32.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_32.setObjectName("c_circle_32")
        self.c_circle_34 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_34.setVisible(False)
        self.c_circle_34.setGeometry(QtCore.QRect(379, 294, 66, 66))
        self.c_circle_34.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_34.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_34.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_34.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_34.setObjectName("c_circle_34")
        self.c_circle_35 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_35.setVisible(False)
        self.c_circle_35.setGeometry(QtCore.QRect(378, 208, 66, 66))
        self.c_circle_35.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_35.setMaximumSize(QtCore.QSize(70, 66))
        self.c_circle_35.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_35.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_35.setObjectName("c_circle_35")
        self.c_circle_24 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_24.setVisible(False)
        self.c_circle_24.setGeometry(QtCore.QRect(292, 294, 66, 66))
        self.c_circle_24.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_24.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_24.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_24.setObjectName("c_circle_24")
        self.c_circle_26 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_26.setVisible(False)
        self.c_circle_26.setGeometry(QtCore.QRect(292, 118, 66, 66))
        self.c_circle_26.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_26.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_26.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_26.setObjectName("c_circle_26")
        self.c_circle_23 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_23.setVisible(False)
        self.c_circle_23.setGeometry(QtCore.QRect(292, 382, 66, 66))
        self.c_circle_23.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_23.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_23.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_23.setObjectName("c_circle_23")
        self.c_circle_22 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_22.setVisible(False)
        self.c_circle_22.setGeometry(QtCore.QRect(292, 470, 66, 66))
        self.c_circle_22.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_22.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_22.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_22.setObjectName("c_circle_22")
        self.c_circle_21 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_21.setVisible(False)
        self.c_circle_21.setGeometry(QtCore.QRect(293, 559, 66, 66))
        self.c_circle_21.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_21.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_21.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_21.setObjectName("c_circle_21")
        self.c_circle_33 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_33.setVisible(False)
        self.c_circle_33.setGeometry(QtCore.QRect(379, 382, 66, 66))
        self.c_circle_33.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_33.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_33.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_33.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_33.setObjectName("c_circle_33")
        self.c_circle_45 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_45.setVisible(False)
        self.c_circle_45.setGeometry(QtCore.QRect(464, 208, 66, 66))
        self.c_circle_45.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_45.setMaximumSize(QtCore.QSize(70, 66))
        self.c_circle_45.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_45.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_45.setObjectName("c_circle_45")
        self.c_circle_56 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_56.setVisible(False)
        self.c_circle_56.setGeometry(QtCore.QRect(550, 118, 66, 66))
        self.c_circle_56.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_56.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_56.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_56.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_56.setObjectName("c_circle_56")
        self.c_circle_51 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_51.setVisible(False)
        self.c_circle_51.setGeometry(QtCore.QRect(551, 558, 66, 66))
        self.c_circle_51.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_51.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_51.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_51.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_51.setObjectName("c_circle_51")
        self.c_circle_52 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_52.setVisible(False)
        self.c_circle_52.setGeometry(QtCore.QRect(550, 471, 66, 66))
        self.c_circle_52.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_52.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_52.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_52.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_52.setObjectName("c_circle_52")
        self.c_circle_54 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_54.setVisible(False)
        self.c_circle_54.setGeometry(QtCore.QRect(550, 295, 66, 66))
        self.c_circle_54.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_54.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_54.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_54.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_54.setObjectName("c_circle_54")
        self.c_circle_55 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_55.setVisible(False)
        self.c_circle_55.setGeometry(QtCore.QRect(550, 208, 66, 66))
        self.c_circle_55.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_55.setMaximumSize(QtCore.QSize(70, 66))
        self.c_circle_55.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_55.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_55.setObjectName("c_circle_55")
        self.c_circle_44 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_44.setVisible(False)
        self.c_circle_44.setGeometry(QtCore.QRect(464, 294, 66, 66))
        self.c_circle_44.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_44.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_44.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_44.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_44.setObjectName("c_circle_44")
        self.c_circle_46 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_46.setVisible(False)
        self.c_circle_46.setGeometry(QtCore.QRect(464, 118, 66, 66))
        self.c_circle_46.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_46.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_46.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_46.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_46.setObjectName("c_circle_46")
        self.c_circle_43 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_43.setVisible(False)
        self.c_circle_43.setGeometry(QtCore.QRect(464, 382, 66, 66))
        self.c_circle_43.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_43.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_43.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_43.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_43.setObjectName("c_circle_43")
        self.c_circle_42 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_42.setVisible(False)
        self.c_circle_42.setGeometry(QtCore.QRect(464, 470, 66, 66))
        self.c_circle_42.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_42.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_42.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_42.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_42.setObjectName("c_circle_42")
        self.c_circle_41 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_41.setVisible(False)
        self.c_circle_41.setGeometry(QtCore.QRect(464, 559, 66, 66))
        self.c_circle_41.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_41.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_41.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_41.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_41.setObjectName("c_circle_41")
        self.c_circle_53 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_53.setVisible(False)
        self.c_circle_53.setGeometry(QtCore.QRect(550, 383, 66, 66))
        self.c_circle_53.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_53.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_53.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_53.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_53.setObjectName("c_circle_53")
        self.c_circle_65 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_65.setVisible(False)
        self.c_circle_65.setGeometry(QtCore.QRect(637, 207, 66, 66))
        self.c_circle_65.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_65.setMaximumSize(QtCore.QSize(70, 66))
        self.c_circle_65.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_65.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_65.setObjectName("c_circle_65")
        self.c_circle_64 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_64.setVisible(False)
        self.c_circle_64.setGeometry(QtCore.QRect(637, 294, 66, 66))
        self.c_circle_64.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_64.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_64.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_64.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_64.setObjectName("c_circle_64")
        self.c_circle_66 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_66.setVisible(False)
        self.c_circle_66.setGeometry(QtCore.QRect(637, 119, 66, 66))
        self.c_circle_66.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_66.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_66.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_66.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_66.setObjectName("c_circle_66")
        self.c_circle_63 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_63.setVisible(False)
        self.c_circle_63.setGeometry(QtCore.QRect(637, 382, 66, 66))
        self.c_circle_63.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_63.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_63.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_63.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_63.setObjectName("c_circle_63")
        self.c_circle_62 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_62.setVisible(False)
        self.c_circle_62.setGeometry(QtCore.QRect(637, 470, 66, 66))
        self.c_circle_62.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_62.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_62.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_62.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_62.setObjectName("c_circle_62")
        self.c_circle_61 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_61.setVisible(False)
        self.c_circle_61.setGeometry(QtCore.QRect(637, 558, 66, 66))
        self.c_circle_61.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_61.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_61.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_61.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_61.setObjectName("c_circle_61")
        self.c_circle_01 = QtWidgets.QFrame(self.centralwidget)
        self.c_circle_01.setVisible(False)
        self.c_circle_01.setGeometry(QtCore.QRect(120, 560, 66, 66))
        self.c_circle_01.setMinimumSize(QtCore.QSize(66, 66))
        self.c_circle_01.setMaximumSize(QtCore.QSize(66, 66))
        self.c_circle_01.setStyleSheet("QFrame{\n"
"border-radius:  32px;\n"
"background-color: rgb(255, 255, 127);\n"
"\n"
"}")
        self.c_circle_01.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.c_circle_01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c_circle_01.setObjectName("c_circle_01")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 30, 611, 681))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton__1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton__1.setMinimumSize(QtCore.QSize(67, 590))
        self.pushButton__1.setMaximumSize(QtCore.QSize(67, 590))
        self.pushButton__1.setStyleSheet("QPushButton{\n"
"background-color : rgba(255, 255, 255, 0);\n"
"border-color :   rgba(255, 255, 255, 0);\n"
"}")
        self.pushButton__1.setText("")
        self.pushButton__1.setObjectName("pushButton__1")
        self.horizontalLayout_2.addWidget(self.pushButton__1)
        self.pushButton__2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton__2.setMinimumSize(QtCore.QSize(67, 590))
        self.pushButton__2.setMaximumSize(QtCore.QSize(67, 590))
        self.pushButton__2.setStyleSheet("QPushButton{\n"
"background-color : rgba(255, 255, 255, 0);\n"
"border-color :   rgba(255, 255, 255, 0);\n"
"}")
        self.pushButton__2.setText("")
        self.pushButton__2.setObjectName("pushButton__2")
        self.horizontalLayout_2.addWidget(self.pushButton__2)
        self.pushButton__3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton__3.setMinimumSize(QtCore.QSize(67, 590))
        self.pushButton__3.setMaximumSize(QtCore.QSize(67, 590))
        self.pushButton__3.setStyleSheet("QPushButton{\n"
"background-color : rgba(255, 255, 255, 0);\n"
"border-color :   rgba(255, 255, 255, 0);\n"
"}")
        self.pushButton__3.setText("")
        self.pushButton__3.setObjectName("pushButton__3")
        self.horizontalLayout_2.addWidget(self.pushButton__3)
        self.pushButton__4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton__4.setMinimumSize(QtCore.QSize(67, 590))
        self.pushButton__4.setMaximumSize(QtCore.QSize(67, 590))
        self.pushButton__4.setStyleSheet("QPushButton{\n"
"background-color : rgba(255, 255, 255, 0);\n"
"border-color :   rgba(255, 255, 255, 0);\n"
"}")
        self.pushButton__4.setText("")
        self.pushButton__4.setObjectName("pushButton__4")
        self.horizontalLayout_2.addWidget(self.pushButton__4)
        self.pushButton__5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton__5.setMinimumSize(QtCore.QSize(67, 590))
        self.pushButton__5.setMaximumSize(QtCore.QSize(67, 590))
        self.pushButton__5.setStyleSheet("QPushButton{\n"
"background-color : rgba(255, 255, 255, 0);\n"
"border-color :   rgba(255, 255, 255, 0);\n"
"}")
        self.pushButton__5.setText("")
        self.pushButton__5.setObjectName("pushButton__5")
        self.horizontalLayout_2.addWidget(self.pushButton__5)
        self.pushButton__6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton__6.setMinimumSize(QtCore.QSize(67, 590))
        self.pushButton__6.setMaximumSize(QtCore.QSize(67, 590))
        self.pushButton__6.setStyleSheet("QPushButton{\n"
"background-color : rgba(255, 255, 255, 0);\n"
"border-color :   rgba(255, 255, 255, 0);\n"
"}")
        self.pushButton__6.setText("")
        self.pushButton__6.setObjectName("pushButton__6")
        self.horizontalLayout_2.addWidget(self.pushButton__6)
        self.pushButton__7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton__7.setMinimumSize(QtCore.QSize(67, 590))
        self.pushButton__7.setMaximumSize(QtCore.QSize(67, 590))
        self.pushButton__7.setStyleSheet("QPushButton{\n"
"background-color : rgba(255, 255, 255, 0);\n"
"border-color :   rgba(255, 255, 255, 0);\n"
"}")
        self.pushButton__7.setText("")
        self.pushButton__7.setObjectName("pushButton__7")
        self.horizontalLayout_2.addWidget(self.pushButton__7)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(5, 1)
        self.horizontalLayout_2.setStretch(6, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 770, 181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 770, 181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.player1_circle = QtWidgets.QFrame(self.centralwidget)
        self.player1_circle.setEnabled(False)
        self.player1_circle.setVisible(True)
        self.player1_circle.setGeometry(QtCore.QRect(-70, 610, 400, 400))
        self.player1_circle.setMinimumSize(QtCore.QSize(400, 400))
        self.player1_circle.setMaximumSize(QtCore.QSize(11111, 111113))
        self.player1_circle.setStyleSheet("QFrame{\n"
"border-radius:  200px;\n"
"background-color: rgb(255, 53, 124);\n"
"\n"
"}")
        self.player1_circle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.player1_circle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player1_circle.setObjectName("player1_circle")
        self.player1_circle_2 = QtWidgets.QFrame(self.centralwidget)
        self.player1_circle_2.setEnabled(False)
        self.player1_circle_2.setVisible(False)
        self.player1_circle_2.setGeometry(QtCore.QRect(460, 620, 400, 400))
        self.player1_circle_2.setMinimumSize(QtCore.QSize(400, 400))
        self.player1_circle_2.setMaximumSize(QtCore.QSize(11111, 111113))
        self.player1_circle_2.setStyleSheet("QFrame{\n"
"border-radius:  200px;\n"
"background-color:rgb(255, 195, 110)\n"
"\n"
"}")
        self.player1_circle_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.player1_circle_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player1_circle_2.setObjectName("player1_circle_2")
        self.exitbutton = QtWidgets.QFrame(self.centralwidget)
        self.exitbutton.setEnabled(False)
        self.exitbutton.setGeometry(QtCore.QRect(340, -80, 150, 150))
        self.exitbutton.setMinimumSize(QtCore.QSize(150, 150))
        self.exitbutton.setMaximumSize(QtCore.QSize(11111, 111113))
        self.exitbutton.setStyleSheet("QFrame{\n"
                                  "border-radius:  50px;\n"
                                  "background-color:rgb(116, 78, 45);\n"
                                  "}")
        self.exitbutton.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.exitbutton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exitbutton.setObjectName("exitbutton")
        self.label_2 = QtWidgets.QLabel(self.exitbutton)
        self.label_2.setGeometry(QtCore.QRect(45, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
                               "color : rgb(222, 222, 222);\n"
                               "}")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.b_invisiblexit = QtWidgets.QPushButton(self.exitbutton)
        self.b_invisiblexit.setGeometry(QtCore.QRect(10, 80, 131, 61))
        self.b_invisiblexit.setStyleSheet("QPushButton{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-color: rgba(255, 255, 255, 0);\n"
                                      "}")
        self.b_invisiblexit.setText("")
        self.b_invisiblexit.setObjectName("b_invisiblexit")
        self.circle_princ = QtWidgets.QFrame(self.centralwidget)
        self.circle_princ.setVisible(False)
        self.circle_princ.setEnabled(False)
        self.circle_princ.setGeometry(QtCore.QRect(140, 160, 511, 431))
        self.circle_princ.setMinimumSize(QtCore.QSize(400, 400))
        self.circle_princ.setMaximumSize(QtCore.QSize(11111, 111113))
        self.circle_princ.setStyleSheet("QFrame{\n"
                                    "border-radius:  200px;\n"
                                    "background-color:rgb(255, 195, 110)\n"
                                    "\n"
                                    "}")
        self.circle_princ.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circle_princ.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circle_princ.setObjectName("circle_princ")
        self.l_bravo = QtWidgets.QLabel(self.circle_princ)
        self.l_bravo.setGeometry(QtCore.QRect(20, 130, 481, 111))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pro M")
        font.setPointSize(48)
        self.l_bravo.setFont(font)
        self.l_bravo.setVisible(False)
        self.l_bravo.setStyleSheet("QLabel{\n"
                               "background-color: rgba(255, 255, 255, 0);\n"
                               "color: rgb(170, 0, 0);\n"
                               "}")
        self.l_bravo.setObjectName("l_bravo")
        self.l_joueur_gagnant = QtWidgets.QLabel(self.circle_princ)
        self.l_joueur_gagnant.setGeometry(QtCore.QRect(90, 190, 481, 111))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pro M")
        font.setPointSize(22)
        self.l_joueur_gagnant.setFont(font)
        self.l_joueur_gagnant.setVisible(False)
        self.l_joueur_gagnant.setStyleSheet("QLabel{\n"
                                        "background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(170, 0, 0);\n"
                                        "}")
        self.l_joueur_gagnant.setObjectName("l_joueur_gagnant")
        self.b_rejouer = QtWidgets.QPushButton(self.circle_princ)
        self.b_rejouer.setGeometry(QtCore.QRect(160, 310, 201, 41))
        self.b_rejouer.setVisible(False)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.player1_circle_2.raise_()
        self.player1_circle.raise_()
        self.label.raise_()
        self.r_circle_01.raise_()
        self.r_circle_02.raise_()
        self.r_circle_03.raise_()
        self.r_circle_04.raise_()
        self.r_circle_05.raise_()
        self.r_circle_06.raise_()
        self.r_circle_24.raise_()
        self.r_circle_26.raise_()
        self.r_circle_25.raise_()
        self.r_circle_22.raise_()
        self.r_circle_23.raise_()
        self.r_circle_21.raise_()
        self.r_circle_34.raise_()
        self.r_circle_36.raise_()
        self.r_circle_35.raise_()
        self.r_circle_32.raise_()
        self.r_circle_33.raise_()
        self.r_circle_31.raise_()
        self.r_circle_44.raise_()
        self.r_circle_46.raise_()
        self.r_circle_45.raise_()
        self.r_circle_42.raise_()
        self.r_circle_43.raise_()
        self.r_circle_41.raise_()
        self.r_circle_51.raise_()
        self.r_circle_55.raise_()
        self.r_circle_52.raise_()
        self.r_circle_53.raise_()
        self.r_circle_56.raise_()
        self.r_circle_54.raise_()
        self.r_circle_64.raise_()
        self.r_circle_66.raise_()
        self.r_circle_65.raise_()
        self.r_circle_62.raise_()
        self.r_circle_63.raise_()
        self.r_circle_61.raise_()
        self.r_circle_14.raise_()
        self.r_circle_16.raise_()
        self.r_circle_15.raise_()
        self.r_circle_12.raise_()
        self.r_circle_13.raise_()
        self.r_circle_11.raise_()
        self.c_circle_15.raise_()
        self.c_circle_04.raise_()
        self.c_circle_06.raise_()
        self.c_circle_12.raise_()
        self.c_circle_11.raise_()
        self.c_circle_13.raise_()
        self.c_circle_16.raise_()
        self.c_circle_05.raise_()
        self.c_circle_02.raise_()
        self.c_circle_14.raise_()
        self.c_circle_03.raise_()
        self.c_circle_25.raise_()
        self.c_circle_36.raise_()
        self.c_circle_31.raise_()
        self.c_circle_32.raise_()
        self.c_circle_34.raise_()
        self.c_circle_35.raise_()
        self.c_circle_24.raise_()
        self.c_circle_26.raise_()
        self.c_circle_23.raise_()
        self.c_circle_22.raise_()
        self.c_circle_21.raise_()
        self.c_circle_33.raise_()
        self.c_circle_45.raise_()
        self.c_circle_56.raise_()
        self.c_circle_51.raise_()
        self.c_circle_52.raise_()
        self.c_circle_54.raise_()
        self.c_circle_55.raise_()
        self.c_circle_44.raise_()
        self.c_circle_46.raise_()
        self.c_circle_43.raise_()
        self.c_circle_42.raise_()
        self.c_circle_41.raise_()
        self.c_circle_53.raise_()
        self.c_circle_65.raise_()
        self.c_circle_64.raise_()
        self.c_circle_66.raise_()
        self.c_circle_63.raise_()
        self.c_circle_62.raise_()
        self.c_circle_61.raise_()
        self.c_circle_01.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.b_invisiblexit.raise_()
        self.circle_princ.raise_()
        self.l_bravo.raise_()
        self.l_joueur_gagnant.raise_()
        self.b_rejouer.raise_()


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.horizontalLayoutWidget.setStyleSheet(_translate("MainWindow", "QPushButton{\n"
"background-color : rgba(255, 255, 255, 0);\n"
"border-color :   rgba(255, 255, 255, 0);\n"
"}"))
        self.label_4.setText(_translate("MainWindow", "player 1 "))
        self.label_5.setText(_translate("MainWindow", "player 2"))
        self.label_2.setText(_translate("MainWindow", "EXIT"))
        self.l_bravo.setText(_translate("MainWindow", "BRAVOOO!!!!!!"))
        self.l_joueur_gagnant.setText(_translate("MainWindow", "Le joueur a Gagné!!"))
        self.b_rejouer.setText(_translate("MainWindow", "rejouer"))

