import sys
import source.components.random_selection as random_selection
import source.components.profile as profile
import source.components.platforms as platforms
import source.components.dialogues as dialogues
import source.components.home as home
import os
from PySide6.QtGui import (
    QAction,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
)

class dashboard(QMainWindow):

    def __init__(self):
        super().__init__()
        self.current_profile = None
        self.scraping = 0
        self.path = None
        self.setWindowTitle("Dashboard")
        self._generate_UI()

    def _generate_UI(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.setCentralWidget(self.tabs)
        self.profile_selection = profile.profile_window(self)
        self.add_platform = platforms.platforms_window(self)

        self.set_profile = QAction("Select Profile", self)
        self.set_profile.triggered.connect(self.log_in)
        self.clear_profile = QAction("Sign Out", self)
        self.clear_profile.triggered.connect(self.log_out)

        menu = self.menuBar()
        self.profile_menu = menu.addMenu("&Profile")

        self.load_settings()

    def profile_change(self):
        self.clear_dashboard()
        self.load_settings()
        return

    def log_in(self):
        self.profile_selection.show()
        return
    
    def log_out(self):
        self.current_profile = None
        self.path = None
        self.profile_change()
        return
    
    def clear_dashboard(self):
        for i in reversed(range(self.tabs.count())):
            t = self.tabs.widget(i)
            self.tabs.removeTab(i)
            t.deleteLater()

        self.profile_menu.clear()
        return

    def load_settings(self):
        self.random = random_selection.random_page(self)

        self.profile_menu.addSeparator()
        self.profile_menu.addAction(self.set_profile)
        if self.current_profile is not None:
            profile_home = home.home_page(self)
            self.tabs.addTab(profile_home, "Home")
            self.profile_menu.addAction(self.clear_profile)
            self.path = os.path.join(os.getcwd(), "profiles", self.current_profile)
            self.database_path = os.path.join(self.path, self.current_profile + '.db')

        self.tabs.addTab(self.random, "Random")
        return

def main():

    star = QApplication(sys.argv)

    window = dashboard()
    window.show()

    star.exec()
    return

main()