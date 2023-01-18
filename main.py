from PyQt5 import QtWidgets
from puissance4_splash import Ui_SplashWindow
from puissance4_main import Ui_MainWindow
from game_controller import Game

import sys


class Jeu:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SplashWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ui2 = Ui_MainWindow()

    def changerpage(self):
        self.MainWindow.close()
        self.ui2.setupUi(self.MainWindow)
        self.MainWindow.show()
        game = Game(self.ui2)
        game.play()


j = Jeu()
j.ui.playboutton.clicked.connect(j.changerpage)

sys.exit(j.app.exec_())
