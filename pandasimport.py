import pandas as pd

#Cargar el archivo .csv
#df=pd.read_csv("data/archivo.csv", sep=";", names=["Producto";"Precio";"Cantidad"]) uso de names en el escenario que el csv no tienen encabezado
df=pd.read_csv("data/archivo.csv", sep=";")

#mostrar la data del csv
print(df)
print(df.head(2))
df["P_Total"]=df['Precio']*df['Cantidad']
print("La nueva serie es:")
print(df)

#importar columnas especificas del csv
fr2 = pd.read_csv("data/archivo.csv", sep=";", usecols=["Producto","Precio"])
print("Nuevo data frame solo con dos columnas")
print(fr2)

#Importar numero de filas
fr3 = pd.read_csv("data/archivo.csv", sep=";", nrows=2, encoding="utf-8")
print("nuevo data frame solo con dos filas")
print(fr3)

df.to_csv("nuevo_archivo.csv",index=False)
df.to_excel("archivo_excel2.xlsx",index=True)#libreria necesaria -- pip install openpyxl
