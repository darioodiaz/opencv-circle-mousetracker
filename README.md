# Opencv Circle Mousetracker
Forma alternativa y simple de mover el cursor e interactuar con la PC usando solo una webcam y un circulo de color.

Proyecto surgido como trabajo final de la material Inteligencia Artificial en UTN-FRC.

## Presentacion

https://drive.google.com/file/d/0B3NVxALbY0gQa1M1N0xGbGd2YWs/view?usp=sharing

## Documentacion de referencia

Filtro por umbral: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding

Filtrado de colores: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces


Transformada de hoguh: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html#py-hough-lines

Transformada hough circulos: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html#hough-circles

Complemento de deteccion de circulos: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_table_of_contents_contours/py_table_of_contents_contours.html#table-of-content-contours

## Quickstart

Librerias: win32api, opencv, numpy
Python: 2.7

El codigo tiene una variable Debug, que si toma el valor True mostrara unos sliders que permitira filtrar lo que la camara esta viendo en un rango de colores, una vez detectado el rango de colores deseados debemos anotar esos valores minimos y maximos. Dentro del codigo estan 2 arrays lower y upper, estos deberan tener los valores que encontramos antes.

Si Debug esta en False, la aplicacion empieza procesa la iamgen de la camara y si detecta un circulo pondra su contorno en verde y movera el mouse segun se mueva el circulo.
