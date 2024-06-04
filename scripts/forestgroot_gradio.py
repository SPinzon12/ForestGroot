import gradio as gr
import PIL.Image as Image
from ultralytics import YOLO
import os

# Obtener la lista de modelos disponibles en la carpeta "models"
model_dir = "../models"
model_files = [f for f in os.listdir(model_dir) if f.endswith(".pt")]

# Función para cargar el modelo seleccionado
def load_model(model_name):
    return YOLO(os.path.join(model_dir, model_name))

# Cargar el modelo predeterminado
model = load_model(model_files[0])

js = """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';

    var text = 'Bienvenido a Kowalsky Labs';
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 250);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}
"""

# Función de predicción de imagen
def predict_image(model_name, img, conf_threshold, iou_threshold):
    global model
    model = load_model(model_name)
    
    results = model.predict(
        source=img,
        conf=conf_threshold,
        iou=iou_threshold,
        show_labels=True,
        show_conf=True,
        imgsz=640,
    )

    for r in results:
        im_array = r.plot()
        im = Image.fromarray(im_array[..., ::-1])

    return im

# Interfaz de Gradio
iface = gr.Interface(
    fn=predict_image,
    inputs=[
        gr.Dropdown(choices=model_files, value=model_files[0], label="Seleccionar Modelo"),
        gr.Image(type="pil", label="Subir Imagen"),
        gr.Slider(minimum=0, maximum=1, value=0.25, label="Umbral de Confianza"),
        gr.Slider(minimum=0, maximum=1, value=0.45, label="Intersección-sobre-unión (IoU)"),
    ],
    outputs=gr.Image(type="pil", label="Resultado"),
    title="Forestgroot",
    description="Carga una imagen para detectar deforestación y otros objetos utilizando diferentes modelos YOLOv8. Ajusta los umbrales de confianza e IoU para personalizar la detección.",
    js=js,
)

if __name__ == "__main__":
    iface.launch(share=True)