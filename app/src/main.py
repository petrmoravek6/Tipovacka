import requests as requests
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from app.gui.error_dialog import UiErrorDialog
from app.src.game import Game
from app.gui.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        game = Game()
    except requests.exceptions.RequestException:
        errorDialog = QtWidgets.QDialog()
        ui = UiErrorDialog()
        ui.setup_ui(errorDialog, "Chyba připojení k internetu.\nZkontrolujte své připojení a spusťe znovu.")
        errorDialog.show()
    except AttributeError:
        errorDialog = QtWidgets.QDialog()
        ui = UiErrorDialog()
        ui.setup_ui(errorDialog, "Interní chyba při získávání dat z internetu.\nKontaktujte vývojáře.")
        errorDialog.show()
    else:
        win = MainWindow(game)
        win.show()
    sys.exit(app.exec())
