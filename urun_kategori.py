from PyQt5.QtWidgets import  *
from urun_kategori_python import Ui_Form
class urunkategoriPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.kategoriform=Ui_Form()
        self.kategoriform.setupUi(self)
        