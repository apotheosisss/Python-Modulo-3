#importar las librerias para trabajar con archivos

import csv #Excel
import json #Json()

#Función para crear archivos .txt
def crear_archivo_txt(nombre_archivo, contenido):
    """
    Crea un archivo de texto y escribe contenido en él.
    """
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"Archivo: {nombre_archivo} creado exitosamente.")

#Función para crear aarchivos JSON

def crear_archivo_json(nombre_archivo, datos):
    """
    Crea un archivo JSON y escribe contenido en él
    """
    with open(nombre_archivo, 'w')as archivo:
    #Conversión de diccionario en json y lo escribe en el archivo.
        json.dump(datos,archivo,indent=4)
    print(f"Archivo JSON: {nombre_archivo} creado exitosamente.")

#Función para crear archivo CSV
def crear_archivo_csv(nombre_archivo, datos):
    """
    Crea un archivo CSV y escribe contenido en él
    """
    with open (nombre_archivo, 'w', newline='') as archivo:
    #Creando un objeto que escribe
        escritor_csv = csv.writer(archivo)
    #Escribe las filas + datos en el csv
        escritor_csv.writerows(datos)
    print(f"Archivo CSV: {nombre_archivo} creado exitosamente.")

#Función leer el archivo txt
def leer_archivo_txt(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()
    
#Función leer el archivo csv
def leer_archivo_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
    #Lee el contenido del csv y lo transforma en una lista de listas o matriz bidimensional    
        return list(csv.reader(archivo))

#Función leer el archivo JSON
def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
    #Lee el contenido dle archivo y lo convierte a un diccionario    
        return json.load(archivo)

#Funcion para agregar contenido a un archivo de texto existente
def agregar_contenido_txt(nombre_archivo, contenido):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(contenido)
    print(f"Contenido agregado al archivo: {nombre_archivo} exitosamente.")

contenido_txt = "Este es un texto de ejemplo, xd"

crear_archivo_txt('ejemplo_crear_archivo.txt', contenido_txt)

#Datos para el archivo CSV
datos_csv =[
    ['nombre', 'edad', 'ciudad'],
    ['Claudio', 18, 'Puerto Montt'],
    ['José', 20, 'Coquimbo'],
    ['Samuel', 38, 'Talca']
]

crear_archivo_csv('Ejemplo.csv', datos_csv)

#Datos para el JSON
datos_json = {
    'nombre': 'Carlos',
    'edad' : 23,
    'ciudad' : 'Llanquihue',
    'habilidades' : ['Python', 'Java', 'SQL']    
}
crear_archivo_json('ejemplo.json', datos_json)

#Leer el contenido
print("Contenido del archivo de texto")
print(leer_archivo_txt('ejemplo_crear_archivo.txt'))

#Leer el contenido
print("Contenido del archivo de CSV")
for fila in leer_archivo_csv('Ejemplo.csv'):
    print(fila)
#Leer el contenido
print("Contenido del archivo JSON")
print(json.dumps(leer_archivo_json('ejemplo.json'), indent=4))

#Agregar un contenido adicional a un archivo

contenido_adicional_txt = "\nEste es un contenido adicional, ayuda."
agregar_contenido_txt('ejemplo_crear_archivo.txt', contenido_adicional_txt)

#Leer y mostrar el contenido actualizado del archivo de texto
print("\nContenido actualizado del txt")
print(leer_archivo_txt('ejemplo_crear_archivo.txt'))