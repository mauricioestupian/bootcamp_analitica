import matplotlib.pyplot as mplo

edades=[20,21,22,25,25,26,27,30,35,40,42]

mplo.hist(edades, bins=5,color="red",edgecolor="black")
mplo.title("Rango edades")
mplo.xlabel("Edades Rangos")
mplo.ylabel("Distribucion edades")
mplo.show()