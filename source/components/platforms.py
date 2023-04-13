import source.components.dialogues as dialogues
import source.scripts.webscrapers as webscrapers
import source.settings as settings
from PySide6.QtCore import (
    Qt,
)
from PySide6.QtWidgets import (
    QComboBox,
    QPushButton,
    QWidget,
    QGridLayout,
    QLineEdit,
    QCheckBox,
)

class platforms_window(QWidget):

    def __init__(self, dashboard_status):
        super().__init__()
        self.dashboard_status = dashboard_status
        self.platform = "None"
        platform_selection = QComboBox()
        platform_selection.addItems(["None", "Steam"])
        self.entered_path = QLineEdit()
        self.replace_platform = QCheckBox("Replace")
        self.replace_platform.setCheckState(Qt.Unchecked)
        add_button = QPushButton("Add Platform")
        add_button.clicked.connect(self.add)

        platform_selection.currentTextChanged.connect(self.platform_change)

        layout = QGridLayout()
        layout.addWidget(platform_selection, 0, 0)
        layout.addWidget(self.entered_path, 1, 0)
        layout.addWidget(self.replace_platform, 2, 0)
        layout.addWidget(add_button, 3, 0)
        self.setLayout(layout)

    def platform_change(self, s):
        self.platform = s
        return
    
    def platform_scrape(self):
        webscrapers.steam_scrape(self.dashboard_status.path, self.dashboard_status.current_profile, self.entered_path.text())
        self.dashboard_status.scraping = 0
        finished = dialogues.alert_dialogue("Finished", "Webscraping complete.")
        finished.exec()
        return

    def add(self):
        if self.platform == "None":
            platform_dialogue = dialogues.alert_dialogue("Platform Unselected", "Please select a platform to add.")
            platform_dialogue.exec()
            return
        if len(self.entered_path.text()) == 0:
            platform_dialogue = dialogues.alert_dialogue("Path Unspecified", "Please provide the path to the wishlist.")
            platform_dialogue.exec()
            return
        check_platform = settings.check_setting(self.dashboard_status.path, 'User', self.platform)
        if check_platform != '0' and self.replace_platform.checkState() == Qt.Unchecked:
            platform_dialogue = dialogues.alert_dialogue("Platform Exists", "Check Replace in form above to replace the current platform path.")
            platform_dialogue.exec()
            return
        settings.change_setting(self.dashboard_status.path, 'User', self.platform, self.entered_path.text())
        self.platform_scrape()
        self.hide()
        return