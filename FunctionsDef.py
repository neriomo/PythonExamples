"""Funciones en python"""
#las funciones es un fragmento de codigo asociado a un nombre
#que realiza un serie de tareas y devuelve un valor
#los valores mutables se pasan por referencia y los inmutables por valor
print ("funciones en python")
valor1 = 10
valor2 = 20
print ("el valor 1 es ",valor1, "el valor2 es ",valor2 )
print

def mostrar ( valor1,  valor2):
	"""Muestra los parametros""" # las funciones llevan una cadena de documentacion
	print ("Los valores son")
	print (valor1,  valor2)


def sumar (valor1, valor2):
	"""imprime la suma de ambos valores"""
	print("la suma es ", valor1+valor2)


def suma_retorna(valor1, valor2):
	"""retorna la suma de ambos valores """
	return valor1 + valor2


def imprimir ( texto, veces =1):#valor por defecto
	"""Imprimer el texto n veces"""
	print (texto * veces)

def mostrar_varios(entero1, entero2, *otros):		#si colocamos ** seria un diccionario y no una tupla
	"""recibe 2 enteros y una tupla y las muestra"""
	print("parametro1", entero1, "parametro2", entero2)
	print("el tercer argumento es una tupla y se enviaron:")
	for valor in otros:
		print(valor)


def retornar_dos(valor1, valor2): # se retorna una tupla =D
	"""retorna una tupla con los valores multiplicados por 1000"""
	return valor1*1000, valor2*1000





mostrar(valor1, valor2)
print
sumar (valor1, valor2)
print
print ("la suma que se retorna es ", suma_retorna(valor1,valor2))

imprimir("living on a prayer \n", valor2)
print
mostrar_varios (1,2,3,4,5,6,7,8,9,10)
print
a,b = retornar_dos(valor1, valor2)
print( "el primer retorno es", a, "el segundo retorno es ", b)
