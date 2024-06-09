import sys
from PyQt6.QtWidgets import QApplication,QWidget, QVBoxLayout,QHBoxLayout,QPushButton
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Menu Button")
        self.setGeometry(200, 200, 700, 400)
        box=QHBoxLayout()
        vbox=QVBoxLayout()
        btn1=QPushButton("Button1")
        btn2=QPushButton("Button2")
        btn3=QPushButton("Button3")
        btn4=QPushButton("Button4")
        box.addWidget(btn1)
        box.addWidget(btn2)
        box.addWidget(btn3)
        box.addWidget(btn4)
        # box.addSpacing(100)
        #box.addStretch(100)

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addSpacing(100)
        # self.setLayout(box)
        self.setLayout(vbox)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()






