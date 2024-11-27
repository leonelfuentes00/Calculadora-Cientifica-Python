Pasos para ejecutar el programa

Clonar o descargar el proyecto: 
    Si el proyecto está en un repositorio, clónalo utilizando Git:

        git clone https://github.com/leonelfuentes00/Calculadora-Cientifica-Python
        cd https://github.com/leonelfuentes00/Calculadora-Cientifica-Python

Ejecutar el programa: 
    Desde la terminal o consola, navega hasta el directorio del proyecto y ejecuta el siguiente comando:

        python main.py
    Esto abrirá la interfaz gráfica de la calculadora.

Uso de la calculadora:

    Operaciones básicas: 
        Introduce números y selecciona las operaciones directamente desde la interfaz.

    Cálculo de integrales:
        Selecciona la función que deseas integrar (Primera, Segunda, o Tercera).
        Ingresa los parámetros solicitados en la ventana emergente.
        Pulsa "Calcular" para obtener los resultados.
        Salida del programa: Haz clic en el botón "Salir" o presiona la tecla q.

Notas importantes
    Imágenes no cargadas: Si no se muestra la imagen en la interfaz, verifica que el archivo spiderman-png-137.png esté en la carpeta img y que su ruta sea correcta en el archivo controller.py.

Errores en la consola:

    Si recibes errores relacionados con módulos no encontrados, asegúrate de instalar las bibliotecas usando el comando:

        pip install -r requirements.txt

Compatibilidad:

    El programa está diseñado para ejecutarse en sistemas operativos Windows. En Linux o macOS, verifica que las funciones de keyboard sean compatibles.

    Error al calcular una integral:

    Revisa los parámetros ingresados y asegúrate de que estén en el formato correcto.
    Asegúrate de que los límites sean numéricos y válidos.
    Problemas con el teclado:

    Si las teclas rápidas no funcionan correctamente, asegúrate de que la biblioteca keyboard esté instalada y que no haya conflictos con otras aplicaciones en tu sistema.
    Error de sintaxis o falta de módulos:

    Verifica que estés usando una versión de Python 3.9 o superior.

Reinstala las bibliotecas con:

        pip install --upgrade pip
        pip install -r requirements.txt