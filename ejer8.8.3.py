import pandas as pd

#Cargar los archivos .csv desde URLs
url="https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df=pd.read_csv(url)
print("Datos ventas:")
print(df.head(10))  
print("\nNúmero total de registros:")
print(len(df))

#Agrupar los datos por "Categoría" Producto
df_conteo=df.groupby("Producto").size().reset_index(name='Conteo')
print("\nConteo por Producto:")
df_conteo=df_conteo.sort_values(by='Producto', ascending=True)
print(df_conteo)

#Conteo sin agrupamiento
conteo_total=df['Producto'].value_counts().reset_index()
conteo_total.columns=['Productosss','Conteo2']
print("\nConteo total por Producto sin agrupamiento:")
print(conteo_total)

#Combinar agrupamiento y conteo
df_grupo=df.groupby("Producto")['Cantidad Vendida'].count().reset_index()
df_grupo.columns=['Productico','Conteo_Ventas']
print("\nConteo agrupado por Producto:")
print(df_grupo)

#Sumar columna nueva por categoría
df_grupo_sum=df_grupo["Conteo_Ventas"].sum()
print(f"\nSuma total de Conteo_Ventas: {df_grupo_sum}")
'''
#Sumar la cantidad vendida por categoría
df_suma=df.groupby("Categoría")['Cantidad Vendida'].sum().reset_index()
df_suma.columns=['Categoría','Suma_Cantidad_Vendida']
print("\nSuma de Cantidad Vendida por Categoría:")
print(df_suma)'''