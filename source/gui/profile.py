import source.userbase as userbase
from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QGridLayout,
    QLineEdit,
    QLabel,
)


class profile_window(QWidget):
    
    def __init__(self, dashboard_status):
        super().__init__()
        self.dashboard_status = dashboard_status
        self.setWindowTitle("Profile Selection")
        select_button = QPushButton("Select Profile")
        create_button = QPushButton("Create Profile")
        create_button.clicked.connect(self.open_create_window)

        layout = QGridLayout()
        layout.addWidget(select_button, 1, 0)
        layout.addWidget(create_button, 1, 1)

        self.setLayout(layout)

    def open_create_window(self):
        self.dashboard_status.creation.show()
        self.close()

class create_profile(QWidget):

    def __init__(self, dashboard_status):
        super().__init__()
        self.dashboard_status = dashboard_status