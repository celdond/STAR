import sys
import source.gui.dash as dash
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
)

class dashboard(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        # self.path = os.path.join(os.getcwd(), "profiles", user)

        self.load_settings()

    def load_settings(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.home = dash.home_page(self)

        toolbar = dash.home_bar()
        self.addToolBar(toolbar)

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