from PyQt5.QtWidgets import *
from urun_liste_python import Ui_Form
class urunlistePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.urunlisteform= Ui_Form()
        self.urunlisteform.setupUi(self)
        

