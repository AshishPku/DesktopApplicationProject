from PyQt6.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton
import sys
i=0
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Potentiostat Measuring Device")
        self.setGeometry(100, 100, 600, 400) #x,y,width,height
        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(250, 150, 100, 50)
        self.button.clicked.connect(self.on_button_click)
        self.i=0
    def on_button_click(self):
        backgroundColor = ["red", "blue", "yellow","pink"]
        self.setStyleSheet(f"background-color:{backgroundColor[self.i]}")
        self.i=(self.i+1)%4
app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec())