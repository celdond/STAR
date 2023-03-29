import sys
import source.gui.random_selection as random_selection
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
        self._generate_UI()

    def _generate_UI(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.setCentralWidget(self.tabs)
        self.profile_selection = profile.profile_window(self)

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
        self.profile_selection = None
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
        if self.profile_selection is None:
            self.profile_menu.addAction(self.clear_profile)

        self.tabs.addTab(self.random, "Random")

        return

def main():

    star = QApplication(sys.argv)

    window = dashboard()
    window.show()

    star.exec()
    return

main()