from PyQt5.QtWidgets import QApplication
from radio import radiopage

app=QApplication([])

pencere=radiopage()
pencere.show()
app.exec_()