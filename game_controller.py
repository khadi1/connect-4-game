import numpy as np
from PyQt5 import QtWidgets


def b():
    print("exit pressed")


def position_a_remplir(j):
    i = 5
    while Game.grille[i][j] != 0:
        i = i - 1
    return i


def affichage_cercle(ui2, i, j):
    if Game.player == 1:
        circleName = "r_circle_" + str(j) + str(5 - i + 1)
        print(circleName)
    elif Game.player == 2:
        circleName = "c_circle_" + str(j) + str(5 - i + 1)
        print(circleName)
    circle = ui2.centralwidget.findChild(QtWidgets.QFrame, circleName)
    circle.setVisible(True)


def changement_jeueur(ui2, winner):
    if not winner:
        if Game.player == 1:
            circle = ui2.centralwidget.findChild(QtWidgets.QFrame, "player1_circle")
            circle.setVisible(False)
            circle = ui2.centralwidget.findChild(QtWidgets.QFrame, "player1_circle_2")
            circle.setVisible(True)
        elif Game.player == 2:
            circle = ui2.centralwidget.findChild(QtWidgets.QFrame, "player1_circle")
            circle.setVisible(True)
            circle = ui2.centralwidget.findChild(QtWidgets.QFrame, "player1_circle_2")
            circle.setVisible(False)


class Game:
    grille = np.zeros((6, 7), dtype=int)
    player = 1


    def __init__(self, ui2):
        self.ui2 = ui2
        print(Game.grille)
        self.winner = 0

    def play(self):

        self.ui2.pushButton__1.clicked.connect(lambda: self.remplir(1))
        self.ui2.pushButton__2.clicked.connect(lambda: self.remplir(2))
        self.ui2.pushButton__3.clicked.connect(lambda: self.remplir(3))
        self.ui2.pushButton__4.clicked.connect(lambda: self.remplir(4))
        self.ui2.pushButton__5.clicked.connect(lambda: self.remplir(5))
        self.ui2.pushButton__6.clicked.connect(lambda: self.remplir(6))
        self.ui2.pushButton__7.clicked.connect(lambda: self.remplir(7))

    def remplir(self, x):
        j = x - 1
        i = position_a_remplir(j)
        Game.grille[i][j] = Game.player
        print(Game.grille)
        affichage_cercle(self.ui2, i, j)
        self.win()
        changement_jeueur(self.ui2, self.winner)
        if self.winner == 0:
            Game.player = Game.player % 2 + 1

    def end(self):
        self.ui2.pushButton__1.setEnabled(False)
        self.ui2.pushButton__2.setEnabled(False)
        self.ui2.pushButton__3.setEnabled(False)
        self.ui2.pushButton__4.setEnabled(False)
        self.ui2.pushButton__5.setEnabled(False)
        self.ui2.pushButton__6.setEnabled(False)
        self.ui2.pushButton__7.setEnabled(False)
        self.ui2.centralwidget.findChild(QtWidgets.QFrame, "circle_princ").setVisible(True)
        self.ui2.centralwidget.findChild(QtWidgets.QLabel, "l_bravo").setVisible(True)
        self.ui2.centralwidget.findChild(QtWidgets.QLabel, "l_joueur_gagnant").setText(
            "le joueur{} a gagne!".format(Game.player))
        self.ui2.centralwidget.findChild(QtWidgets.QLabel, "l_joueur_gagnant").setVisible(True)

    def win(self):
        for x in range(len(Game.grille)):
            for y in range(len(Game.grille[x])):
                for turn in [1, 2]:
                    try:
                        if Game.grille[x][y] == turn and Game.grille[x][y + 1] == turn and Game.grille[x][
                            y + 2] == turn and Game.grille[x][y + 3]: pass
                    except:
                        pass
                    else:
                        if Game.grille[x][y] == turn and Game.grille[x][y + 1] == turn and Game.grille[x][
                            y + 2] == turn and Game.grille[x][y + 3] == turn:
                            self.winner = turn
                    try:
                        if Game.grille[x][y] == turn and Game.grille[x + 1][y + 1] == turn and Game.grille[x + 2][
                            y + 2] == turn and Game.grille[x + 3][y + 3]: pass
                    except:
                        pass
                    else:
                        if Game.grille[x][y] == turn and Game.grille[x + 1][y + 1] == turn and Game.grille[x + 2][
                            y + 2] == turn and Game.grille[x + 3][y + 3] == turn:
                            self.winner = turn

                    try:
                        if Game.grille[x][y] == turn and Game.grille[x + 1][y] == turn and Game.grille[x + 2][
                            y] == turn and Game.grille[x + 3][y]: pass
                    except:
                        pass
                    else:
                        if Game.grille[x][y] == turn and Game.grille[x + 1][y] == turn and Game.grille[x + 2][
                            y] == turn and Game.grille[x + 3][y] == turn:
                            self.winner = turn

                    try:
                        if Game.grille[x][y] == turn and Game.grille[x - 1][y + 1] == turn and Game.grille[x - 2][
                            y + 2] == turn and Game.grille[x - 3][y + 3]: pass
                    except:
                        pass
                    else:
                        if Game.grille[x][y] == turn and Game.grille[x - 1][y + 1] == turn and Game.grille[x - 2][
                            y + 2] == turn and Game.grille[x - 3][y + 3] == turn:
                            self.winner = turn
        if self.winner != 0:
            print("Bravooo! , le joueur {} est le gagnant!".format(Game.player))
            self.end()
