# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(965, 609)
        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setGeometry(QtCore.QRect(350, 580, 250, 22))
        self.back_btn.setMaximumSize(QtCore.QSize(250, 16777215))
        self.back_btn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.back_btn.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        self.back_btn.setObjectName("back_btn")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 895, 541))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.back_btn.setText(_translate("Form", "Zpět"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Vítejte v aplikace/hře </span><span style=\" font-size:12pt; font-weight:700;\">Tipovačka</span><span style=\" font-size:12pt;\">. Účastníci této hry vyplní mimo tuto aplikaci tabulku, ve které tipují<br/>výsledky fotbalové soutěže </span><span style=\" font-size:12pt; font-weight:700;\">Ligy Mistrů</span><span style=\" font-size:12pt;\">, konrétně sézony 2021/22.<br/>Po vytvoření profilu v aplikaci je hráč zařazen do hry a jeho výsledky (body) se zobrazují na hlavní stránce. <br/>U zápasů základní skupinové fáze se tipují celé výsledky. <br/>Ve vyřazovací části se tipují pouze týmy, které tam postoupí a v neposlední řadě taky celý vítěz turnaje. <br/>Za každý správně uhodnutý výsledek skutečně odehraných zápasů hráč obdrží body dle pravidel následovně:</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">- Celý výsledek se skóre: 20 bodů<br/>- Výsledek bez skóre: 5 bodů<br/>- Osmifinalista: 10 bodů<br/>- Čtvrtfinalista: 15 bodů<br/>- Semifinalista: 25 bodů<br/>- Finalista: 75 bodů<br/>- Vítěz celého turnaje: 120 bodů</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><br/></p><p><span style=\" font-size:14pt;\">Hlavní stránka:</span></p><p><span style=\" font-size:10pt; font-weight:700;\">Souhrn hry</span><span style=\" font-size:10pt;\"> - Zobrazí již odehrané zápasy a k nim, jak si který hráč vedl.</span></p><p><span style=\" font-size:10pt; font-weight:700;\">Přidání hráče</span><span style=\" font-size:10pt;\"> - Po vyplnění unikátní přezdívky, jména a příjmení a vybrání souboru s natipovanými zápasy <br/>daného hráče bude hráč zařazen do hry a jeho body a statistiky bude možné v aplikaci najít. <br/>Pozor, soubor musí splňovat dané podmnky a musí být ve formátu CSV, jinak se zobrazí chybová hláška.</span></p><p><span style=\" font-size:10pt; font-weight:700;\">Odebrání hráče</span><span style=\" font-size:10pt;\"> - Po vybrání hráče ze seznamu a potvrzení tlačítkem &quot;Smazat&quot; dojde ke smazání hráčových tipů a bude vyřazen ze hry.</span></p><p><span style=\" font-size:10pt; font-weight:700;\">Procházet hráče </span><span style=\" font-size:10pt;\">- Ze seznamu vlevo po vybrání hráče dojde k zobrazení jeho natipovaných výsledků. <br/>Pokud jsou již známy výsledky, zobrazí se zde skutečný výsledek a udělené body.</span></p><p><span style=\" font-size:10pt; font-weight:700;\">Aktualizovat</span><span style=\" font-size:10pt;\"> - Dojde k aktualizování již odehraných utkání turnaje z internetu. <br/>K aktualizování dochází také při spuštění aplikace nebo v Souhrnu hry či Procházení hráče.</span></p><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())