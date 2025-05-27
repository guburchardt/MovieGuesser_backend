from PIL import Image, ImageFilter
import io
import base64

def apply_blur(image_data: bytes, blur_level: int) -> str:
    """
    Aplica um efeito de blur na imagem.
    
    Args:
        image_data (bytes): Dados da imagem em bytes
        blur_level (int): Nível de blur (1-4)
    
    Returns:
        str: Imagem em base64 com blur aplicado
    """
    # Converte os bytes para uma imagem PIL
    image = Image.open(io.BytesIO(image_data))
    
    # Aplica o blur baseado no nível
    if blur_level == 1:
        image = image.filter(ImageFilter.GaussianBlur(radius=15))
    elif blur_level == 2:
        image = image.filter(ImageFilter.GaussianBlur(radius=10))
    elif blur_level == 3:
        image = image.filter(ImageFilter.GaussianBlur(radius=5))
    elif blur_level == 4:
        image = image.filter(ImageFilter.GaussianBlur(radius=2))
    
    # Converte a imagem de volta para bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Converte para base64
    return base64.b64encode(img_byte_arr).decode() 