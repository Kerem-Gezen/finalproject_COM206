import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtGui import QFont, QIntValidator
from PySide6.QtCore import Qt

class DijitalKumbara(QWidget):
    def __init__(self):
        super().__init__()

        
        self.toplam_bakiye = 0

       
        self.setWindowTitle("Dijital Kumbara")
        self.resize(380, 250)
        self.setStyleSheet("background-color: #1e1e2e; color: #cdd6f4;") 

       

        
        self.lbl_bakiye = QLabel("0 TL", self)
        self.lbl_bakiye.setFont(QFont("Arial", 28, QFont.Bold))
        self.lbl_bakiye.setAlignment(Qt.AlignCenter)
        self.lbl_bakiye.setStyleSheet("color: #a6e3a1; margin-bottom: 20px;") # Yeşil renk bakiye

        
        self.input_miktar = QLineEdit(self)
        self.input_miktar.setPlaceholderText("Miktar girin...")
        self.input_miktar.setFont(QFont("Arial", 14))
        self.input_miktar.setStyleSheet("padding: 8px; background-color: #313244; border: 1px solid #45475a; border-radius: 6px;")

       
        self.input_miktar.setValidator(QIntValidator(1, 999999, self))

        
        self.btn_para_at = QPushButton("Para At 💰", self)
        self.btn_para_at.setFont(QFont("Arial", 12, QFont.Bold))
        self.btn_para_at.setStyleSheet("padding: 10px; background-color: #fab387; color: #11111b; border-radius: 6px;")

        
        self.btn_para_al = QPushButton("Para Al 💸", self)
        self.btn_para_al.setFont(QFont("Arial", 12, QFont.Bold))
        self.btn_para_al.setStyleSheet("padding: 10px; background-color: #f38ba8; color: #11111b; border-radius: 6px;") # Kırmızımtırak renk

        
        self.btn_para_at.clicked.connect(self.para_ekle)
        self.btn_para_al.clicked.connect(self.para_al) 
        self.input_miktar.returnPressed.connect(self.para_ekle)

       
        buton_yerlesimi = QHBoxLayout()
        buton_yerlesimi.addWidget(self.btn_para_at)
        buton_yerlesimi.addWidget(self.btn_para_al)
        buton_yerlesimi.setSpacing(10)

       
        ana_yerlesim = QVBoxLayout()
        ana_yerlesim.addWidget(self.lbl_bakiye)
        ana_yerlesim.addWidget(self.input_miktar)
        ana_yerlesim.addLayout(buton_yerlesimi) 
        ana_yerlesim.setContentsMargins(30, 30, 30, 30)
        ana_yerlesim.setSpacing(15)

        self.setLayout(ana_yerlesim)

    
    def para_ekle(self):
        girilen_metin = self.input_miktar.text()

        if girilen_metin:
            eklenecek_para = int(girilen_metin)
            self.toplam_bakiye += eklenecek_para
            self.lbl_bakiye.setText(f"{self.toplam_bakiye} TL")
            self.input_miktar.clear()
            self.input_miktar.setPlaceholderText("Miktar girin...") 

    
    def para_al(self):
        girilen_metin = self.input_miktar.text()

        if girilen_metin:
            alinacak_para = int(girilen_metin)

            
            if alinacak_para <= self.toplam_bakiye:
                self.toplam_bakiye -= alinacak_para
                self.lbl_bakiye.setText(f"{self.toplam_bakiye} TL")
                self.input_miktar.clear()
                self.input_miktar.setPlaceholderText("Miktar girin...")
            else:
               
                self.input_miktar.clear()
                self.input_miktar.setPlaceholderText("Bakiye yetersiz!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    kumbara = DijitalKumbara()
    kumbara.show()
    sys.exit(app.exec())
