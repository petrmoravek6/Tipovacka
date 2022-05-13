from PyQt6 import QtWidgets, QtCore


class RemovePlayerWidget(QtWidgets.QWidget):
    def __init__(self, game, main_window, parent=None):
        super(RemovePlayerWidget, self).__init__(parent)
        self.game = game
        self.main_window = main_window
        self.resize(380, 410)
        self.setMaximumSize(QtCore.QSize(380, 410))
        self.setMinimumSize(QtCore.QSize(380, 410))
        self.setObjectName("removePlayerWidget")
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.remove_btn = QtWidgets.QPushButton(self)
        self.remove_btn.setObjectName("remove_btn")
        self.remove_btn.clicked.connect(self.remove_btn_clicked)
        self.verticalLayout.addWidget(self.remove_btn)
        self.exit_btn = QtWidgets.QPushButton(self)
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(lambda: self.cancel_btn_clicked())
        self.verticalLayout.addWidget(self.exit_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.display_list_of_players()
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("removePlayerWidget", "Odebrání hráče ze hry"))
        self.remove_btn.setText(_translate("removePlayerWidget", "Smazat hráče"))
        self.exit_btn.setText(_translate("removePlayerWidget", "Odejít"))

    def remove_btn_clicked(self):
        if self.listWidget.currentItem() is None:
            return
        self.game.database.del_player(str(self.listWidget.currentItem().text()))
        self.display_list_of_players()

    def display_list_of_players(self):
        self.listWidget.clear()
        for idx, nickname in enumerate(self.game.database.get_all_players()):
            self.listWidget.insertItem(idx, nickname[0])

    def cancel_btn_clicked(self):
        self.close()
        self.main_window.display_rankings_table()
