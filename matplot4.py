import matplotlib.pyplot as mplo

ingresos=[100,200,300,500,550]
gastos=[80,120,250,400,520]

mplo.plot(ingresos,gastos,)
mplo.title("Gastos vs Ingresos")
mplo.xlabel("Gastos")
mplo.ylabel("Ingresos")
mplo.show()


mplo.scatter(gastos,ingresos, color="Chocolate")
mplo.title("Gastos vs Ingresos")
mplo.xlabel("Gastos")
mplo.ylabel("Ingresos")
mplo.show()