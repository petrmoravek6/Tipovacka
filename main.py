from PyQt6.QtWidgets import QTableWidget, QDialog, QMainWindow, QApplication, QDialogButtonBox, QVBoxLayout, QLabel, \
    QWidget

from game import Game
from main_window import MainWindow


if __name__ == "__main__":
    import sys
    game = Game()
    app = QApplication(sys.argv)
    win = MainWindow(game)
    win.show()
    sys.exit(app.exec())
