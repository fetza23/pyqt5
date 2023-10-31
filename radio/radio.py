
from PyQt5.QtWidgets import *
from radio_python import Ui_Form

class radiopage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.radioform=Ui_Form()
        self.radioform.setupUi(self)
