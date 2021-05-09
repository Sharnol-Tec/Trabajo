#datos de entrada
inporte=float(input("digite el importe total vendido en el mes:"))
#proceso
sueldo_basico=300
comision_ventas=0.09*inporte
sueldo_bruto=sueldo_basico + comision_ventas
descuento=0.11*sueldo_bruto
sueldo_neto=sueldo_bruto-descuento
#salida
print("sueldo basico:s/.",sueldo_basico)
print("comision por ventas:s/.",comision_ventas)
print("sueldo bruto:s/.",sueldo_bruto)
print("descuento:s/.",descuento)
print("sueldo neto:s/.",sueldo_neto)