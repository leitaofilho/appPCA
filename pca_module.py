from sklearn.decomposition import PCA
import numpy as np
from PIL import Image


def apply_pca(image_array, new_resolution):
    """
    Aplica PCA a uma imagem e retorna a imagem comprimida com a nova resolução.

    Parameters:
    - image_array: np.ndarray da imagem original.
    - new_resolution: Resolução desejada (lado menor da imagem comprimida).

    Returns:
    - compressed_image: A imagem comprimida após o PCA.
    - original_shape: Forma original da imagem.
    - compressed_shape: Forma da imagem comprimida.
    """
    original_shape = image_array.shape

    # Redimensionar a imagem com base na nova resolução
    height, width, _ = original_shape
    if height > width:
        new_width = new_resolution
        new_height = int(new_resolution * height / width)
    else:
        new_height = new_resolution
        new_width = int(new_resolution * width / height)

    # Flatten a imagem para aplicar PCA
    flat_image = image_array.reshape(-1, original_shape[-1])  # Dimensões (pixels, canais de cor)

    # O número de componentes não pode ser maior que o número de características ou amostras
    n_components = min(new_resolution, min(flat_image.shape))

    # Aplicar PCA
    pca = PCA(n_components=n_components)
    compressed_image = pca.fit_transform(flat_image)

    # Reverter a forma comprimida
    compressed_image = pca.inverse_transform(compressed_image)

    # Converter a imagem comprimida de volta para formato de imagem
    compressed_image = compressed_image.reshape(original_shape)

    # Redimensionar a imagem final com PIL
    compressed_image_pil = Image.fromarray(compressed_image.astype('uint8'))
    compressed_image_pil = compressed_image_pil.resize((new_width, new_height), Image.Resampling.LANCZOS)

    compressed_shape = (new_height, new_width, original_shape[-1])
    return np.array(compressed_image_pil), original_shape, compressed_shape
