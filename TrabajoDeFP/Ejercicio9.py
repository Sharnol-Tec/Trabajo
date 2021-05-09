#datos de entrada
print("ingrsar el presio del producto:")
pp=input()
pp=float(pp)
print("ingrasr la cantidad de unidades adquiridas:")
ua=input()
ua=int(ua)

#proceso
ic=pp*ua
pd=0.10*ic
sd=0.10*(ic-pd)
dt=pd+sd
ip=ic-dt

#salida
print("importe de la compra es:",ic)
print("importe del descuento total es:",dt)
print("importe a pagar es:",ip)