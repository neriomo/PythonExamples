"""Control de flujo """
print ("Estructuturas de Control")
print
print ("operador if")

nombre = "nerio"
num = 5
contador = 0
secuen = [1,2,3,4,5,6,7,8,9] #lista de numeros complejos (secuencia)
if nombre ==  "nerio":
	print("encontrado")
	print("Nerio Moran")

print

print ("operador if...else")
if nombre == "neio":
	print("encontrado")
else:
	print("no encontrado")

print

print ("operador if...elif...else")
if num > 0:
	print("positivo")
elif num <0:
	print("negativo")
else:
	print("Cero")

print


print ("operador while ")

while contador < 10:
	print(contador)
	contador=contador +1;
print
print("introduzca una cadena, escriba adios para salir")
while True:
	entrada = raw_input(">") #espera a recibir un dato
	if entrada == "adios":
		print ("exit")
		break
	else:
		print(entrada)

print 

print ("operador for...in 					(solo muestra, no modifica)")
for valor in secuen:
	print(valor)

print

print ("operador for indice in range (len(lista))")
print ("Los elementos en la lista son")
print (secuen)

for indice in range(len(secuen)): #len() devuelve la longitud de la lista
	secuen[indice] = secuen[indice] * 10
	

print
print ("ahora los elementos en la lista son")
print (secuen)