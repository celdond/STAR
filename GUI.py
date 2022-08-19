import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget

class dashboard(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)

class wishlist_selector_page(QWidget):

    def __init__(self):
        super().__init__()


class sign_in_window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STAR")

        sign_in_button = QPushButton("Sign In")
        sign_in_button.clicked.connect(self.check_sign_in)
        self.setCentralWidget(sign_in_button)

    def check_sign_in(self, checked):
        self.d = dashboard()
        self.d.show()


def main():

    star = QApplication(sys.argv)

    window = dashboard()
    window.show()

    star.exec()
    return

main()