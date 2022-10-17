PRIMERA ENTREGA PROYECTO PYTHON (34625) - CODERHOUSE

Autores:
- Jimena Cambronero
- Jexson Montilla
- Jhonathan Rengifo Castillo

OBJETIVO:
- Desarrollar una WEB Django con patrón MVT subida a GitHub que incluya los siguientes puntos:

    1. Herencia HTML.
    2. Por lo menos 3 clases en models.
    3. Un formulario para insertar datos a todas las clases de los models.
    4. Un formulario para buscar algo en la BD.
    5. Readme que indique el orden en el que se prueban las cosas y/o dónde estan las funcionalidades.

INSTRUCCIONES:

El diseño de la WEB con patrón MVT fue realizado con 3 clases para un gimnasio (Cliente, Entrenador, Rutina), cada clase tiene su propio formulario para ingresar datos en la BD que heredan el header de la página de navegación. Para la pagina de inicio se puede acceder mediante el link http://127.0.0.1:8000 en el cual podrá acceder a los link de los formularios. Cabe anotar que sólo se creó el formulario de consulta para la clase cliente en función del nombre.

1. Ingrese a la dirección 127.0.0.1:8000 para ir a la página de inicio.
2. Si desea agregar un nuevo cliente, entrenador o rutina lo puede realizar mediante el formulario correspondiente que podrá encontrarlos accediendo a traves de los botones de "Clientes" , "Entrenadores" y "Rutinas" en la barra superior de la pagina, o accediendo desde el enlace http://127.0.0.1:8000/formularioCliente/, http://127.0.0.1:8000/formularioEntrenador/ o http://127.0.0.1:8000/formularioRutina/ y completando el formulario correspondiente.
3. Si desea realizar una busqueda de algun cliente, ingrese en el boton de "Buscar Cliente" o acceda al link http://127.0.0.1:8000/busquedaCliente/ y coloque el nombre del cliente que desea buscar (ej: Vanessa Antonieta).