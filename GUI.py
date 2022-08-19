import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class sign_in_window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STAR")

        sign_in_button = QPushButton("Sign In")

        self.setCentralWidget(sign_in_button)

star = QApplication(sys.argv)

window = sign_in_window()
window.show()

star.exec()