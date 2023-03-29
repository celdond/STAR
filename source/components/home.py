import source.database as database
import source.scripts.webscrapers as scrapers
import threading
from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QGridLayout,
)

class home_page(QWidget):

    def __init__(self, dashboard_status):
        super().__init__()
        self.dashboard_status = dashboard_status
        add_button = QPushButton("Add Platform")
        add_button.clicked.connect(self.add_button)

        layout = QGridLayout()
        layout.addWidget(add_button, 0, 1)

        self.setLayout(layout)

    def add_button(self):
        database.change_setting(self.path, "user", "steam", self.wishlist_name.text())
        self.dashboard_status.add_steam_tab()
        return