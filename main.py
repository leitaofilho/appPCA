import sys
from PyQt5.QtWidgets import QApplication
from ui_module import PCAImageAppUI
from backend import ImagePCAProcessor


def main():
    app = QApplication(sys.argv)

    # Inicializar interface e lógica de negócios
    ui = PCAImageAppUI()
    processor = ImagePCAProcessor(ui)

    # Conectar botões à lógica de negócios
    ui.load_button.clicked.connect(processor.load_image)
    ui.apply_button.clicked.connect(processor.apply_pca_to_image)

    # Mostrar interface
    ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
