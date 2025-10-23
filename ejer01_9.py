#inportancion de librerias
import pandas as pd
import matplotlib.pyplot as mplo
import gdown #importar gdown para descargar archivos desde google drive

#Cargar el archivo .csv
df_p=pd.read_csv("data/datos_groupby.csv") #cargar archivo csv con pandas
#carga archivo csv desde google drive con gdown
url = "https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C" 
#url del archivo en google drive
output = "data/datos_group.csv" #nombre del archivo a guardar
gdown.download(url, output, quiet=False) #descargar el archivo desde google drive
df_gd=pd.read_csv("data/datos_group.csv") #cargar archivo csv descargado con gdown

print("Dataframe cargado con pandas:")
print(df_p.head())
print("Dataframe cargado con gdown:")
print(df_gd)    

#agrupar datos por categoria y sumar cantidades vendidas
grouped=df_p.groupby("Categoría")["Cantidad Vendida"].sum().reset_index()
print("Datos agrupados por categoria:")
print(grouped)

#agriupar datos por categoria y sumar catidades vendidas del archivo descargado con gdown
grouped_gd=df_gd.groupby("Categoría")["Cantidad Vendida"].sum().reset_index()
print("Datos agrupados por categoria (gdown):")
print(grouped_gd)

mplo.figure(figsize=(10,6))
mplo.bar(grouped_gd["Categoría"],grouped_gd["Cantidad Vendida"], color=["Cyan","Magenta","Yellow","Green","Blue"])
mplo.title("Ventas por Categoria")
mplo.xlabel("categoríassss")
mplo.ylabel("Cantidad Vendida")
mplo.xticks(rotation=45)
mplo.tight_layout()
mplo.grid(color="#BC3F3F", linestyle="--", linewidth=0.5)
mplo.show()