import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget, QLabel
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class ExerciseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('App de Exercícios')
        self.setGeometry(100, 100, 800, 600)

        # Configurar o layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Adicionar a barra de pesquisa
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Digite o nome do exercício...')
        self.search_button = QPushButton('Buscar')
        self.search_button.clicked.connect(self.search)

        self.layout.addWidget(self.search_bar)
        self.layout.addWidget(self.search_button)

        # Adicionar a lista de vídeos e a área de exibição
        self.video_list = QListWidget()
        self.video_list.itemClicked.connect(self.play_video)
        self.layout.addWidget(self.video_list)

        self.video_player = QLabel('Selecione um vídeo para assistir.')
        self.layout.addWidget(self.video_player)

        # Lista de vídeos de exemplo (músculo -> URL do Instagram)
        self.videos = {
            'biceps': '', # Substitua XXXXXX pelo ID do post do Instagram
            'triceps': 'https://www.instagram.com/reel/C8Nn2exP5yv/?igsh=ZjBuZHpzdTJ2M2Nw', # Substitua YYYYYY pelo ID do post do Instagram
            'peito': 'https://www.instagram.com/p/ZZZZZZ/', # Substitua ZZZZZZ pelo ID do post do Instagram
        }