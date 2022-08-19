import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class dashboard(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")

class sign_in_window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STAR")

        sign_in_button = QPushButton("Sign In")
        sign_in_button.clicked.connect(self.check_sign_in)
        self.setCentralWidget(sign_in_button)

    def check_sign_in(self, checked):
        d= dashboard()
        d.show()

star = QApplication(sys.argv)

window = sign_in_window()
window.show()

star.exec()