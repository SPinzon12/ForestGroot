# forestGroot - Detección y segmentación de Areas con indices de deforestación
##### _Elaborado Por: Juan Camilo Vargas - Sebastian Diaz - Samuel Pinzón_

## Escenario
La deforestación ilegal representa uno de los más grandes desafíos en Colombia, con consecuencias bastante perjudiciales para el medio ambiente, la economía y los ciudadanos. Esta práctica indebida va desde la tala de árboles hasta la conversión de bosques en tierras agrícolas, arraigándose en diversas regiones del país y siendo alimentada principalmente por la ausencia de una supervisión y regulación efectiva. Como consecuencia de esta problemática surge la necesidad de buscar soluciones innovadoras y eficaces que sean capaces de combatir la deforestación ilegal. En este contexto, los avances tecnológicos, principalmente en el campo de la inteligencia artificial, buscan ofrecer una herramienta para abordar este desafío.

El objetivo principal de este proyecto se basa en desarrollar un sistema de detección automatizada de areas con indices de deforestación, especialmente en imágenes aéreas. Como resultado, este sistema podría ayudar a las autoridades, organizaciones ambientales y ONG's a identificar las actividades de tala ilegal, aportando a la conservación del medio ambiente y la protección de los bosques amazonicos.

## Dataset
Para la selección del conjunto de datos, se buscaron principalmente datasets con imágenes aéreas. Sin embargo, debido a la falta de disponibilidad de un dataset adecuado, nos vimos en la tarea de crear nuestro propio conjunto de datos utilizando imágenes obtenidas de Google Earth. En este proceso, se priorizó la obtención de imágenes que mostraran índices de deforestación en los alrededores del área amazónica, con un enfoque particular en Colombia. Para la recolección de las imágenes, se tuvo en cuenta el criterio de los profesores, quienes recomendaron capturar imágenes no solo de áreas deforestadas, sino también otras areas de interez con el fin de realizar un buen trabajo en términos de segmentación de objetos, las clases resultados fueron:

- deforestation - Areas Deforestadas
- urban - Areas Urbanas
- fire - Incendios Forestales
- water - Cuerpos de Agua

El resultado fue un dataset de 400 imágenes en total, 100 por cada clase, las cuales tenían características específicas como una resolución fija de 640x640 píxeles, y cada imagen fue tomada aproximadamente a 700 metros de altura, de acuerdo a Google Earth.
