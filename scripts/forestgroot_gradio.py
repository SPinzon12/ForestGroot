import gradio as gr
import PIL.Image as Image
from ultralytics import YOLO
import os

# Obtener la lista de modelos disponibles en la carpeta "models"
model_dir = "./models"
modelos = [f for f in os.listdir(model_dir) if f.endswith(".pt")]

# Función para cargar el modelo seleccionado
def load_model(model_name):
    return YOLO(os.path.join(model_dir, model_name))

# Cargar el modelo predeterminado
model = load_model(modelos[0])

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

css = """

    gradio-app {
    background-color: #0b0f19 !important; 
    }

    empty.svelte-1oiin9d.large.unpadded_box {
    background-color: #0b0f19 !important;
    }

    p {
    font-size: 16px;
    padding-left: 20px;
    padding-right: 20px;
    }

    #gradio-animation {
    background-color: #53b844;
    color: #0b0f19;
    width: 700px;
    border-radius: 20px;
    }

    .gradio-container.gradio-container-5-13-2.svelte-1yb15ey.app {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 20px;
    }

    .lg.primary.svelte-5st68j {
    background-color: #53b844 !important;
    }

    .selected.svelte-1ebruwp {
    color: #53b844 !important;
    }

    .primary.svelte-cmf5ev {
    border: #53b844 !important;
    background: #53b844 !important;
    }

    .svelte-10lj3xl input[type="range"] {
    accent-color: #53b844 !important;
    background-image: #53b844 !important;
    background-color: #53b844 !important;
    }

    slider_input_container.svelte-10lj3xl {
    accent-color: #53b844 !important;
    background-image: #53b844 !important;
    background-color: #53b844 !important;
    }

    .border-none.svelte-1sk0pyu {
    background-image: #1f2937 !important;
    }

"""

# Función de predicción de imagen
def predict_image(model_name, img, conf_threshold, iou_threshold):
    global model
    model = load_model(model_name)
    print(model_name)
    
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
demo = gr.Interface(
    fn=predict_image,
    inputs=[
        gr.Dropdown(choices=modelos, value=modelos[0], label="Seleccionar Modelo"),
        gr.Image(type="pil", label="Subir Imagen"),
        gr.Slider(minimum=0, maximum=1, value=0.25, label="Umbral de Confianza"),
        gr.Slider(minimum=0, maximum=1, value=0.45, label="Intersección-sobre-unión (IoU)"),
    ],
    outputs=gr.Image(type="pil", label="Resultado"),
    title=" &#x1F332 Forestgroot - Detección de Areas con Indices de Deforestación",
    description="Selecciona el modelo de tu preferencia, carga una imagen para detectar deforestación y otros objetos utilizando diferentes modelos YOLOv8. Ajusta los umbrales de confianza e IoU para personalizar la detección.",
    js=js,
    css=css,
)

if __name__ == "__main__":
    demo.launch(share=True)