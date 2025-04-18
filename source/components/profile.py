import source.database as database
import source.components.dialogues as dialogues
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

        profile_button = QPushButton("Create Profile")
        profile_button.clicked.connect(self.create)
        sign_in_button = QPushButton("Sign In")
        sign_in_button.clicked.connect(self.check_sign_in)
        self.entered_username = QLineEdit()
        self.entered_password = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(QLabel("Username"), 0, 0)
        layout.addWidget(QLabel("Password"), 1, 0)
        layout.addWidget(self.entered_username, 0, 1)
        layout.addWidget(self.entered_password, 1, 1)
        layout.addWidget(profile_button, 2, 0)
        layout.addWidget(sign_in_button, 2, 1)

        self.setLayout(layout)

    def create(self):
        if '/' in self.entered_username.text():
            illegal_dialogue = dialogues.alert_dialogue("Failure", "Character '/' is not allowed.")
            illegal_dialogue.exec()
            return
        taken = database.build_user(self.entered_username.text(), self.entered_password.text())

        if taken == '/0':
            fail_dialogue = dialogues.alert_dialogue("Failure", "Name taken.")
            fail_dialogue.exec()
            return
        
        legal_dialogue = dialogues.alert_dialogue("Profile Created", "Profile Successfully Created!")
        legal_dialogue.exec()
        self.dashboard_status.current_profile = taken
        self.dashboard_status.profile_change()
        self.hide()
        return
    
    def check_sign_in(self):
        user = database.fetch_profile(self.entered_username.text(), self.entered_password.text())
        if user == '/0':
            fail_dialogue = dialogues.alert_dialogue("Failure", "Username or password is incorrect.")
            fail_dialogue.exec()
            return
        self.dashboard_status.current_profile = user
        self.dashboard_status.profile_change()
        self.hide()
        return