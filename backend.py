import os
from pca_module import apply_pca
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal


class PCAWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(object, object, object)

    def __init__(self, image_array, new_resolution):
        super().__init__()
        self.image_array = image_array
        self.new_resolution = new_resolution

    def run(self):
        # Simular progresso
        for i in range(1, 101):
            self.progress.emit(i)
            QThread.msleep(10)  # Simula processamento

        # Aplicar PCA
        compressed_image, original_shape, compressed_shape = apply_pca(self.image_array, self.new_resolution)
        self.finished.emit(compressed_image, original_shape, compressed_shape)


class ImagePCAProcessor:
    def __init__(self, ui):
        self.ui = ui
        self.worker = None

    def load_image(self):
        # Abrir um diálogo para o usuário escolher a imagem
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            None,
            "Selecione uma Imagem",
            "",
            "Imagens (*.png *.jpg *.jpeg)",
            options=options
        )
        if file_name:
            self.ui.image_path.setText(file_name)
            pixmap = QPixmap(file_name)
            self.ui.image_label.setPixmap(pixmap)
            self.ui.image_label.setScaledContents(True)
            self.ui.image_label.setFixedSize(300, 300)

            # Obter dimensões e resolução original
            img = Image.open(file_name)
            img_array = np.array(img)
            width, height = img.size
            dpi = img.info.get('dpi', (72, 72))[0]  # Pega DPI horizontal ou 72 padrão

            self.ui.dimensions_label.setText(f"Dimensões Originais: {width}x{height}")
            self.ui.resolution_label.setText(f"Resolução Original: {dpi} DPI")

    def apply_pca_to_image(self):
        # Ler a nova resolução inserida
        try:
            new_resolution = int(self.ui.resolution_input.text())
        except ValueError:
            QMessageBox.warning(self.ui, "Entrada Inválida", "Por favor, insira uma resolução válida.")
            return

        # Carregar a imagem e converter para array numpy
        img_path = self.ui.image_path.text()
        if not img_path:
            QMessageBox.warning(self.ui, "Nenhuma Imagem", "Por favor, carregue uma imagem primeiro.")
            return

        img = Image.open(img_path)
        img_array = np.array(img)
        width, height = img.size

        # Verificar se a resolução inserida é menor que a original
        if new_resolution >= width or new_resolution >= height:
            QMessageBox.warning(
                self.ui,
                "Resolução Inválida",
                f"A resolução deve ser menor que {width}x{height}."
            )
            return

        # Desabilitar botões durante o processamento
        self.ui.apply_button.setEnabled(False)
        self.ui.load_button.setEnabled(False)

        # Iniciar o worker para processar PCA
        self.worker = PCAWorker(img_array, new_resolution)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.pca_finished)
        self.worker.start()

    def update_progress(self, value):
        self.ui.progress_bar.setValue(value)

    def pca_finished(self, compressed_image, original_shape, compressed_shape):
        # Atualizar a interface com os resultados
        self.ui.compressed_dim_label.setText(f"Dimensões Comprimidas: {compressed_shape}")

        # Salvar a imagem comprimida no diretório "outputs"
        output_dir = "outputs"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_path = os.path.join(output_dir, "compressed_image.png")
        compressed_image_pil = Image.fromarray(compressed_image.astype('uint8'))
        compressed_image_pil.save(output_path)

        # Mostrar a imagem comprimida na interface
        pixmap = QPixmap(output_path)
        self.ui.compressed_image_label.setPixmap(pixmap)
        self.ui.compressed_image_label.setScaledContents(True)
        self.ui.compressed_image_label.setFixedSize(300, 300)

        # Resetar barra de progresso
        self.ui.progress_bar.setValue(0)

        # Reabilitar botões
        self.ui.apply_button.setEnabled(True)
        self.ui.load_button.setEnabled(True)
