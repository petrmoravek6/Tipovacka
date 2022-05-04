from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem


class GameSummaryWidget(QtWidgets.QWidget):
    def __init__(self, game, parent=None):
        super(GameSummaryWidget, self).__init__(parent)
        self.game = game
        game.update_results()
        self.setObjectName("game_summary")
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.resize(1320, 890)
        self.setMinimumSize(QtCore.QSize(1320, 890))
        self.setMaximumSize(QtCore.QSize(1320, 890))
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
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 32))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        self.verticalLayout.addWidget(self.tableWidget)
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

        self.retranslateUi()
        self.display()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("game_summary", "Souhrn hry"))
        item = self.summary_table.horizontalHeaderItem(0)
        item.setText(_translate("game_summary", "Odehraný zápas"))
        item = self.summary_table.horizontalHeaderItem(1)
        item.setText(_translate("game_summary", "Výsledek"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("game_summary", "CELKEM:"))
        self.back_btn.setText(_translate("game_summary", "Zpět"))

    def display(self):
        results = self.game.database.get_all_results_ordered_by_date()
        for idx, res in enumerate(results):
            self.summary_table.insertRow(idx)
            if res[0] == 'Group Stage':
                self.summary_table.setItem(idx, 0, QTableWidgetItem(
                    str(res[0]) + ": " + str(res[1]) + " - " + str(res[2])))
                self.summary_table.setItem(idx, 1, QTableWidgetItem(str(res[3]) + ":" + str(res[4])))
            else:
                continue
                # todo