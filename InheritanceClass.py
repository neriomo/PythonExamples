"""Herencia"""

#Hay 3 conceptops basicos para cualquier lenguaje de programacion
#orientado a objetos Herencia, encapsulamiento y polimorfismo
#En la Herencia una sub clase hereda los metodos y atributos de una superclase

#ejemplo Clase Geometria


#Clase Artista
class Artista:
	"""Abstraccion de un Artista"""
	def __init__(self, nombre, edad, sexo):
		self.nombre = nombre
		self.edad = edad
		self.sexo = sexo

	def mostrar_datos(self):
		print ("nombre: ", self.nombre)
		print ("edad:", self.edad)
		print ("sexo: ", self.sexo)

		pass




#Definimos una classe Instrumento
class Instrumento:
	"""superclase Abstraccion de un Instrumento"""
	def __init__(self, precio, marca = "no tiene"):
		self.precio = precio
		self.marca = marca
	
	def tocar(self):
		print ("Estamos tocando musica")

	def romper(self):
		print("Eso lo pagas tu", self.precio,"$$$")
	
	def mostrar_marca(self):
				print ("La marca es", self.marca)

		

#La clase bateria contiene todos los atributos y metodos de la clase Instrumento
class Bateria(Instrumento):
	"""Abstraccion de Bateria"""
	pass



#La clase Guitarra contiene los metodos de la clase intrumento y contiene un metodo
class Guitara(Instrumento):
	"""Abstraccion de una Guitara"""
	def __init__(self,precio,marca,tipo):
		self.tipo = tipo
		self.precio = precio
		self.marca = marca

	def mostrar_tipo(self):
		print ("El tipo es ", self.tipo )
		Instrumento.mostrar_marca(self)
	

										
print("Instanciamos una bateria")
mi_bateria = Bateria(1000, "SteelMaster")
mi_bateria.tocar()
mi_bateria.romper()
mi_bateria.mostrar_marca()

print

print("Instanciamos una Guitarra")
mi_guitarra = Guitara(4000,"Cremona","acustica")
mi_guitarra.tocar()
mi_guitarra.romper()
mi_guitarra.mostrar_marca()

print

print ("Instanciamos un Artista")
mi_artista = Artista ("nerio", 20, "masculino")
mi_artista.mostrar_datos()
print

"""Herencia Multiple"""

# A diferencia de otros lenguajes como java o c# Python permite herencia multiple
# se toma el constructor de la herencia mas a al izquierda "Arstista"
class Musico1(Artista, Instrumento):
		pass

# si quisieramos tener usar todos los atributos de ambas herencias debemos tener un constructor
#propio para la clase musico de lo contrario solo trabajara con los atributos y metodos
#de la herencia mas a la izquierda

class Musico2(Artista , Instrumento):
	"""Abstraccion de un Musico2"""
	def __init__(self, nombre, edad, sexo, precio, marca):
		
		self.precio  = precio
		self.marca = marca
		
		self.nombre = nombre
		self.edad = edad
		self.sexo = sexo

		
	pass



print("instanciamos un musico1 con constructor heredado")
mi_musico1 = Musico1("nerio",20,"masculino")
mi_musico1.mostrar_datos()

print
print("instanciamos un musico2 con constructor sobreescrito")
mi_musico2 = Musico2("nerio",20,"masculino",1000,"Stradivarius")
mi_musico2.mostrar_datos()
mi_musico2.tocar()
mi_musico2.romper()
mi_musico2.mostrar_marca()