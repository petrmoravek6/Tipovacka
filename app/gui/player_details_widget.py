from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem

from app.src.rules import determine_points


class PlayerDetailsWidget(QtWidgets.QWidget):
    def __init__(self, game, parent=None):
        super(PlayerDetailsWidget, self).__init__(parent)
        self.game = game
        try:
            self.game.update_results()
        except Exception:
            pass
        self.setObjectName("playerDetailsWidget")
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.resize(1280, 720)
        self.setMinimumSize(QtCore.QSize(1280, 720))
        self.setMaximumSize(QtCore.QSize(1280, 720))
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listOfPlayers = QtWidgets.QListWidget(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.listOfPlayers.sizePolicy().hasHeightForWidth())
        self.listOfPlayers.setSizePolicy(size_policy)
        self.listOfPlayers.setObjectName("listOfPlayers")
        self.listOfPlayers.clicked.connect(lambda: self.display_players_statistics())
        self.horizontalLayout.addWidget(self.listOfPlayers)
        self.table = QtWidgets.QTableWidget(self)
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        self.table.setSortingEnabled(True)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()

        item.setFont(font)
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.table.setHorizontalHeaderItem(4, item)
        self.set_column_width()
        self.horizontalLayout.addWidget(self.table)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.horizontalLayout2.addStretch()
        self.back_btn = QtWidgets.QPushButton(self)
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(lambda: self.close())
        self.horizontalLayout2.addWidget(self.back_btn)
        self.horizontalLayout2.addStretch()
        self.verticalLayout.addLayout(self.horizontalLayout2)
        self.display_list_of_players()

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def set_column_width(self):
        self.table.setColumnWidth(0, 172)
        self.table.setColumnWidth(1, 395)
        self.table.setColumnWidth(2, 152)
        self.table.setColumnWidth(3, 152)
        self.table.setColumnWidth(4, 100)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("playerDetailsWidget", "Proch??zet hr????e"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("playerDetailsWidget", "F??ze"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("playerDetailsWidget", "Z??pas / Postupuj??c?? t??m"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("playerDetailsWidget", "M??j v??sledek"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("playerDetailsWidget", "V??sledek"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("playerDetailsWidget", "Body"))
        self.back_btn.setText(_translate("playerDetailsWidget", "Zp??t"))

    def display_list_of_players(self):
        self.listOfPlayers.clear()
        for idx, nickname in enumerate(self.game.database.get_all_players()):
            self.listOfPlayers.insertItem(idx, nickname[0])

    def display_players_statistics(self):
        player = self.listOfPlayers.currentItem()
        self.table.setRowCount(0)
        matches = self.game.database.get_all_match_guesses(str(player.text()))
        for idx, guess in enumerate(matches):
            self.table.insertRow(idx)
            self.table.setItem(idx, 0, QTableWidgetItem(guess[1]))
            phase = str(guess[1])
            if phase == 'Group Stage':
                self.table.setItem(idx, 1, QTableWidgetItem(str(guess[2]) + ' : ' + str(guess[3])))
                self.table.setItem(idx, 2, QTableWidgetItem(str(guess[4]) + ' : ' + str(guess[5])))
                res = self.game.database.get_match_result('Group Stage', guess[2], guess[3])
                self.table.setItem(idx, 3, QTableWidgetItem(str(res[3]) + ' : ' + str(res[4])))
                self.table.setItem(idx, 4, QTableWidgetItem(str(determine_points(guess, res))))
            else:
                self.table.setItem(idx, 1, QTableWidgetItem(str(guess[2])))
                self.table.setItem(idx, 2, QTableWidgetItem(""))
                if phase == 'Final':
                    res = self.game.database.get_match_result_by_phase_and_home_team(phase, guess[2])
                    if res is None:
                        res = self.game.database.get_match_result_by_phase_and_away_team(phase, guess[2])
                elif phase == 'Winner':
                    res = self.game.database.get_match_result_by_phase_and_home_team("Final-Full Result", guess[2])
                    if res is None:
                        res = self.game.database.get_match_result_by_phase_and_away_team("Final-Full Result", guess[2])
                else:
                    res = self.game.database.get_match_result_by_phase_and_home_team(phase, guess[2])
                pts = determine_points(guess, res)
                if pts == 0:
                    self.table.setItem(idx, 3, QTableWidgetItem("X"))
                else:
                    self.table.setItem(idx, 3, QTableWidgetItem("???"))
                self.table.setItem(idx, 4, QTableWidgetItem(str(pts)))
