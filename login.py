from PyQt5.QtWidgets import  *
from login_python import Ui_Form
from anapencere import AnapencerePage

class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform=Ui_Form()
        self.loginform.setupUi(self)
        self.anapencereac= AnapencerePage()
        self.loginform.pushButton_giris.clicked.connect(self.GirisYap)
        
    def GirisYap(self):
        kadi = self.loginform.lineEdit_kullaniciadi.text()
        sifre=self.loginform.lineEdit_sifre.text()
        if kadi == "Fatih" and sifre=="1234":
            self.hide()
            self.anapencereac.show()



