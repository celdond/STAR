from PySide6.QtWidgets import (
    QComboBox,
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
        self.platform = None
        platform_selection = QComboBox()
        platform_selection.addItems(["None", "Steam"])

        platform_selection.currentTextChanged.connect(self.platform_changed)

        layout = QGridLayout()
        layout.addWidget(platform_selection, 0, 0)
        self.setLayout(layout)

    def platform_change(self, s):
        self.platform = s
        return