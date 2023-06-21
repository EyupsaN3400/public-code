import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Rammsteinli Calculator')
        self.setWindowIcon(QIcon("rammsettin.jpg"))
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('1. Sayı')
        self.lbl_sayi1.move(50,30)


        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('2. Sayı')
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)
#--------------------------
#            Butonlar
        self.lbl_topla = QtWidgets.QPushButton(self)
        self.lbl_topla.setText('Toplama')
        self.lbl_topla.move(150,130)
        self.lbl_topla.clicked.connect(self.hesapma)

        self.lbl_cikar = QtWidgets.QPushButton(self)
        self.lbl_cikar.setText('Cikarma')
        self.lbl_cikar.move(150,170)
        self.lbl_cikar.clicked.connect(self.hesapma)

        self.lbl_carpma = QtWidgets.QPushButton(self)
        self.lbl_carpma.setText('Carpma')
        self.lbl_carpma.move(150,210)
        self.lbl_carpma.clicked.connect(self.hesapma)

        self.lbl_bolme = QtWidgets.QPushButton(self)
        self.lbl_bolme.setText('Bolme')
        self.lbl_bolme.move(150,250)
        self.lbl_bolme.clicked.connect(self.hesapma)

        self.lbl_sonuc = QtWidgets.QPushButton(self)
        self.lbl_sonuc.setText('Sonuç: ')
        self.lbl_sonuc.move(150,290)
    
    def hesapma(self):
        sender = self.sender()
        result = 0

        if sender.text() == 'Toplama':
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender.text() == 'Cikarma':
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender.text() == 'Carpma':
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender.text() == 'Bolme':
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        
        self.lbl_sonuc.setText('Sonuç: ' + str(result))

#        if sender.text() == 'Toplama':
#            print(f'kullanıcı {sender.text()} ya tıkladı')
#        else:
#            print(f'kullanıcı {sender.text()} ye tıkladı')

        if sender.text() == 'Toplama':
            print(f'kullanıcı {sender.text()} ya tıkladı')
        else:
            print(f'kullanıcı {sender.text()} ye tıkladı')

        
#        self.lbl_sonuc.setText('sonuç: '+ str(result))



#-----------------------------
#     window show
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
app()


