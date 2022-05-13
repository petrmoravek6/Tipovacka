from PyQt6 import QtCore, QtWidgets


class UiErrorDialog(object):
    def setupUi(self, errorDialog, text):
        self.text = text
        errorDialog.setObjectName("errorDialog")
        errorDialog.resize(400, 300)
        errorDialog.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Czech, QtCore.QLocale.Country.Czechia))
        errorDialog.setWindowTitle("Chyba!")
        self.msg = QtWidgets.QLabel(errorDialog)
        self.msg.setGeometry(QtCore.QRect(50, 40, 301, 201))
        self.msg.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.msg.setObjectName("msg")

        self.retranslateUi(errorDialog)
        QtCore.QMetaObject.connectSlotsByName(errorDialog)

    def retranslateUi(self, errorDialog):
        _translate = QtCore.QCoreApplication.translate
        errorDialog.setWindowTitle(_translate("errorDialog", "Chyba"))
        self.msg.setText(_translate("errorDialog", self.text))
