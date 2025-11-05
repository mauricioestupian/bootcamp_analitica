#importamos pandas
import pandas as pd

#Cargar los archivos .csv desde URLs
url1="https://drive.google.com/uc?export=download&id=1txHNdJmFQqfGr1p7_9Y07HjfaHV7oJ1b"
url2="https://drive.google.com/uc?export=download&id=1Vbfvur9orXO3lbb9RQgu27hAg1F9BMKm"
df_ventas=pd.read_csv(url1)
df_peoductos=pd.read_csv(url2)
'''print("Datos ventas:")
print(df_ventas.head(10))  
print("\nDatos productos:")
print(df_peoductos.head(10))'''

#Realizar la unión de los DataFrames mediante Left Join en base a la columna "Producto ID"
#asegurando que se sonserven todas las filas del DataFrame de ventas
#incluyendo si no hay coincidencias en el DataFrame de productos

df_combinado=pd.merge(df_ventas,df_peoductos, how='left', left_on='Producto_ID', right_on='Producto_ID')
#df_combinado=pd.merge(df_ventas,df_peoductos, how='left', on='Producto_ID')
print("Datos combinados de ventas y productos:")
print(df_combinado.head(10))