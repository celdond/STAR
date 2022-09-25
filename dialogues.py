from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
)

class sign_in_failure_dialogue(QDialog):
    def __init__(self, message: str):
        super().__init__()

        self.setWindowTitle("Failure")

        ok_button = QDialogButtonBox.Close

        self.buttonBox = QDialogButtonBox(ok_button)