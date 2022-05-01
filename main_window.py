from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QTableWidget, QDialog, QMainWindow, QApplication, QDialogButtonBox, QVBoxLayout, QLabel, \
    QWidget

from add_player_widget import AddPlayerWidget
from remove_player_widget import RemovePlayerWidget


class MainWindow(QMainWindow):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.setObjectName("MainWindow")
        self.resize(570, 390)
        self.setMinimumSize(QtCore.QSize(570, 390))
        self.setMaximumSize(QtCore.QSize(570, 390))
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(12, 20, 12, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftButtonsLayout = QtWidgets.QVBoxLayout()
        self.leftButtonsLayout.setObjectName("leftButtonsLayout")
        self.gif = QtWidgets.QLabel(self.widget)
        self.gif.setObjectName("gif")
        self.movie = QMovie("img/goal_gif.gif")
        self.leftButtonsLayout.addWidget(self.gif)
        self.game_summary_btn = QtWidgets.QPushButton(self.widget)
        self.game_summary_btn.setObjectName("game_summary_btn")
        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.game_summary_btn)
        self.leftButtonsLayout.addWidget(self.game_summary_btn)
        self.add_player_btn = QtWidgets.QPushButton(self.widget)
        self.add_player_btn.setObjectName("add_player_btn")
        self.add_player_btn.clicked.connect(self.add_player_clicked)
        self.buttonGroup.addButton(self.add_player_btn)
        self.leftButtonsLayout.addWidget(self.add_player_btn)
        self.remove_player_btn = QtWidgets.QPushButton(self.widget)
        self.remove_player_btn.setObjectName("remove_player_btn")
        self.remove_player_btn.clicked.connect(self.remove_player_clicked)
        self.buttonGroup.addButton(self.remove_player_btn)
        self.leftButtonsLayout.addWidget(self.remove_player_btn)
        self.player_details_btn = QtWidgets.QPushButton(self.widget)
        self.player_details_btn.setObjectName("player_details_btn")
        self.buttonGroup.addButton(self.player_details_btn)
        self.leftButtonsLayout.addWidget(self.player_details_btn)
        self.help_btn = QtWidgets.QPushButton(self.widget)
        self.help_btn.setObjectName("help_btn")
        self.buttonGroup.addButton(self.help_btn)
        self.leftButtonsLayout.addWidget(self.help_btn)
        self.end_btn = QtWidgets.QPushButton(self.widget)
        self.end_btn.setObjectName("end_btn")
        self.end_btn.clicked.connect(self.close)
        self.buttonGroup.addButton(self.end_btn)
        self.leftButtonsLayout.setSpacing(10)
        self.leftButtonsLayout.addWidget(self.end_btn)
        self.leftButtonsLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout.addLayout(self.leftButtonsLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rankingsTable = QTableWidget()
        self.rankingsTable.setObjectName("rankings_table")
        self.rankingsTable.setColumnCount(2)
        self.rankingsTable.setRowCount(0)
        self.rankingsTable.resize(300, 310)
        self.rankingsTable.setMinimumSize(QtCore.QSize(300, 310))
        self.rankingsTable.setMaximumSize(QtCore.QSize(300, 310))
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.rankingsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.rankingsTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.rankingsTable)
        self.reload_btn = QtWidgets.QPushButton(self.widget)
        self.reload_btn.setObjectName("reload_btn")
        self.reload_btn.clicked.connect(self.reload_btn_clicked)
        self.verticalLayout_3.addWidget(self.reload_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Tipovačka"))
        self.gif.setText(_translate("MainWindow", "GIF"))
        self.game_summary_btn.setText(_translate("MainWindow", "Souhrn hry"))
        self.add_player_btn.setText(_translate("MainWindow", "Přidat hráče"))
        self.remove_player_btn.setText(_translate("MainWindow", "Odebrat hráče"))
        self.player_details_btn.setText(_translate("MainWindow", "Procházet hráče"))
        self.help_btn.setText(_translate("MainWindow", "Nápověda"))
        self.end_btn.setText(_translate("MainWindow", "Konec"))
        self.reload_btn.setText(_translate("MainWindow", "Aktualizovat"))
        item = self.rankingsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Hráč"))
        item = self.rankingsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Body"))
        self.gif.setMovie(self.movie)
        self.movie.start()

    def add_player_clicked(self):
        wid = AddPlayerWidget(self.game)
        wid.show()

    def remove_player_clicked(self):
        wid = RemovePlayerWidget(self.game)
        wid.show()

    def reload_btn_clicked(self):
        self.game.update_results()
        # update tabulku

    def display_rankings_table(self):
        self.rankingsTable.set