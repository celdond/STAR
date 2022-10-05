import sys
import Star
import Steam
import threading
import random_methods as r_m
import os
import dialogues
from PySide6.QtCore import (
    Qt,
    QAbstractTableModel,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
    QGridLayout,
    QLineEdit,
    QCheckBox,
    QLabel,
    QTableView,
)

class wishlist_view(QAbstractTableModel):

    def __init__(self, data, parent = None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent = None):
        return self._data.shape[0]
        
    def columnCount(self, parent = None):
        return self._data.shape[1]

    def data(self, index, role = Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class dashboard(QMainWindow):

    def __init__(self, user):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.user = user
        self.path = os.path.join(os.getcwd(), "profiles", user)

        self.load_settings()

    def add_steam_tab(self):
        steam_wishlist = steam_wishlist_page(self.path, self.user)
        self.tabs.addTab(steam_wishlist, "Steam")
        return

    def load_settings(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.home = home_page(self, self.path, self.user)

        self.tabs.addTab(self.home, "Home")
        self.setCentralWidget(self.tabs)

        to_add = Star.load_window_settings(self.path)
        for x in to_add:
            if x == 's':
                self.add_steam_tab()
        return

class home_page(QWidget):

    def __init__(self, dashboard_status, path, user):
        super().__init__()
        self.dashboard_status = dashboard_status
        self.path = path
        self.user = user
        self.user_database = os.path.join(path, user) + '.db'
        add_button = QPushButton("Add List")
        add_button.clicked.connect(self.add_button)

        rand_button = QPushButton("Random")
        rand_button.clicked.connect(self.random_button_thread)

        self.platforms = platform_selection()

        self.wishlist_name = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(self.wishlist_name, 0, 0)
        layout.addWidget(add_button, 0, 1)
        layout.addWidget(rand_button, 1, 1)
        layout.addWidget(self.platforms, 0, 2)

        self.setLayout(layout)

    def add_button(self):
        Star.change_setting(self.path, "user", "steam", self.wishlist_name.text())
        self.dashboard_status.add_steam_tab()
        return

    def random_button_thread(self):
        button_thread = threading.Thread(target = self.random_button)
        button_thread.start()
        return

    def random_button(self):
        steam_state = self.platforms.steam_check.isChecked()
        shuffle_list = list()
        if steam_state:
            steam_conn = Star.check_setting(self.path, "user", "steam")
            Steam.steam_scrape( self.user_database, steam_conn)
            shuffle_list.append('steam')
        print(r_m.random_function(self.user_database, shuffle_list))
        return

class steam_wishlist_page(QWidget):

    def __init__(self, path: str, user: str):
        super().__init__()

        data = Star.load_database_external(path, user, 'steam')
        self.pandas_model = wishlist_view(data)
        table = QTableView()
        table.setModel(self.pandas_model)
        layout = QGridLayout()
        layout.addWidget(table, 0, 0)

        self.setLayout(layout)

class platform_selection(QWidget):

    def __init__(self):
        super().__init__()

        self.steam_check = QCheckBox("Steam")
        self.steam_check.setCheckState(Qt.Unchecked)

        layout = QGridLayout()
        layout.addWidget(self.steam_check, 0, 0)

        self.setLayout(layout)

class stats_page(QWidget):

    def __init__(self):
        super().__init__()

class sign_in_window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STAR")

        sign_in_button = QPushButton("Sign In")
        sign_in_button.clicked.connect(self.check_sign_in)
        profile_button = QPushButton("Create Profile")
        profile_button.clicked.connect(self.create_profile)
        self.entered_username = QLineEdit()
        self.entered_password = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(QLabel("Username"), 0, 0)
        layout.addWidget(QLabel("Password"), 1, 0)
        layout.addWidget(self.entered_username, 0, 1)
        layout.addWidget(self.entered_password, 1, 1)
        layout.addWidget(sign_in_button, 2, 1)
        layout.addWidget(profile_button, 2, 0)

        page = QWidget()
        page.setLayout(layout)
        self.setCentralWidget(page)

    def check_sign_in(self):
        if Star.fetch_profile(self.entered_username.text(), self.entered_password.text()) == '/0':
            fail_dialogue = dialogues.sign_in_failure_dialogue("Failure", "Username or password is incorrect.")
            fail_dialogue.exec()
            return
        d = dashboard(self.entered_username.text())
        d.show()
        self.close()

    def create_profile(self):
        if '/' in self.entered_username.text():
            print(self.entered_username.text())
            illegal_dialogue = dialogues.sign_in_failure_dialogue("Failure", "Character '/' is not allowed.")
            illegal_dialogue.exec()
            return
        taken = Star.build_user(self.entered_username.text(), self.entered_password.text())

        if taken == '/0':
            fail_dialogue = dialogues.sign_in_failure_dialogue("Username taken.")
            fail_dialogue.exec()
            return
        
        legal_dialogue = dialogues.sign_in_failure_dialogue("Profile Created", "Profile Successfully Created!")
        legal_dialogue.exec()
        return

def main():

    star = QApplication(sys.argv)

    window = sign_in_window()
    window.show()

    star.exec()
    return

main()