from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QTableWidgetItem
from app.src.rules import determine_points


class GameSummaryWidget(QtWidgets.QWidget):
    def __init__(self, game, parent=None):
        super(GameSummaryWidget, self).__init__(parent)
        self.game = game
        game.update_results()
        self.setObjectName("game_summary")
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.resize(1500, 890)
        self.setMinimumSize(QtCore.QSize(1500, 890))
        self.setMaximumSize(QtCore.QSize(1500, 890))
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.summary_table = QtWidgets.QTableWidget(self)
        self.summary_table.setEnabled(True)
        self.summary_table.setObjectName("summary_table")
        self.summary_table.setColumnCount(2)
        self.summary_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.summary_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.summary_table.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.summary_table)
        self.points_table = QtWidgets.QTableWidget(self)
        self.points_table.setMaximumSize(QtCore.QSize(16777215, 32))
        self.points_table.setObjectName("points_table")
        self.points_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        item.setSizeHint(QSize(530, 32))
        self.points_table.setVerticalHeaderItem(0, item)
        self.verticalLayout.addWidget(self.points_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addStretch()
        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(lambda: self.close())
        self.horizontalLayout.addWidget(self.back_btn)
        self.horizontalLayout.addStretch()
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.summary_table.setColumnWidth(0, 420)
        self.summary_table.setColumnWidth(1, 80)


        self.retranslateUi()
        self.display()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("game_summary", "Souhrn hry"))
        item = self.summary_table.horizontalHeaderItem(0)
        item.setText(_translate("game_summary", "Odehraný zápas / Postupující tým"))
        item = self.summary_table.horizontalHeaderItem(1)
        item.setText(_translate("game_summary", "Výsledek"))
        item = self.points_table.verticalHeaderItem(0)
        item.setText(_translate("game_summary", "CELKEM:"))
        self.back_btn.setText(_translate("game_summary", "Zpět"))
        self.points_table.horizontalHeader().hide()

    def display(self):
        results = self.game.database.get_all_results_ordered_by_date()
        players = self.game.database.get_all_players()
        pts_of_player = dict()
        for i, p in enumerate(players):
            self.summary_table.insertColumn(i + 2)
            self.summary_table.setHorizontalHeaderItem(i + 2, QTableWidgetItem(str(p[0])))
            self.points_table.insertColumn(i)
            pts_of_player[p[0]] = 0
        for idx, res in enumerate(results):
            self.summary_table.insertRow(idx)
            if res[0] == 'Group Stage':
                self.summary_table.setItem(idx, 0, QTableWidgetItem(str(res[0]) + ": " + str(res[1]) + " - " + str(res[2])))
                item = QTableWidgetItem(str(res[3]) + ":" + str(res[4]))
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.summary_table.setItem(idx, 1, item)
                for i, player in enumerate(players):
                    guess = self.game.database.get_match_guess_gs(player[0], 'Group Stage', res[1], res[2])
                    pts = determine_points(guess, res)
                    pts_of_player[player[0]] += pts
                    item = QTableWidgetItem('+' + str(pts))
                    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    self.summary_table.setItem(idx, i + 2, item)
            else:
                item = QTableWidgetItem("✓")
                item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.summary_table.setItem(idx, 1, item)
                if res[0] == 'Final-Full Result':
                    winner = res[1] if res[3] > res[4] else res[2]
                    self.summary_table.setItem(idx, 0, QTableWidgetItem("Winner: " + str(winner)))
                    self.fill_the_row_of_ks(idx, res, players, True, None, 'Winner', pts_of_player)
                elif res[0] == 'Final':
                    self.summary_table.setItem(idx, 0, QTableWidgetItem(str(res[0]) + ": " + str(res[1])))
                    self.fill_the_row_of_ks(idx, res, players, False, 1, res[0], pts_of_player)
                    idx += 1
                    self.summary_table.insertRow(idx)
                    self.summary_table.setItem(idx, 0, QTableWidgetItem(str(res[0]) + ": " + str(res[2])))
                    self.fill_the_row_of_ks(idx, res, players, False, 2, res[0], pts_of_player)
                else:
                    self.summary_table.setItem(idx, 0, QTableWidgetItem(str(res[0]) + ": " + str(res[1])))
                    self.fill_the_row_of_ks(idx, res, players, False, 1, res[0], pts_of_player)
        for i, pl in enumerate(players):
            self.points_table.setItem(0, i, QTableWidgetItem(str(pts_of_player[pl[0]])))

    def fill_the_row_of_ks(self, idx_row, res, players, try_second_res, team, phase, pts_of_player):
        for i, player in enumerate(players):
            if try_second_res:
                guess = self.game.database.get_match_guess_ks(player[0], phase, res[1])
                if guess is None:
                    guess = self.game.database.get_match_guess_ks(player[0], phase, res[2])
            else:
                guess = self.game.database.get_match_guess_ks(player[0], phase, res[team])
            pts = determine_points(guess, res)
            pts_of_player[player[0]] += pts
            item = QTableWidgetItem('+' + str(pts))
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.summary_table.setItem(idx_row, i + 2, item)
