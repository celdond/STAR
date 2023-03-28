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

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.setCentralWidget(self.tabs)
        self.profile_selection = profile.profile_window(self)

        menu = self.menuBar()
        self.profile_menu = menu.addMenu("&Profile")

        self.load_settings()

    def log_in(self):
        self.profile_selection.show()
        return
    
    def log_out(self):
        self.profile_selection = None
        self.clear_dashboard()
        self.load_settings()
        return
    
    def clear_dashboard(self):
        for i in reversed(range(self.tabs.count()-1)):
            self.tabs.childAt(i).deleteLater()

        self.profile_menu.clear()
        return

    def load_settings(self):
        self.home = home.home_page(self)

        self.set_profile = QAction("Select Profile", self)
        self.set_profile.triggered.connect(self.log_in)
        self.clear_profile = QAction("Sign Out", self)
        self.clear_profile.triggered.connect(self.log_out)

        self.profile_menu.addSeparator()
        self.profile_menu.addAction(self.set_profile)
        if self.profile_selection != None:
            self.profile_menu.addAction(self.clear_profile)

        self.tabs.addTab(self.home, "Home")

        return

def main():

    star = QApplication(sys.argv)

    window = dashboard()
    window.show()

    star.exec()
    return

main()