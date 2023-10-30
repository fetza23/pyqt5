from PyQt5.QtWidgets import  *
from anapencere_python import Ui_MainWindow
from urun_kategori import urunkategoriPage
from urunlistele import urunlistePage
class AnapencerePage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.anapencereform=Ui_MainWindow()
        self.anapencereform.setupUi(self)
        self.urunlisteform=urunlistePage()
        self.kategoriformu= urunkategoriPage()
        self.anapencereform.urunlistele.triggered.connect(self.urunlist)
        self.anapencereform.kategoriEkle.triggered.connect(self.urunkategori)
    def urunlist(self):
        self.urunlisteform.show()
    def urunkategori(self):
        self.kategoriformu.show()
    

        


        

    