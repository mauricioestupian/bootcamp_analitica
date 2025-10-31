#importamos las bibliotecas necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Cargar el archivo .csv
#url = "https://drive.google.com/uc?export=download&id=1VbrQjDF2Br0tjHHiruUnp-0qmnQwon1I"
#df = pd.read_csv(url)
#Modificar para cargar el archivo excel localmente
df= pd.read_excel("data/datos_comparacion.xlsx")
#Para importar archivos excel en versiones anteriores xls se debe usar: pd.read_excel("data/datos_comparacion.xls", engine='xlrd')
#instalar libreria xlrd si no esta instalada: pip install xlrd
#df= pd.read_excel("data/datos_comparacion.xls")
#cambiar directorio a mis documentos en este caso; es independiente en cada equipo segun su direccionamiento
df= pd.read_excel("../../Documents/datos_comparacion.xlsx")
print(df.head())

#Asegurar que columnas "Edad" e "Ingreso Mensual" sean numéricas
df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")
df["Ingreso Mensual"] = pd.to_numeric(df["Ingreso Mensual"], errors="coerce")

#eliminar filas con valores NaN en "Edad" o "Ingreso Mensual"
df.dropna(subset=["Edad", "Ingreso Mensual"],inplace=True)
#Inplace modifica el dataframe original eliminando las filas con NaN
print(df.head())

# Crear una nueva columna "Grupo Edad" basada en rangos de edad
df['Grupo Edad2'] = pd.cut(df['Edad'], bins=[0,18, 31, 50,51], labels=['Menores','entre 18-30', 'entre 31-50', '51 y más'])
print(df.head())
# Crear una nueva columna "Grupo Edad" basada en rangos de edad haciendo uso de funcion 
def clasicar_edad(edad):
    if 18 <= edad <= 30:
        return 'Jovenes'
    elif 31 <= edad <= 50: 
        return 'Adultos'
    elif edad > 50:
        return 'Mayores'

df['nueva_columna'] = df["Edad"].map(clasicar_edad) #ejemplo de uso de la funcion
df['Grupo Edad'] = df['Edad'].apply(clasicar_edad)

#filtrar datos para incluir datos validos en "Grupo Edad"
df = df[df['Grupo Edad'] != 'Fuera de rango']
print(df.head())

#generar grafico de caja con seaborn

sns.set(style="whitegrid")
colors = ["Cyan", "Magenta", "Yellow"]
plt.figure(figsize=(14,6))
sns.kdeplot(data=df, x="Ingreso Mensual", hue="Grupo Edad", fill=True, common_norm=False, alpha=0.5, palette=colors)

#personalizar el grafico
plt.title("Distribución de Ingreso Mensual por Grupo de Edad")
plt.xlabel("Ingreso Mensual")
plt.ylabel("Densidad")
plt.tight_layout()
plt.show()