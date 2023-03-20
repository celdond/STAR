import sys
import source.gui.home as home
import source.gui.profile as profile
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
        self.profile_selection = None
        self.setWindowTitle("Dashboard")
        # self.path = os.path.join(os.getcwd(), "profiles", user)

        self.load_settings()

    def log_in(self):
        self.profile_selection.show()
        return
    
    def log_out(self):
        return

    def load_settings(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.home = home.home_page(self)
        self.profile_selection = profile.profile_window(self)
        self.creation = profile.create_profile(self)

        self.set_profile = QAction("Log In", self)
        self.set_profile.triggered.connect(self.log_in)
        self.clear_profile = QAction("Sign Out", self)
        self.clear_profile.triggered.connect(self.log_out)

        menu = self.menuBar()
        self.profile_menu = menu.addMenu("&Profile")
        self.profile_menu.addSeparator()
        self.profile_menu.addAction(self.set_profile)

        self.tabs.addTab(self.home, "Home")
        self.setCentralWidget(self.tabs)

        return

def main():

    star = QApplication(sys.argv)

    window = dashboard()
    window.show()

    star.exec()
    return

main()