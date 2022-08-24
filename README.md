Pasos previos para al encendido del robot:
- Conectarse a una misma red raspberry y pc, la red que de momento esta configurada es:
    - SSID: Redmi_Note_9_pro
    - contraseña: pepe pecas

Para el optimo funcionamiento del robot, es necesario:
- Abrir dos terminales, ambas por ssh y con la opción -X que permite abrir ventanas emergentes las cuales son requeridas para la visualización de objetos en pantalla, ejemplo de comando que se debe ingresar: ssh -X pi@136.136.136.136 (Evidentemente debe ponerse como IP aquella otorgada por la red configurada anteriormente)
- correr el archivo script2.py en una de las terminales, el cual permite mover el robot por medio de comandos. 
- En la segunda terminal, deberán dirigirse a la siguiente ruta dentro del directorio principal del proyecto (Proyecto_Final_SI): exalmples/tflite/examples/object_detection/raspberry_pi/ y debe de correr el archivo detect.py con la opción --model y deben poner la ruta del modelo del proyecto principal y el nombre del modelo (Sé que suena muy complicado pero aquí les va un ejemplo equisde): 
    - python detect.py --model /home/Code/Proyecto_final_SI/model/CansDetectorModel.tflite

Esto permitiría abrir la una ventana emergente y visualizar el las latas que hasta el momento detecta el modelo, good luck and have fun with the Doctor Said:) 
