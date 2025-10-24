#instalamos biblioteca Seaborn 
#importamos las bibliotecas necesarias
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
#Cargar el archivo .csv 

url= "https://drive.google.com/uc?export=download&id=1VbrQjDF2Br0tjHHiruUnp-0qmnQwon1I"
df=pd.read_csv(url )
print(df.head())

#Asegurar que columnas "Puntuación de Crédito" e "Ingreso Mensual" sean numéricas
df["Puntuacion de credito"]=pd.to_numeric(df["Puntuacion de credito"], errors="coerce")
df["Ingreso Mensual"]=pd.to_numeric(df["Ingreso Mensual"], errors="coerce")
df["Region"]=pd.to_numeric(df["Region"], errors="coerce")#ejemplo con errores y convertir a NaN
#print(df.head())

df['Grupo Credito'] = pd.cut(df['Puntuacion de credito'], bins=[0,300, 600, 700, 800, 900], labels=['Muy Malo', 'Malo', 'Regular', 'Bueno', 'Excelente'])
print(df.head())
#generar grafico de dispersión con seaborn
plt.figure(figsize=(14,6))
sns.boxplot(x="Grupo Credito", y="Ingreo Mensual", data=df, palette="Set2")

#superponer grafico de swarmplot 
sns.swarmplot(x="Grupo Credito", y="Ingreso Mensual", data=df, color="0.25")

#mostrar el grafico
plt.title("Relación entre Puntuación de Crédito e Ingreso Mensual")
plt.xlabel("Puntuación de Crédito")
plt.ylabel("Ingreso Mensual")
plt.tight_layout()
plt.show()