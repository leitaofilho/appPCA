from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QGuiApplication
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, \
    QProgressBar


class PCAImageAppUI(QWidget):
    def __init__(self):
        super().__init__()

        # Obter o tamanho da tela
        screen_geometry = QGuiApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Definir tamanho máximo da janela
        window_width = min(900, screen_width - 100)
        window_height = min(700, screen_height - 100)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setSpacing(30)  # Espaçamento global entre os elementos

        # Definindo estilo global de fonte
        font = QFont("Arial", 12)

        # Layout para imagens e seus dados - duas colunas
        image_layout = QHBoxLayout()
        image_layout.setAlignment(Qt.AlignCenter)
        image_layout.setSpacing(50)  # Espaçamento entre as colunas

        ### Coluna 1: Imagem Original e Dados ###
        column1_layout = QVBoxLayout()
        column1_layout.setAlignment(Qt.AlignTop)
        column1_layout.setSpacing(15)

        # Exibição da imagem original
        self.image_label = QLabel("Imagem Original", self)
        self.image_label.setFont(font)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 1px solid #666; background-color: #222;")
        self.image_label.setFixedSize(350, 350)  # Tamanho maior para as imagens
        column1_layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        # Exibição das dimensões da imagem original
        self.dimensions_label = QLabel("Dimensões Originais: -", self)
        self.dimensions_label.setFont(font)
        self.dimensions_label.setAlignment(Qt.AlignCenter)
        column1_layout.addWidget(self.dimensions_label)

        # Exibição da resolução original
        self.resolution_label = QLabel("Resolução Original: -", self)
        self.resolution_label.setFont(font)
        self.resolution_label.setAlignment(Qt.AlignCenter)
        column1_layout.addWidget(self.resolution_label)

        image_layout.addLayout(column1_layout)

        ### Coluna 2: Imagem Comprimida e Dados ###
        column2_layout = QVBoxLayout()
        column2_layout.setAlignment(Qt.AlignTop)
        column2_layout.setSpacing(15)

        # Exibição da imagem comprimida
        self.compressed_image_label = QLabel("Imagem Comprimida", self)
        self.compressed_image_label.setFont(font)
        self.compressed_image_label.setAlignment(Qt.AlignCenter)
        self.compressed_image_label.setStyleSheet("border: 1px solid #666; background-color: #222;")
        self.compressed_image_label.setFixedSize(350, 350)  # Tamanho maior para as imagens
        column2_layout.addWidget(self.compressed_image_label, alignment=Qt.AlignCenter)

        # Exibição das dimensões comprimidas
        self.compressed_dim_label = QLabel("Dimensões Comprimidas: -", self)
        self.compressed_dim_label.setFont(font)
        self.compressed_dim_label.setAlignment(Qt.AlignCenter)
        column2_layout.addWidget(self.compressed_dim_label)

        image_layout.addLayout(column2_layout)

        # Adicionar layout de imagens ao layout principal
        main_layout.addLayout(image_layout)

        ### Parte inferior: Controles e barra de progresso ###
        controls_layout = QVBoxLayout()
        controls_layout.setAlignment(Qt.AlignCenter)
        controls_layout.setSpacing(20)

        # Label para o caminho da imagem
        self.image_path = QLineEdit(self)
        self.image_path.setPlaceholderText("Selecione a imagem...")
        self.image_path.setReadOnly(True)
        self.image_path.setFont(font)
        self.image_path.setFixedHeight(40)
        self.image_path.setFixedWidth(400)  # Ajustar largura
        controls_layout.addWidget(self.image_path)

        # Layout horizontal para centralizar o botão "Carregar Imagem"
        load_button_layout = QHBoxLayout()
        load_button_layout.setAlignment(Qt.AlignCenter)
        self.load_button = QPushButton("Carregar Imagem")
        self.load_button.setObjectName("CarregarImagem")  # Definir o nome do objeto para o seletor de estilo
        self.load_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.load_button.setFixedHeight(40)
        self.load_button.setFixedWidth(400)
        load_button_layout.addWidget(self.load_button)
        controls_layout.addLayout(load_button_layout)

        # Caixa de entrada para resolução
        self.resolution_input = QLineEdit(self)
        self.resolution_input.setPlaceholderText("Atribua uma nova altura (em px)")
        self.resolution_input.setFont(font)
        self.resolution_input.setFixedHeight(40)
        self.resolution_input.setFixedWidth(400)
        controls_layout.addWidget(self.resolution_input)

        # Layout horizontal para centralizar o botão "Aplicar PCA"
        apply_button_layout = QHBoxLayout()
        apply_button_layout.setAlignment(Qt.AlignCenter)
        self.apply_button = QPushButton("Aplicar PCA")
        self.apply_button.setObjectName("AplicarPCA")  # Definir o nome do objeto para o seletor de estilo
        self.apply_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.apply_button.setFixedHeight(40)
        self.apply_button.setFixedWidth(400)
        apply_button_layout.addWidget(self.apply_button)
        controls_layout.addLayout(apply_button_layout)

        # Barra de progresso
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        self.progress_bar.setFixedHeight(30)
        self.progress_bar.setFixedWidth(400)
        self.progress_bar.setStyleSheet("QProgressBar { text-align: center; }")
        controls_layout.addWidget(self.progress_bar)

        # Adicionar o layout de controles ao layout principal
        main_layout.addLayout(controls_layout)

        # Definir o layout principal
        self.setLayout(main_layout)
        self.setWindowTitle('Simulação PCA para Imagens')

        # Definir a geometria da janela
        self.setGeometry(100, 100, window_width, window_height)

        # Estilo geral - Tema escuro e botões arredondados
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #333;
                color: #ffffff;
                border: 1px solid #444;
                border-radius: 5px;
                padding-left: 10px;
            }
            QPushButton {
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton#CarregarImagem {
                background-color: #555555;  /* Cor cinza para o botão Carregar Imagem */
            }
            QPushButton:hover#CarregarImagem {
                background-color: #666666;
            }
            QPushButton:pressed#CarregarImagem {
                background-color: #444444;
            }
            QPushButton#AplicarPCA {
                background-color: #007BFF;  /* Cor azul para o botão Aplicar PCA */
            }
            QPushButton:hover#AplicarPCA {
                background-color: #0056b3;
            }
            QPushButton:pressed#AplicarPCA {
                background-color: #003f7f;
            }
            QProgressBar {
                background-color: #333;
                color: white;
                border: 1px solid #555;
                border-radius: 5px;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                width: 20px;
            }
        """)
