from PIL import Image

def add_margin_to_icon(input_path, output_path, margin=3):
    # Abrir la imagen original
    original_icon = Image.open(input_path)
    
    # Calcular las nuevas dimensiones con el margen
    new_width = original_icon.width + 2 * margin
    new_height = original_icon.height + 2 * margin
    
    # Crear una nueva imagen con fondo transparente
    new_icon = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))
    
    # Pegar el icono original en el centro de la nueva imagen
    new_icon.paste(original_icon, (margin, margin))
    
    # Guardar la nueva imagen
    new_icon.save(output_path)

# Lista de tus iconos
icon_paths = [
    ("offline.png", "./modified/offline.png"),
    ("headset.png", "./modified/headset.png"),
    ("battery-00.png", "./modified/battery-00.png"),
    ("battery-20.png", "./modified/battery-20.png"),
    ("battery-40.png", "./modified/battery-40.png"),
    ("battery-60.png", "./modified/battery-60.png"),
    ("battery-80.png", "./modified/battery-80.png"),
    ("battery-100.png", "./modified/battery-100.png"),
]

# Aplicar la función a cada icono
for original, modified in icon_paths:
    add_margin_to_icon(original, modified)
