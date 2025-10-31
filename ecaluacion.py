import pandas as pd
#enlace para descarga directa de archivos desde google drive
#https://drive.google.com/uc?export=download&id=ID_DEL_ARCHIVO


#Cargar los datos

data = {
    "ID": [1,2,3,4,5,6,7,8,9,10],
    "Producto": ["Laptop", "Monitor", "Teclado", "Laptop", "Tablet", "Impresora", "Smartphone", "Mouse", "Monitor", "Tablet"],
    "Categoría": ["Electrónica", "Computación", "Accesorios", "Electrónica", "Computación", "Oficina", "Electrónica", "Accesorios", "Computación", "Computación"],
    "Ventas": [15, 8, 25, 10, 20, 5, 30, 40, 12, 18],
    "Precio Unitario": [1200, 500, 50, 1100, 700, 400, 800, 20, 450, 750],
    "Total Ventas": [18000, 4000, 1250, 11000, 14000, 2000, 24000, 800, 5400, 13500],
    "Región": ["Norte", "Sur", "Norte", "Este", "Oeste", "Norte", "Sur", "Este", "Oeste", "Norte"]
}
df=pd.DataFrame(data)
print("Datos ventas:")
print(df.head())

df['Ventas']= pd.to_numeric(df['Ventas'], errors='coerce')
total=df['Ventas'].sum()
print(total)

# Agrupar por categoría y sumar las ventas
ventas_por_categoria = df.groupby('Categoría')['Total Ventas'].sum()

# Ordenar de mayor a menor
ventas_ordenadas = ventas_por_categoria.sort_values(ascending=False)
print("Ventas por categoría ordenadas:")
print(ventas_ordenadas) 

# Mostrar la categoría con más ventas
categoria_top = ventas_ordenadas.idxmax()
ventas_top = ventas_ordenadas.max()
print(f"La categoría con más ventas es '{categoria_top}' con un total de {ventas_top} ventas.")

import os

# Ruta del directorio donde está el script
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Listar archivos en ese directorio
archivos = os.listdir(directorio_actual)

print("Archivos en el mismo directorio:")
for archivo in archivos:
    print(archivo)

