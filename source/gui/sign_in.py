import source.userbase as userbase
from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QGridLayout,
    QLineEdit,
    QLabel,
)

class sign_in_window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STAR")

        sign_in_button = QPushButton("Sign In")
        sign_in_button.clicked.connect(self.check_sign_in)
        profile_button = QPushButton("Create Profile")
        profile_button.clicked.connect(self.create_profile)
        self.entered_username = QLineEdit()
        self.entered_password = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(QLabel("Username"), 0, 0)
        layout.addWidget(QLabel("Password"), 1, 0)
        layout.addWidget(self.entered_username, 0, 1)
        layout.addWidget(self.entered_password, 1, 1)
        layout.addWidget(sign_in_button, 2, 1)
        layout.addWidget(profile_button, 2, 0)

        page = QWidget()
        page.setLayout(layout)
        self.setCentralWidget(page)

    def check_sign_in(self):
        if userbase.fetch_profile(self.entered_username.text(), self.entered_password.text()) == '/0':
            fail_dialogue = dialogues.sign_in_failure_dialogue("Failure", "Username or password is incorrect.")
            fail_dialogue.exec()
            return
        self.close()

    def create_profile(self):
        if '/' in self.entered_username.text():
            print(self.entered_username.text())
            illegal_dialogue = dialogues.sign_in_failure_dialogue("Failure", "Character '/' is not allowed.")
            illegal_dialogue.exec()
            return
        taken = userbase.build_user(self.entered_username.text(), self.entered_password.text())

        if taken == '/0':
            fail_dialogue = dialogues.sign_in_failure_dialogue("Username taken.")
            fail_dialogue.exec()
            return
        
        legal_dialogue = dialogues.sign_in_failure_dialogue("Profile Created", "Profile Successfully Created!")
        legal_dialogue.exec()
        return