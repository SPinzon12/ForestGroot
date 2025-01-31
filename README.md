# Detección y segmentación de areas con indices de deforestación
##### _Elaborado Por: Juan Camilo Vargas - Sebastian Diaz - Samuel Pinzón_

## Escenario
La deforestación ilegal representa uno de los más grandes desafíos en Colombia, con consecuencias bastante perjudiciales para el medio ambiente, la economía y los ciudadanos. Esta práctica indebida va desde la tala de árboles hasta la conversión de bosques en tierras agrícolas, arraigándose en diversas regiones del país y siendo alimentada principalmente por la ausencia de una supervisión y regulación efectiva. Como consecuencia de esta problemática surge la necesidad de buscar soluciones innovadoras y eficaces que sean capaces de combatir la deforestación ilegal. En este contexto, los avances tecnológicos, principalmente en el campo de la inteligencia artificial, buscan ofrecer una herramienta para abordar este desafío.

El objetivo principal de este proyecto se basa en desarrollar un sistema de detección basado en algoritmos de deep learning, como redes neuronales convolucionales, para la identificación de áreas con índices de deforestación, especialmente en imágenes aéreas. Como resultado, este sistema podría ayudar a las autoridades, organizaciones ambientales y ONG's a identificar las actividades de tala ilegal, aportando a la conservación del medio ambiente y la protección de los bosques amazónicos.

## Dataset
Para la selección del conjunto de datos, se buscaron principalmente datasets con imágenes aéreas. Sin embargo, debido a la falta de disponibilidad de un dataset adecuado, nos vimos en la tarea de crear nuestro propio conjunto de datos utilizando imágenes obtenidas de Google Earth. En este proceso, se priorizó la obtención de imágenes que mostraran índices de deforestación en los alrededores del área amazónica, con un enfoque particular en Colombia. Para la recolección de las imágenes, se tuvo en cuenta el criterio de los profesores, quienes recomendaron capturar imágenes no solo de áreas deforestadas, sino también otras areas de interez con el fin de realizar un buen trabajo en términos de segmentación de objetos, las clases resultados fueron:

<div align="center">
   
   | Clase  | Descripción |
   | ------------- | ------------- |
   | deforestation | Áreas donde con indices de deforestación |
   | urban | Áreas urbanas y rurales |
   | fire | Áreas con indices de incendios forestales |
   | water | Áreas con cuerpos de agua (rios, lagos, etc) |
   
</div>
<br>

El resultado fue un dataset de 400 imágenes en total, un aproximado de 100 imágenes por clase. Pese a esto y a la posibilidad de que existieran más de una instancia por imagen, se creó un desbalance entre las clases. Por tal motivo, se decidió balancear el número de instancias añadiendo más imágenes a la clase con menos instancias mediante un data augmentation en código `/scripts/data_augmentation.py`, terminando con un total de 830 imágenes. El motivo del desbalance en la captura de las imágenes se debe al número de instancias por imagen que hay, siendo una instancia un objeto dentro de la imagen, la cual puede tener más de una instancia. Las imágenes tenían características específicas como una resolución fija de 640x640 píxeles, y cada imagen fue tomada aproximadamente a 700 metros de altura, de acuerdo a Google Earth.

![image](https://github.com/SPinzon12/forestGroot/assets/99686755/7ff13bc2-bc72-4ec2-af1e-420f60edeabd)


Después, en Roboflow, se llevó a cabo un proceso adicional de data augmentation con el fin de aumentar aún más el número de datos balanceados para el entrenamiento. Esta etapa de aumento de datos permitió diversificar la variabilidad en el conjunto de datos, introduciendo modificaciones como rotaciones, traslaciones, entre otros. Este enfoque de expansión de datos garantizó una mayor robustez del modelo durante el entrenamiento y una mejor capacidad para generalizar patrones en datos nuevos y no vistos. Como resultado de este proceso, el dataset final alcanzó un total de 1992 imágenes, proporcionando una base sólida y rica en variedad para el desarrollo y la evaluación del modelo.

<div align="center">
   
   | Imagen Original  | Imagen Segmentada |
   | ------------- | ------------- |
   | <img src="https://i.postimg.cc/d0w36X0d/Captura3.jpg" alt="Perro" width="500" height="500"/> | <img src="https://i.postimg.cc/TwPwMDg3/Captura2.jpg" alt="Perro" width="500" height="500"/> |
   
</div>

## YOLO (You Only Look Once)
YOLO es un sistema de detección de objetos en imágenes o videos basado en redes neuronales convolucionales. A diferencia de otros enfoques que dividían la tarea de detección en múltiples etapas, como la selección de regiones y la clasificación, YOLO aborda el problema de detección de objetos de manera integral. En lugar de examinar la imagen varias veces a diferentes escalas y ubicaciones, YOLO realiza la detección de una sola vez (de ahí su nombre), utilizando una red neuronal convolucional para predecir simultáneamente las cajas delimitadoras y las probabilidades de clase para los objetos en la imagen.

## Entrenamiento
Para realizar el entrenamiento del modelo, puedes usar el notebook `/notebooks/train_forestgroot.ipynb`. Sigue todos los pasos en orden para su realización.

> [!IMPORTANT]
> En caso de no poseer el computo adecuado para el entrenamiento se recomienda utilizar la T4 GPU de Google Colab. Esto facilitara su ejecución al usar los recursos de la GPU del servidor y no de tu maquina.

## Setup - Instalación

### Configuración del Entorno Virtual

1. Primero, crea un entorno virtual para este proyecto. Puedes hacerlo usando `venv` de la siguiente manera:
    ```bash
    python3 -m venv myenv
    ```

2. Luego, activa el entorno virtual. La forma de hacerlo varía según tu sistema operativo:
    - En Windows:
        ```bash
        myenv\Scripts\activate
        ```
    - En macOS y Linux:
        ```bash
        source myenv/bin/activate
        ```

### Instalación de Dependencias

3. Asegúrate de que estás en el entorno virtual que acabas de activar. Luego, instala las dependencias desde el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución del Script

4. Una vez que hayas configurado el entorno virtual y tengas las dependencias instaladas, ejecuta el siguiente comando en la consola para iniciar la aplicación:
    ```bash
    python scripts/forestgroot_gradio.py
    ```

### Uso de la Aplicación

5. Después de ejecutar el comando, verás dos URLs en la terminal:
    - El primer enlace es para acceder a la aplicación Gradio de forma local.
    - El segundo enlace es para compartirlo públicamente con otros usuarios.

6. Dentro de la aplicación Gradio, a la izquierda encontrarás campos para seleccionar el modelo e ingresar la imagen a analizar. Puedes ajustar los valores de Confianza y IoU según tu preferencia.
   <div align="center">
      <img align="center" src="https://i.postimg.cc/Jzt6NhmN/Captura.jpg" alt="Perro" width="650" height="580"/>
   </div>

7. Una vez que selecciones la imagen y presiones 'Submit', comenzará el proceso de segmentación con el modelo YOLO y se mostrará una comparativa de la imagen original y la imagen segmentada.
   <div align="center">
      <img align="center" src="https://i.postimg.cc/xTQdnhKZ/Captura5.jpg" alt="Perro" width="850" height="450"/>
   </div>




