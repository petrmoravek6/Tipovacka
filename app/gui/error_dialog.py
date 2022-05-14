from PyQt6 import QtCore, QtWidgets


class UiErrorDialog(object):
    def setup_ui(self, error_dialog, text):
        self.text = text
        error_dialog.setObjectName("error_dialog")
        error_dialog.resize(400, 300)
        error_dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        error_dialog.setWindowTitle("Chyba!")
        self.msg = QtWidgets.QLabel(error_dialog)
        self.msg.setGeometry(QtCore.QRect(50, 40, 301, 201))
        self.msg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.msg.setObjectName("msg")

        self.retranslate_ui(error_dialog)
        QtCore.QMetaObject.connectSlotsByName(error_dialog)

    def retranslate_ui(self, error_dialog):
        _translate = QtCore.QCoreApplication.translate
        error_dialog.setWindowTitle(_translate("error_dialog", "Chyba"))
        self.msg.setText(_translate("error_dialog", self.text))
