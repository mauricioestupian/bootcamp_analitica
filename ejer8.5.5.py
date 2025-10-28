#Ejercicio: Cálculo de "Ingresos Totales" tras la Fusión de Datos
#Importando librerías necesarias
import pandas as pd

#Cargar los archivos .csv desde URLs
url_ventas = "https://drive.google.com/uc?export=download&id=1txHNdJmFQqfGr1p7_9Y07HjfaHV7oJ1b"
url_productos = "https://drive.google.com/uc?export=download&id=1Vbfvur9orXO3lbb9RQgu27hAg1F9BMKm"

df_ventas = pd.read_csv(url_ventas)
df_productos = pd.read_csv(url_productos)
print("Datos de Ventas:")
print(df_ventas.head())
print("\nDatos de Productos:")
print(df_productos.head())

#Establecer la columna "Producto_ID" como índice en ambos DataFrames
df_ventas.set_index("Producto_ID", inplace=True)
df_productos.set_index("Producto_ID", inplace=True)

#Fusionar los DataFrames utilizando el método adecuado (.join() o pd.merge()).
#df_combinado = df_ventas.join(df_productos, how="inner")
#df_combinado = pd.merge(df_ventas, df_productos, on="Producto_ID", how="inner")
df_combinado = pd.merge(df_ventas, df_productos, left_index=True, right_index=True, how="inner")
print("\nDatos Fusionados:")
print(df_combinado.head())

#Crear una nueva columna llamada "Ingresos Totales" imprimir los 10 primeros registros
df_combinado["Ingresos Totales"] = df_combinado["Cantidad Vendida"] * df_combinado["Precio Unitario"]
print("\nDatos con Ingresos Totales:")
print(df_combinado.head(10))
