e=int(input("Ingrese la cantidad de empleados: "))
total_sueldos=0
c1=0#entre $100 y $300
c2=0#más de $300
for i in range(e):
    sueldo=float(input("Ingrese el sueldo del empleado:"))
    if sueldo <=300:
        c1 += 1
    else:
        c2 += 1
    total_sueldos +=sueldo
print("Empleados que cobran entre $100 y $300:",c1)
print("Empleados que cobran más de $300:",c2)
print("Gasto total en sueldos:",total_sueldos)