import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
    QGridLayout,
    QLineEdit,
)

class dashboard(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)

        self.home = home_page()

        tabs.addTab(self.home, "Home")
        tabs.addTab(steam_wishlist_page(), "Steam")
        tabs.addTab(stats_page(), "Stats")
        self.setCentralWidget(tabs)

class home_page(QWidget):

    def __init__(self):
        super().__init__()

        add_button = QPushButton("Add List")
        add_button.clicked.connect(self.add_button)
        wishlist_name = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(wishlist_name, 0, 0)
        layout.addWidget(add_button, 0, 1)

        self.setLayout(layout)

    def add_button(self):
        pass

class steam_wishlist_page(QWidget):

    def __init__(self):
        super().__init__()

        rand_button = QPushButton("Random")
        rand_button.clicked.connect(self.random_button)
        
        layout = QGridLayout()
        layout.addWidget(rand_button, 0, 1)

        self.setLayout(layout)
    
    def random_button(self):
        pass

class stats_page(QWidget):

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

def fetch_profile():

    return

def main():

    star = QApplication(sys.argv)

    window = dashboard()
    window.show()

    star.exec()
    return

main()