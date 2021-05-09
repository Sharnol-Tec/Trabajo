print("ingrese el nombre del empleado:")
nombre=input()
print("cuantas horas trabajo esta semana",nombre,":")
horas=input()
horas=int(horas)
print ("cuanto se paga por hora? :")
precioH=input()
precioH=float(precioH)
#Evaluando el salario
if (horas<=40):
  pago=horas*precioH
  print ("El sueldo final" ,nombre, "es $",pago)
else:
  extras=horas-40
  pago=40*precioH
  pagoFinal=pagos + (extras*precioH*2)
  
print ("El sueldo final" ,nombre, "es $",pagoFinal)