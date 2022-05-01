from PyQt6 import QtWidgets, QtCore


class RemovePlayerWidget(QtWidgets.QWidget):
    def __init__(self, game, parent=None):
        super(RemovePlayerWidget, self).__init__(parent)
        self.game = game
        self.resize(400, 520)
        self.setMaximumSize(QtCore.QSize(400, 520))
        self.setMinimumSize(QtCore.QSize(400, 520))
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
        self.verticalLayout.addWidget(self.remove_btn)
        self.exit_btn = QtWidgets.QPushButton(self)
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(lambda: self.close())
        self.verticalLayout.addWidget(self.exit_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("removePlayerWidget", "Odebrání hráče ze hry"))
        self.remove_btn.setText(_translate("removePlayerWidget", "Smazat hráče"))
        self.exit_btn.setText(_translate("removePlayerWidget", "Odejít"))
