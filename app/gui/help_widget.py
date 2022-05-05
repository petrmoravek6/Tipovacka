from PyQt6 import QtWidgets, QtCore


class HelpWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HelpWidget, self).__init__(parent)
        self.setObjectName("helpWidget")
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.resize(965, 610)
        self.setMinimumSize(QtCore.QSize(965, 610))
        self.setMaximumSize(QtCore.QSize(965, 610))
        self.back_btn = QtWidgets.QPushButton()
        self.back_btn.setGeometry(QtCore.QRect(350, 580, 250, 22))
        self.back_btn.setMaximumSize(QtCore.QSize(250, 16777215))
        self.back_btn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(lambda: self.close())
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(15, 10, 15, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addStretch()
        self.h_box.addWidget(self.back_btn)
        self.h_box.addStretch()
        self.verticalLayout.addLayout(self.h_box)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("helpWidget", "Nápověda"))
        self.back_btn.setText(_translate("helpWidget", "Zpět"))
        self.label.setText(_translate("helpWidget",
                                      "<html><head/><body><p><span style=\" font-size:12pt;\">"
                                      "Vítejte v aplikace/hře </span><span style=\" font-size:12pt; font-weight:700;\">"
                                      "Tipovačka</span><span style=\" font-size:12pt;\">. "
                                      "Účastníci této hry vyplní mimo"
                                      " tuto aplikaci tabulku, ve které tipují<br/>výsledky fotbalové soutěže </span>"
                                      "<span style=\" font-size:12pt; font-weight:700;\">Ligy Mistrů</span><span style="
                                      "\" font-size:12pt;\">, konrétně sézony 2021/22.<br/>Po vytvoření profilu v "
                                      "aplikaci je hráč zařazen do hry a jeho výsledky (body) se zobrazují na hlavní "
                                      "stránce. <br/>U zápasů základní skupinové fáze se tipují celé výsledky. <br/>Ve "
                                      "vyřazovací části se tipují pouze týmy, které tam postoupí a v neposlední řadě "
                                      "taky celý vítěz turnaje. <br/>Za každý správně uhodnutý výsledek skutečně "
                                      "odehraných zápasů hráč obdrží body dle pravidel "
                                      "následovně:</span></p></body></html>"))
        self.label_2.setText(_translate("helpWidget",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">- Celý výsledek se "
                                        "skóre: 20 bodů<br/>- Výsledek bez skóre: 5 bodů<br/>- Osmifinalista: 10 bodů"
                                        "<br/>- Čtvrtfinalista: 15 bodů<br/>- Semifinalista: 25 bodů<br/>- Finalista: "
                                        "75 bodů<br/>- Vítěz celého turnaje: 120 bodů</span></p></body></html>"))
        self.label_3.setText(_translate("helpWidget",
                                        "<html><head/><body><p><br/></p><p><span style=\" font-size:14pt;\">Hlavní "
                                        "stránka:</span></p><p><span style=\" font-size:10pt; font-weight:700;\">"
                                        "Souhrn hry</span><span style=\" font-size:10pt;\"> - Zobrazí již odehrané "
                                        "zápasy a k nim, jak si který hráč vedl.</span></p><p><span style=\" font-size:"
                                        "10pt; font-weight:700;\">Přidání hráče</span><span style=\" font-size:10pt;\">"
                                        " - Po vyplnění unikátní přezdívky, jména a příjmení a vybrání souboru s "
                                        "natipovanými zápasy <br/>daného hráče bude hráč zařazen do hry a jeho body "
                                        "a statistiky bude možné v aplikaci najít. <br/>Pozor, soubor musí splňovat "
                                        "dané podmnky a musí být ve formátu CSV, jinak se zobrazí chybová hláška."
                                        "</span></p><p><span style=\" font-size:10pt; font-weight:700;\">Odebrání "
                                        "hráče</span><span style=\" font-size:10pt;\"> - Po vybrání hráče ze seznamu "
                                        "a potvrzení tlačítkem &quot;Smazat&quot; dojde ke smazání hráčových tipů a "
                                        "bude vyřazen ze hry.</span></p><p><span style=\" font-size:10pt; font-weight:"
                                        "700;\">Procházet hráče </span><span style=\" font-size:10pt;\">- Ze seznamu "
                                        "vlevo po vybrání hráče dojde k zobrazení jeho natipovaných výsledků. <br/>"
                                        "Pokud jsou již známy výsledky, zobrazí se zde skutečný výsledek a udělené "
                                        "body.</span></p><p><span style=\" font-size:10pt; font-weight:700;\">"
                                        "Aktualizovat</span><span style=\" font-size:10pt;\"> - Dojde k aktualizování "
                                        "již odehraných utkání turnaje z internetu. <br/>K aktualizování dochází "
                                        "také při spuštění aplikace nebo v Souhrnu hry či Procházení hráče.</span>"
                                        "</p><p><br/></p></body></html>"))
