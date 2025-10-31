#Importar libredias necesarias
import pandas as pd

#Cargar los archivos .csv desde URLs
url="https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df=pd.read_csv(url)
print("Datos ventas:")
print(df.head(10))
        
#Agrupar los datos por "Categoría"
df_grouped=df.groupby("Categoría")['Cantidad Vendida'].agg(['min', 'max', 'mean', 'std'])

#Muestra los resultados
print("\nEstadísticas por Categoría:")
print(df_grouped)