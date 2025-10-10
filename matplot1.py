#Instalar Matplotlib
#pip install matplotlib o python -m pip install matplotlib
import matplotlib.pyplot as mplo

productos=["Manzanas","Peras","Naranjas"]
ventas=[50,80,30]

mplo.bar(productos,ventas)
mplo.title("Ventas por Producto")
mplo.xlabel("Productos")
mplo.ylabel("Ventas")
mplo.show()