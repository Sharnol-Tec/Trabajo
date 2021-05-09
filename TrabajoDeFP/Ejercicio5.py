#datos de entrada
print("ingrese el monto a repartir:")
mrepartir=input()
mrepartir=float(mrepartir)
#proceso
juan=0.45*mrepartir
pedro=0.6*juan
luis=mrepartir-(pedro+juan)
#datos de salida
print("juan recibio:",juan,"soles")
print("pedro recibio:",pedro,"soles")
print("luis recibio:",luis,"soles")