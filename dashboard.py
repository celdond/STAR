import sys
from star import fetch_profile
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
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

        self.home = home_page(self)

        tabs.addTab(self.home, "Home")
        #tabs.addTab(steam_wishlist_page(), "Steam")
        #tabs.addTab(stats_page(), "Stats")
        self.setCentralWidget(tabs)

class home_page(QWidget):

    def __init__(self, dashboard_status):
        super().__init__()
        self.dashboard_status = dashboard_status

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
        self.entered_username = QLineEdit()
        self.entered_password = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(self.entered_username, 0, 1)
        layout.addWidget(self.entered_password, 1, 1)
        layout.addWidget(sign_in_button, 2, 1)

        page = QWidget()
        page.setLayout(layout)
        self.setCentralWidget(page)

    def check_sign_in(self, checked):
        if fetch_profile(self.entered_username, self.entered_password) == '/0':
            return
        d = dashboard()
        d.show()
        self.close()

def main():

    star = QApplication(sys.argv)

    window = sign_in_window()
    window.show()

    star.exec()
    return

main()