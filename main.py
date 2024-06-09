from PyQt6.QtWidgets import QApplication,QLabel,QWidget
from PyQt6.QtGui import QIcon,QFont,QPixmap,QMovie
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,1000,800)
        # self.showMaximized()
        self.setWindowTitle("Potentiostat Measuring Device")
        self.setWindowTitle("Potentiostat Measuring Device")
        self.setStyleSheet('background-color:black')
        
        '''
        label=QLabel("GUI for potentiostat",self)
        label.setText("Text got changed!")
        label.move(100,0) #move(X,Y)
        label.setFont(QFont("sanserif",30))
        label.setStyleSheet("color:green")
        # label.setText(str(4232))
        label.setNum(708)
        label.clear()
        '''
        label=QLabel(self)
        # label.setPixmap(QPixmap('icon.png'))
        movie=QMovie('tensor.gif')
        label.setMovie(movie)
        movie.start()






app = QApplication(sys.argv)
w = Window()
w.show()
sys.exit(app.exec())