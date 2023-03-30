from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
)

class alert_dialogue(QDialog):
    def __init__(self, title: str, message: str):
        super().__init__()

        self.setWindowTitle(title)

        buttons = QDialogButtonBox(self)
        buttons.addButton("Ok", QDialogButtonBox.AcceptRole)
        buttons.accepted.connect(self.window_close)

        self.layout = QVBoxLayout()
        response = QLabel(message)
        self.layout.addWidget(response)
        self.layout.addWidget(buttons)
        self.setLayout(self.layout)
    
    def window_close(self):
        self.close()
