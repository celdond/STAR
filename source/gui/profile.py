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
        select_button = QPushButton("Select Profile")
        ## sign_in_button.clicked.connect(self.check_sign_in)
        create_button = QPushButton("Create Profile")

        layout = QGridLayout()
        layout.addWidget(select_button, 1, 0)
        layout.addWidget(create_button, 1, 1)

        self.setLayout(layout)