"""Colecciones en python"""

print("Colecciones: Tuplas")
#para definir una tupla se usan (), y todo lo aplicado a las listas se aplica a las Tuplas
tupla1 = (1,) #una tupla de un 1 entero
tupla2 = (1,2,3,4,5,6,) #una tupla de enteros
tupla3 = ("hola", [100,200,300],True, 1+2j ) #tupla de elementos de diferentes tipos
print ("la tupla1 contiene")
print (tupla1)
print

print ("la tupla2 contiene")
print (tupla2)
print

print ("la tupla3 contiene")
print (tupla3)
print

#para acceder a un elemento especifico usamos el mismo operador que en las listas
print ("El elemento 1 de la tupla3 es ")
print (tupla3[0])

"""Las listas y las tuplas son objetos llamados secuencias al igual que las cadenas
	 la diferencia entre estas es que las tuplas no poseen mecanismos de modificacion
	 y son de tamaño fijo.(No se modifican los valores una vez creada)