#importar pandas
import pandas as pd

#Cargar los archivos .csv desde URLs
url="https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df=pd.read_csv(url)
#Mostrar las primeras 10 filas del DataFrame para explorar su estructura.
print("Datos ventas:")
print(df.head(10))

#Agrupar los datos por la columna "Categoría"
precio_promedio=df.groupby("Categoría")['Cantidad Vendida'].sum().round(2).reset_index()
print("\nSuma Cantidad Vendida por Categoría:")
precio_promedio=precio_promedio.sort_values(by='Cantidad Vendida', ascending=True)#Ordenar por Categoría
print(precio_promedio)  