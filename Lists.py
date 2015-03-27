"""Colecciones en python"""
#listas, tuplas y diccionarios
print ("Colecciones: Listas")
#para crear un lista se usan corchetes cerrados []
lista1 = [22,11,10,0,1,2,3,47,5]
#Las listas pueden tener difirente tipos de datos
lista2 = ["que fue", True, 20.45, "Hola", 1+ 2j, [1,2,3,4,5]]
print("La lista1 contiene")
print(lista1)
print
print ("La lista2 contiene")
print (lista2)
print
#para accder a los elementos de la lista 

element1 = lista1[0]
print ("El elemento 1 de la lista 1 es ")
print (element1)
print

print ("El elemento 5 de la lista 2 es ")
element2 = lista2[5]
print (element2)
print
# En caso de querer accder a un elemento especifico de una lista de una lista
element3 = lista2[5][3]
print ("el elemento 4 de lista de el elemento 5 de la  lista2 es ")
print (element3)	
print
#para modficiar un elemento de la lista
print ("el elemeto 1 de la lista 1 es ")
print (lista1[0])
print ("ahora es ")
lista1[0] = 0
print (lista1[0])
print
#para accder a el ultimo, penultimo, antepenultimo elemento de una lista
print ("El ultimo elemento de la lista1 es")
print (lista1[-1])
print ("El penultimo elemento de la lista1 es")
print (lista1[-2])
print
#para realizar un slicing o particionado de una lista
print ("slicing de la lista1", lista1, "de 0 a 3")
slicing = lista1[0:3] #ahora slicing tiene los elemento desde 0a 3 de lista1
print (slicing)	
