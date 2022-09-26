from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
)

class sign_in_failure_dialogue(QDialog):
    def __init__(self, message: str):
        super().__init__()

        self.setWindowTitle("Failure")

        ok_button = QDialogButtonBox.Close

        self.buttonBox = QDialogButtonBox(ok_button)

        self.layout = QVBoxLayout()
        response = QLabel(message)
        self.layout.addWidget(response)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)