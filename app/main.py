import sys

from PySide6.QtWidgets import QApplication, QMainWindow


def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("PDF Editor")
    window.resize(1400, 900)
    window.setMinimumSize(800, 600)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
