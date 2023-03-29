from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QGridLayout,
    QLineEdit,
    QLabel,
)

class platforms_window(QWidget):

    def __init__(self, dashboard_status):
        super().__init__()
        self.dashboard_status = dashboard_status