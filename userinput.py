import sys
from PyQt6.QtWidgets import QApplication, QMainWindow,QLineEdit
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Menu Button")
        self.setGeometry(200, 200, 700, 400)
        
        inputUser=QLineEdit(self)
        # inputUser.setText("Hare Krishna")
        inputUser.setFont(QFont("Sanserif",20))
        # inputUser.setEnabled(False)
        inputUser.setPlaceholderText("Enter your name")
        # inputUser.setEchoMode(QLineEdit.EchoMode.Password)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()






