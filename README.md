# Proyecto Escape Room QR Matemático

## 1. Introducción
En la actualidad, los códigos QR (Quick Response) son herramientas fundamentales para el acceso rápido a información. Se utilizan en ámbitos como el comercio, la educación y la seguridad digital. Sin embargo, pocas veces se estudia el fundamento matemático detrás de su funcionamiento.

Este proyecto busca analizar la relación entre álgebra lineal y códigos QR, explorando cómo el uso de matrices permite codificar información y aplicar corrección de errores. Además, se desarrollará un juego educativo basado en códigos QR y problemas de álgebra lineal para mejorar la comprensión de estos conceptos de manera interactiva.

## 2. Propósito u Objetivo
El objetivo de este proyecto es desarrollar un escape room matemático basado en álgebra lineal y códigos QR. A través de una serie de desafíos, los estudiantes deberán aplicar conceptos como sistemas de ecuaciones, transformaciones lineales y matrices para avanzar en el juego.

Los objetivos específicos incluyen:

- Explicar cómo los códigos QR almacenan y procesan información usando álgebra lineal.
- Diseñar un juego de pistas interactivas con códigos QR, donde los estudiantes resuelvan problemas matemáticos para desbloquear la siguiente pista.
- Aplicar programación para generar y validar códigos QR en función de las respuestas ingresadas por los jugadores.

## 3. Descripción del Juego: Escape Room QR Matemático
El juego será un escape room matemático en el que los participantes deberán resolver una serie de problemas de álgebra lineal para avanzar de una pista a otra.

### Mecánica del juego:
#### Inicio del juego:
- Los jugadores escanearán un código QR inicial que los llevará a la primera pista (puede ser una página web, un formulario o una aplicación).
- Se les presentará un problema de álgebra lineal que deben resolver.

#### Resolución de problemas matemáticos:
Cada pista tendrá un desafío basado en álgebra lineal, como:

- Resolver un sistema de ecuaciones para encontrar coordenadas ocultas.
- Aplicar una transformación lineal (rotación, escala, reflexión) a un conjunto de puntos.
- Descomponer una matriz para revelar un código numérico.

Los jugadores ingresarán su respuesta en la plataforma o aplicación.

#### Desbloqueo de la siguiente pista:
Si la respuesta es correcta, se generará un nuevo código QR que los llevará a la siguiente pista.

Si la respuesta es incorrecta, el juego les pedirá que intenten de nuevo o les dará pistas adicionales.

#### Finalización del juego:
Una vez resueltos todos los problemas, se desbloqueará el último QR con un mensaje de victoria o una recompensa.

## 4. Posibles Implementaciones Técnicas
El juego puede desarrollarse de diferentes maneras:

- **Uso de formularios de Google Forms**: Cada código QR dirige a un formulario con una pregunta. Al responder correctamente, se muestra el siguiente QR.
- **Aplicación en Python**: Un programa en Python generará códigos QR dinámicos basados en respuestas correctas.
- **Sitio web interactivo**: Se puede programar una plataforma web donde los jugadores ingresen respuestas y desbloqueen pistas automáticamente.

Este proyecto permitirá que los estudiantes aprendan álgebra lineal de una manera dinámica y aplicada a la vida real, combinando matemáticas, tecnología y juegos interactivos.

---

## Marco Teórico

### 1. Álgebra Lineal: Fundamentos y Aplicaciones
El álgebra lineal es una rama fundamental de las matemáticas que estudia los vectores, las matrices, los sistemas de ecuaciones lineales y las transformaciones lineales. Estas herramientas permiten representar y resolver una gran variedad de problemas que surgen en ciencias aplicadas, ingeniería, informática, y más recientemente, en tecnologías como el reconocimiento de patrones, la inteligencia artificial y la codificación de información.

#### Conceptos Clave:
- **Vectores y Espacios Vectoriales**: Son elementos que poseen dirección y magnitud.
- **Matrices**: Representan datos o transformaciones lineales y se pueden realizar diversas operaciones sobre ellas.
- **Sistemas de Ecuaciones Lineales**: Se resuelven mediante métodos como eliminación de Gauss.
- **Determinantes**: Ayudan a identificar si un sistema tiene solución única.
- **Transformaciones Lineales**: Son funciones que transforman vectores respetando operaciones de suma y producto escalar.

---

### 2. Códigos QR y su Relación con el Álgebra Lineal
Los **códigos QR (Quick Response)** son códigos de barras bidimensionales que almacenan información en forma de matriz de celdas binarias. Su capacidad para contener y corregir errores se debe al uso de álgebra lineal.

#### Estructura de un Código QR:
- **Matriz de datos**: Representa la información codificada.
- **Patrones de detección y alineación**: Facilitan la lectura desde cualquier ángulo.
- **Corrección de errores**: Implementada mediante algoritmos matemáticos como los **códigos de Reed-Solomon**, utilizando álgebra lineal y teoría de polinomios.

#### Corrección de errores y álgebra lineal:
La corrección de errores se basa en operaciones lineales que permiten detectar errores y reconstruir datos faltantes. Se utilizan matrices generadoras y de verificación.

---

### 3. Aplicación en el Proyecto: Escape Room QR Matemático
Este proyecto propone una aplicación educativa que combina álgebra lineal con la generación de códigos QR en Python para crear una experiencia interactiva tipo **escape room matemático**.

#### Dinámica del juego:
- Cada nivel del juego presenta un problema de álgebra lineal.
- El enunciado de cada problema está codificado en un código QR.
- Al escanear el código, el jugador visualiza el problema y debe resolverlo.
- Si responde correctamente, el programa genera un nuevo código QR con la siguiente pista.
- El juego continúa hasta que se resuelvan todas las pistas.

#### Ejemplos de problemas usados en el juego:
- **Sistemas de ecuaciones**: Resolver 2x + 3y = 13 y x - y = 1.
- **Transformación lineal**: Aplicar una matriz como [[2,0],[0,3]] al vector (2,1).
- **Determinantes**: Calcular el determinante de una matriz 2x2 o 3x3.

Este tipo de actividad promueve el aprendizaje activo y refuerza habilidades de resolución de problemas.

---

### 4. Herramientas Utilizadas
Para el desarrollo de esta aplicación se emplearon herramientas tecnológicas accesibles y poderosas:

- **Python**: Lenguaje de programación utilizado para desarrollar la aplicación.
- **Librería qrcode**: Permite generar códigos QR a partir de textos o enlaces.
- **Pillow (opcional)**: Para visualizar o guardar las imágenes de los códigos QR.
- **Conocimientos de álgebra lineal**: Aplicados en el diseño de los problemas y la verificación de respuestas.

---

## Conclusión del Marco Teórico
Este proyecto demuestra cómo el álgebra lineal, más allá de ser una teoría abstracta, tiene aplicaciones directas en el mundo digital, como en la construcción y lectura de códigos QR. Al implementar un escape room educativo con problemas de álgebra lineal y pistas en códigos QR, se crea una herramienta innovadora que une matemáticas, tecnología y juego, fomentando una comprensión más profunda de los conceptos matemáticos y su utilidad en la vida real.

---

## Descripción detallada de los procesos realizados

### 1. Definición del propósito del proyecto
El objetivo principal del proyecto es crear un juego interactivo y educativo basado en álgebra lineal, utilizando códigos QR como medio para presentar los retos matemáticos.

### 2. Diseño de la estructura del juego
El juego fue diseñado como una serie de pistas que el jugador debe resolver. Cada pista contiene un problema de álgebra lineal, y solo si se responde correctamente, se genera la siguiente pista a través de un nuevo código QR.

### 3. Implementación en Python
El juego se desarrolla en Python por su facilidad de uso, versatilidad y capacidad de integración con librerías como `qrcode` y `Pillow`.

#### a) Instalación de librerías necesarias
```bash
pip install qrcode
pip install Pillow
