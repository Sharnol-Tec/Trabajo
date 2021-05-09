#definir variables
nombre=input("digite nombre del empleado:")
horas=float(input("digite el numero de horas laboradas"))
#proceso
if horas<=50:
  salario=horas*30000
else:
  salario=(horas-50)*40000+50*30000
#salida
print("el nombre de empleado es:",nombre)
print("su salario a pagar es:",salario)