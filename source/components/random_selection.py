import source.database as database
import source.scripts.webscrapers as scrapers
import threading
import source.scripts.random_methods as r_m
from PySide6.QtCore import (
    Qt,
    QAbstractTableModel,
)
from PySide6.QtWidgets import (
    QPushButton,
    QTabWidget,
    QWidget,
    QGridLayout,
    QLineEdit,
    QCheckBox,
    QTableView,
)

class random_page(QWidget):

    def __init__(self, dashboard_status):
        super().__init__()
        self.dashboard_status = dashboard_status

        rand_button = QPushButton("Random")
        rand_button.clicked.connect(self.random_button_thread)

        self.platforms = platform_selection()

        layout = QGridLayout()

        layout.addWidget(rand_button, 0, 1)
        layout.addWidget(self.platforms, 0, 2)

        self.setLayout(layout)

    def random_button_thread(self):
        button_thread = threading.Thread(target = self.random_button)
        button_thread.start()
        return

    def random_button(self):
        steam_state = self.platforms.steam_check.isChecked()
        shuffle_list = list()
        if steam_state:
            steam_conn = database.check_setting(self.path, "user", "steam")
            scrapers.steam_scrape( self.user_database, steam_conn)
            shuffle_list.append('steam')
        print(r_m.random_function(self.user_database, shuffle_list))
        return

class steam_wishlist_page(QWidget):

    def __init__(self, path: str, user: str):
        super().__init__()

        data = database.load_database_external(path, user, 'steam')
        self.pandas_model = wishlist_view(data)
        table = QTableView()
        table.setModel(self.pandas_model)
        layout = QGridLayout()
        layout.addWidget(table, 0, 0)

        self.setLayout(layout)

class platform_selection(QWidget):

    def __init__(self):
        super().__init__()

        self.steam_check = QCheckBox("Steam")
        self.steam_check.setCheckState(Qt.Unchecked)

        self.gog_check = QCheckBox("GOG")
        self.gog_check.setCheckState(Qt.Unchecked)

        layout = QGridLayout()
        layout.addWidget(self.steam_check, 0, 0)
        layout.addWidget(self.gog_check, 1, 0)

        self.setLayout(layout)

class stats_page(QWidget):

    def __init__(self):
        super().__init__()

class wishlist_view(QAbstractTableModel):

    def __init__(self, data, parent = None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent = None):
        return self._data.shape[0]
        
    def columnCount(self, parent = None):
        return self._data.shape[1]

    def data(self, index, role = Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
