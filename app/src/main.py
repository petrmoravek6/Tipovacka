from PyQt6.QtWidgets import QApplication

from app.src.game import Game
from app.gui.main_window import MainWindow


if __name__ == "__main__":
    import sys
    game = Game()
    app = QApplication(sys.argv)
    win = MainWindow(game)
    win.show()
    sys.exit(app.exec())
