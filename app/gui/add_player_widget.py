import os

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QFileDialog

from app.src.game import NicknameAlreadyInDatabase, BadCSVFile


class AddPlayerWidget(QtWidgets.QWidget):
    def __init__(self, game, main_window, parent=None):
        super(AddPlayerWidget, self).__init__(parent)
        self.game = game
        self.main_window = main_window
        self.nickname = ""
        self.name = ""
        self.csv_file_path = None
        self.resize(444, 320)
        self.setMinimumSize(QtCore.QSize(444, 320))
        self.setMaximumSize(QtCore.QSize(444, 320))
        self.setGeometry(QtCore.QRect(30, 30, 481, 321))
        self.setObjectName("addPlayerWidget")
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditNickname = QtWidgets.QLineEdit(self)
        self.lineEditNickname.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.lineEditNickname.setMaxLength(50)
        self.lineEditNickname.setObjectName("lineEditNickname")
        self.lineEditNickname.setPlaceholderText('Zadej nickname hráče')
        self.lineEditName = QtWidgets.QLineEdit(self)
        self.lineEditName.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.lineEditName.setMaxLength(50)
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditName.setPlaceholderText('Zadej jméno a příjmení hráče')
        self.verticalLayout.addWidget(self.lineEditNickname)
        self.verticalLayout.addWidget(self.lineEditName)
        self.addFileBtn = QtWidgets.QPushButton(self)
        self.addFileBtn.setObjectName("addFileBtn")
        self.addFileBtn.clicked.connect(lambda: self.select_file_btn_clicked())
        self.verticalLayout.addWidget(self.addFileBtn)
        self.infoLabel = QtWidgets.QLabel(self)
        self.infoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBtn = QtWidgets.QPushButton(self)
        self.addBtn.setObjectName("addBtn")
        self.addBtn.clicked.connect(lambda: self.add_btn_clicked())
        self.horizontalLayout.addWidget(self.addBtn)
        self.cancelBtn = QtWidgets.QPushButton(self)
        self.cancelBtn.setObjectName("cancelBtn")
        self.cancelBtn.clicked.connect(lambda: self.cancel_btn_clicked())
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("Přidání nového hráče")
        self.addFileBtn.setText(_translate("addPlayerWidget", "Vybrat soubor se zápasy"))
        self.infoLabel.setText(_translate("addPlayerWidget", ""))
        self.addBtn.setText(_translate("addPlayerWidget", "Přidat"))
        self.cancelBtn.setText(_translate("addPlayerWidget", "Odejít"))

    def add_btn_clicked(self):
        self.nickname = self.lineEditNickname.text()
        self.name = self.lineEditName.text()
        if self.nickname == '' or self.name == '':
            self.infoLabel.setText("Jméno a nickname nesmí být prázdné!")
            return
        if self.csv_file_path is None:
            self.infoLabel.setText("Je nutné vybrat soubor obsahující tabulku se zápasy")
            return
        try:
            self.game.add_player(self.nickname, self.name, self.csv_file_path)
        except NicknameAlreadyInDatabase:
            self.infoLabel.setText("Zadaný nickname pro hráče již ve hře existuje")
            return
        except BadCSVFile:
            self.infoLabel.setText("Vybraný soubor nesplňuje správné podmínky. \nZkontroluj, jestli byl vybrán "
                                   "správný soubor, \npříp. jestli je v něm vše vyplněno správně")
            return
        self.infoLabel.setText("Hráč byl úspěšně přidán do hry!")
        self.lineEditNickname.setText("")
        self.lineEditName.setText("")
        self.nickname = ''
        self.name = ''
        self.csv_file_path = None

    def cancel_btn_clicked(self):
        self.close()
        self.main_window.display_rankings_table()

    def select_file_btn_clicked(self):
        self.csv_file_path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Vyber tabulku s výsledky',
            directory=os.getcwd(),
            filter='CSV File (*.csv)'
        )[0]
