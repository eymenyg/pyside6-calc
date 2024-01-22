from PySide6.QtWidgets import QApplication
from mainwidget import MainWidget

app = QApplication()

widget = MainWidget()
widget.show()

app.exec()