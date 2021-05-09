#datos de entrada
print("digite el monto de la donacion:")
donacion=input()
donacion=float(donacion)

#proceso
MG=0.45*donacion
G=0.8*MG
p=0.2*(MG+G)
T=donacion-(MG+G+p)
#salida de datos
print("el area de Medicina General recibio:",MG,"soles")
print("el area de Ginecologia recibio:",G,"soles")
print("el area de Pediatria rcsibio:",p,"soles")
print("el area de Traumatologia recibio:",T,"soles")