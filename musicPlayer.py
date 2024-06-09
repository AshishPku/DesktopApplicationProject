import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Music Player")
        self.setGeometry(100, 100, 300, 200)

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        # Create a QPushButton
        self.play_button = QPushButton("Play Music")
        self.play_button.clicked.connect(self.play_music)
        self.play_button.setFont(QFont("Times",14,QFont.Weight.ExtraBold))
        layout.addWidget(self.play_button)
 
        # Create a QWidget and set it as the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Create a QMediaPlayer
        self.player = QMediaPlayer()

        # Create a QAudioOutput
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # Set the media source (you can replace the URL with your local file path)
        self.player.setSource(QUrl.fromLocalFile("/home/ashish/Music/music1.mp3"))

    def play_music(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
            self.play_button.setText("Play Music")
        else:
            self.player.play()
            self.play_button.setText("Pause Music")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()






