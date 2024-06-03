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

El resultado fue un dataset de 830 imágenes en total, 90 de deforestación, 103 de incendios, 199 urbanas y 191 de cuerpos de agua. El motivo del desbalance en la captura de las imágenes se debe al número de instancias por imagen que hay, siendo una instancia un objeto dentro de la imagen, la cual puede tener más de una instancia. Las imágenes tenían características específicas como una resolución fija de 640x640 píxeles, y cada imagen fue tomada aproximadamente a 700 metros de altura, de acuerdo a Google Earth.

<div align="center">
   
   | Imagen original  | Imagen segmentada |
   | ------------- | ------------- |
   | <img src="https://i.postimg.cc/d0w36X0d/Captura3.jpg" alt="Perro" width="500" height="500"/> | <img src="https://i.postimg.cc/TwPwMDg3/Captura2.jpg" alt="Perro" width="500" height="500"/> |
   
</div>
<br>

## Entrenamiento
Para realizar el entrenamiento del modelo, puedes usar el notebook XXXXX. Sigue todos los pasos en orden para su realización.

> [!IMPORTANT]
> En caso de no poseer el computo adecuado para el entrenamiento se recomienda utilizar la T4 GPU de Google Colab.

## Setup - Instalación
Antes de ejecutar el codigo asegurate de tener instalados los siguientes requerimientos:
```bash
   pip install torch torchvision
   pip install ultralytics
   pip install gradio
