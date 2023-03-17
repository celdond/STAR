import source.userbase as userbase
from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QGridLayout,
    QLineEdit,
    QLabel,
)


class profile_window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Profile Selection")
        sign_in_button = QPushButton("Select Profile")
        ## sign_in_button.clicked.connect(self.check_sign_in)
        profile_button = QPushButton("Create Profile")