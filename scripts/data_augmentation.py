import Augmentor

# Definir las clases junto con la ruta de la carpeta que contiene las imágenes y la cantidad de imágenes en cada clase
classes = [{
    'class': 'urban',
    'path': 'Urban',
    'quantity': 245
}, {
    'class': 'fire',
    'path': 'Fire',
    'quantity': 85
}, {
    'class': 'water',
    'path': 'Water',
    'quantity': 100
}]
           
# Iterar sobre cada clase y aplicar aumentos de datos
for class_info in classes:
    print("Processing class:", class_info['class'])
    p = Augmentor.Pipeline(class_info['path'])
    p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    p.rotate90(probability=0.5)
    p.rotate270(probability=0.5)
    p.flip_left_right(probability=0.8)
    p.flip_top_bottom(probability=0.3)
    p.crop_random(probability=1, percentage_area=0.9)
    p.resize(probability=1.0, width=640, height=640)
    p.sample(class_info['quantity'])  # Generar la cantidad específica de muestras para cada clase


