"""
Diccionarios: Son una estructura de datos manejados mediante "clave" : valor
Los definimos mediante {}
las claves son únicas e inmutables: números, cadenas o tuplas.
Los valores: puedesn ser cualquier tipo de datos y son mutables.
Los diccionarios no tienen un orden especifico
"""
#crear un diccionario 1ra forma
diccionario = {
    "nombre" : "Marcelo",
    "edad" : 37,
    "ciudad" : "Puerto Montt"
}"""
Diccionarios: Son una estructura de datos manejados mediante "clave" : valor
Los definimos mediante {}
las claves son únicas e inmutables: números, cadenas o tuplas.
Los valores: puedesn ser cualquier tipo de datos y son mutables.
Los diccionarios no tienen un orden especifico
"""
#crear un diccionario 1ra forma
diccionario = {
    "nombre" : "Marcelo",
    "edad" : 37,
    "ciudad" : "Puerto Montt"
}
print(diccionario)
#Segunda manera de crear un diccionario dict(clave = "String")
diccionario2 = dict(marca = "Toyota", modelo="Yaris", año= 2020)
#acceder a los elementos de un diccionario.
print(diccionario2["marca"])
#acceder a los elementos .get()
print(diccionario.get("nombre"))
#agregar o modificar un valor de un diccionario
#1-actualizar un valor 
diccionario2["modelo"]="Raize"
print(diccionario2)
#2- actualizar con .update
diccionario2.update({"año": 2024})
print(diccionario2)
"""
Eliminar elementos 
usando el método pop().
utilizando la palabra clave del
Usando el método .popitem()
utilizado el método clear()  vacia el diccionario
"""


diccionario_3={
    "nombre": "Juan",
    "apellido": "Mansilla",
    "edad": 23,
    "comuna": "Puerto Varas"
,}

#eliminar .pop()eliminar edad
diccionario_3.pop("edad")
print(diccionario_3)

#elimina con del nombre_diccionario["clave_a_eliminar"]

del diccionario_3["comuna"]
print(diccionario_3)


#popitem()elimina el ultimo par clave valor : diccionario.popitem

diccionario_3.popitem()
print(diccionario_3)

#clear()n
diccionario_3.clear()
print(diccionario_3)

"""
len() retorna el número de pares clave valor
str() retorna una representacion del diccionario en cadena.
Métodos
keys() Retorna las claves
values() Retorna los valores
items() Retorna todos los items clave valor
copy() Realiza una copia de mi diccionario
"""
diccionario_4 = {

    "Asignatura": "Fundamentos de programación",
    "Semestre": "Segundo",
    "Carrera": "ingenieria informática",
    "Años": 4,
    "Intitución": "DUOC UC",
    "Sede": "Puerto Monttcito",
}
print("-----"*10)

print(diccionario_4.keys())
print(diccionario_4)
#Contar los pares de elementos que tiene mi diccionario
#print(len(nombre_diccionario))
print(len(diccionario_4))
#imprimir en formato cadena mi diccionario str()
print(str(diccionario_4)) 

#imprimir todas las claves del diccionario keys()
print(diccionario_4.keys())
#imprimir los valores values()
print(diccionario_4.values())

#crear una copia de mi diccionario 
#nombre_nuevo_diccionario = nombre_diccionario.copy()
print("-----"*10)
nuevoDiccionario = diccionario_4.copy()
print(nuevoDiccionario)

#iterar sobre mi diccionario se imprimen las claves
# for indice in nombre_diccionario:
    #print indice


for indice in diccionario_4:
    print(indice)


#iterar sobre mi diccionario e imprimir los valores
# for indice in nombre_diccionario.values():
    #print indice
    
    for indice in diccionario_4.values():
        print(indice)

"""Iterar sobre pares clave: valor
for clave,valor in nombre_diccionario.items():
    print()
"""
for clave, valor in diccionario_4.items():
    print(clave+":"+str(valor)
print(diccionario)
#Segunda manera de crear un diccionario dict(clave = "String")
diccionario2 = dict(marca = "Toyota", modelo="Yaris", año= 2020)
#acceder a los elementos de un diccionario.
print(diccionario2["marca"])
#acceder a los elementos .get()
print(diccionario.get("nombre"))
#agregar o modificar un valor de un diccionario
#1-actualizar un valor 
diccionario2["modelo"]="Raize"
print(diccionario2)
#2- actualizar con .update
diccionario2.update({"año": 2024})
print(diccionario2)
"""
Eliminar elementos 
usando el método pop().
utilizando la palabra clave del
Usando el método .popitem()
utilizado el método clear()  vacia el diccionario
"""


diccionario_3={
    "nombre": "Juan",
    "apellido": "Mansilla",
    "edad": 23,
    "comuna": "Puerto Varas"
,}

#eliminar .pop()eliminar edad
diccionario_3.pop("edad")
print(diccionario_3)

#elimina con del nombre_diccionario["clave_a_eliminar"]

del diccionario_3["comuna"]
print(diccionario_3)


#popitem()elimina el ultimo par clave valor : diccionario.popitem

diccionario_3.popitem()
print(diccionario_3)

#clear()n
diccionario_3.clear()
print(diccionario_3)

"""
len() retorna el número de pares clave valor
str() retorna una representacion del diccionario en cadena.
Métodos
keys() Retorna las claves
values() Retorna los valores
items() Retorna todos los items clave valor
copy() Realiza una copia de mi diccionario
"""
diccionario_4 = {

    "Asignatura": "Fundamentos de programación",
    "Semestre": "Segundo",
    "Carrera": "ingenieria informática",
    "Años": 4,
    "Intitución": "DUOC UC",
    "Sede": "Puerto Monttcito",
}
print("-----"*10)

print(diccionario_4.keys())
print(diccionario_4)
#Contar los pares de elementos que tiene mi diccionario
#print(len(nombre_diccionario))
print(len(diccionario_4))
#imprimir en formato cadena mi diccionario str()
print(str(diccionario_4)) 

#imprimir todas las claves del diccionario keys()
print(diccionario_4.keys())
#imprimir los valores values()
print(diccionario_4.values())

#crear una copia de mi diccionario 
#nombre_nuevo_diccionario = nombre_diccionario.copy()
print("-----"*10)
nuevoDiccionario = diccionario_4.copy()
print(nuevoDiccionario)

#iterar sobre mi diccionario se imprimen las claves
# for indice in nombre_diccionario:
    #print indice


for indice in diccionario_4:
    print(indice)


#iterar sobre mi diccionario e imprimir los valores
# for indice in nombre_diccionario.values():
    #print indice
    
    for indice in diccionario_4.values():
        print(indice)

"""Iterar sobre pares clave: valor
for clave,valor in nombre_diccionario.items():
    print()
"""
""""""""""""""""""""""""
for clave, valor in diccionario_4.items():
    print(clave+":"+str(valor))