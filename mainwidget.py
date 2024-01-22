from PySide6.QtWidgets import QWidget
from ui_mainwidget import Ui_MainWidget

class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)