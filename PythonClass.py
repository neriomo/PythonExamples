"""Programacion orientada a objetos"""
#Un objeto es una entidad que agrupa un estado y funcionalidad relacionadas
#El estado se define a traves de variables llamadas atributos
#La funcionalidad se define a traves de funciones llamadas metodos

#Una clase es una plantilla generica para instanciar dicho objeto,
#donde se definen los atributos y funciones


#las clases en python se definen


#ejemplo clase circulo
class Circulo:
	"""Abstraccion de un circulo"""		
	def __init__(self, radio):		#def__init__ se coloca justo despues de crear un nuevo objeto(instanciacion) 
		self.radio = radio			# el atributo self se usa para referirse a sus atrivutos self.radio

	def area(self):
		if self.radio >= 0:
			print("area:", 3.14*self.radio**2)
		else:
			print("area does no exist")										
	
	def diametro(self):
		if self.radio >= 0:
			print("diametro:", self.radio*2)
		else:
			print("diametro does not exist")

	def perimetro(self):
		if self.radio >= 0:
			print("perimetro:", 3.14*self.radio*2)
		

mi_circulo = Circulo(0)

print (mi_circulo.radio)
mi_circulo.area()
mi_circulo.diametro()
mi_circulo.perimetro()

#ejemplo clases Coche

class Coche:
	"""Abstraccion de un Coche"""
	def __init__(self, gasolina):
		self.gasolina = gasolina
		print "tenemos ", gasolina, "litros"

	def arrancar(self):
		if self.gasolina > 0:
			return True
		else:
			return False

	def conducir(self):
		if self.gasolina > 0:
			self.gasolina -= 1
			print "Quedan", self.gasolina, "litros"
		else:
			print "No se mueve"


	


mi_coche =  Coche(15)
print("gasolina del coche: ",mi_coche.gasolina)

while mi_coche.arrancar() == True:
	mi_coche.conducir()


print "gasolina gastada en el objeto"
mi_coche.conducir()