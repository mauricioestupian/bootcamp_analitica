import matplotlib.pyplot as mplo

meses=["Enero","Febrero","Marzo","Abril"]
ventas=[120,150,110,200]

mplo.plot(meses,ventas, color="#E32AD7")
mplo.title("Evolucion de ventas")
mplo.xlabel("Meses")
mplo.ylabel("Ventas")
mplo.grid(True)
mplo.show()