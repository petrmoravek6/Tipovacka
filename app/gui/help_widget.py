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
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("helpWidget", "N??pov??da"))
        self.back_btn.setText(_translate("helpWidget", "Zp??t"))
        self.label.setText(_translate("helpWidget",
                                      "<html><head/><body><p><span style=\" font-size:12pt;\">"
                                      "V??tejte v aplikace/h??e </span><span style=\" font-size:12pt; font-weight:700;\">"
                                      "Tipova??ka</span><span style=\" font-size:12pt;\">. "
                                      "????astn??ci t??to hry vypln?? mimo"
                                      " tuto aplikaci tabulku, ve kter?? tipuj??<br/>v??sledky fotbalov?? sout????e </span>"
                                      "<span style=\" font-size:12pt; font-weight:700;\">Ligy Mistr??</span><span style="
                                      "\" font-size:12pt;\">, konr??tn?? s??zony 2021/22.<br/>Po vytvo??en?? profilu v "
                                      "aplikaci je hr???? za??azen do hry a jeho v??sledky (body) se zobrazuj?? na hlavn?? "
                                      "str??nce. <br/>U z??pas?? z??kladn?? skupinov?? f??ze se tipuj?? cel?? v??sledky. <br/>Ve "
                                      "vy??azovac?? ????sti se tipuj?? pouze t??my, kter?? tam postoup?? a v neposledn?? ??ad?? "
                                      "taky cel?? v??t??z turnaje. <br/>Za ka??d?? spr??vn?? uhodnut?? v??sledek skute??n?? "
                                      "odehran??ch z??pas?? hr???? obdr???? body dle pravidel "
                                      "n??sledovn??:</span></p></body></html>"))
        self.label_2.setText(_translate("helpWidget",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">- Cel?? v??sledek se "
                                        "sk??re: 20 bod??<br/>- V??sledek bez sk??re: 5 bod??<br/>- Osmifinalista: 10 bod??"
                                        "<br/>- ??tvrtfinalista: 15 bod??<br/>- Semifinalista: 25 bod??<br/>- Finalista: "
                                        "75 bod??<br/>- V??t??z cel??ho turnaje: 125 bod??</span></p></body></html>"))
        self.label_3.setText(_translate("helpWidget",
                                        "<html><head/><body><p><br/></p><p><span style=\" font-size:14pt;\">Hlavn?? "
                                        "str??nka:</span></p><p><span style=\" font-size:10pt; font-weight:700;\">"
                                        "Souhrn hry</span><span style=\" font-size:10pt;\"> - Zobraz?? ji?? odehran?? "
                                        "z??pasy a k nim, jak si kter?? hr???? vedl.</span></p><p><span style=\" font-size:"
                                        "10pt; font-weight:700;\">P??id??n?? hr????e</span><span style=\" font-size:10pt;\">"
                                        " - Po vypln??n?? unik??tn?? p??ezd??vky, jm??na a p????jmen?? a vybr??n?? souboru s "
                                        "natipovan??mi z??pasy <br/>dan??ho hr????e bude hr???? za??azen do hry a jeho body "
                                        "a statistiky bude mo??n?? v aplikaci naj??t. <br/>Pozor, soubor mus?? spl??ovat "
                                        "dan?? podmnky a mus?? b??t ve form??tu CSV, jinak se zobraz?? chybov?? hl????ka."
                                        "</span></p><p><span style=\" font-size:10pt; font-weight:700;\">Odebr??n?? "
                                        "hr????e</span><span style=\" font-size:10pt;\"> - Po vybr??n?? hr????e ze seznamu "
                                        "a potvrzen?? tla????tkem &quot;Smazat&quot; dojde ke smaz??n?? hr????ov??ch tip?? a "
                                        "bude vy??azen ze hry.</span></p><p><span style=\" font-size:10pt; font-weight:"
                                        "700;\">Proch??zet hr????e </span><span style=\" font-size:10pt;\">- Ze seznamu "
                                        "vlevo po vybr??n?? hr????e dojde k zobrazen?? jeho natipovan??ch v??sledk??. <br/>"
                                        "Pokud jsou ji?? zn??my v??sledky, zobraz?? se zde skute??n?? v??sledek a ud??len?? "
                                        "body.</span></p><p><span style=\" font-size:10pt; font-weight:700;\">"
                                        "Aktualizovat</span><span style=\" font-size:10pt;\"> - Dojde k aktualizov??n?? "
                                        "ji?? odehran??ch utk??n?? turnaje z internetu. <br/>K aktualizov??n?? doch??z?? "
                                        "tak?? p??i spu??t??n?? aplikace nebo v Souhrnu hry ??i Proch??zen?? hr????e.</span>"
                                        "</p><p><br/></p></body></html>"))
