import source.userbase as userbase
import source.gui.dialogues as dialogues
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

        profile_button = QPushButton("Create Profile")
        profile_button.clicked.connect(self.create)
        self.entered_username = QLineEdit()
        self.entered_password = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(QLabel("Username"), 0, 0)
        layout.addWidget(QLabel("Password"), 1, 0)
        layout.addWidget(self.entered_username, 0, 1)
        layout.addWidget(self.entered_password, 1, 1)
        layout.addWidget(profile_button, 2, 0)

        self.setLayout(layout)

    def create(self):
        if '/' in self.entered_username.text():
            illegal_dialogue = dialogues.sign_in_failure_dialogue("Failure", "Character '/' is not allowed.")
            illegal_dialogue.exec()
            return
        taken = userbase.build_user(self.entered_username.text(), self.entered_password.text())

        if taken == '/0':
            fail_dialogue = dialogues.sign_in_failure_dialogue("Name taken.")
            fail_dialogue.exec()
            return
        
        legal_dialogue = dialogues.sign_in_failure_dialogue("Profile Created", "Profile Successfully Created!")
        legal_dialogue.exec()
        return