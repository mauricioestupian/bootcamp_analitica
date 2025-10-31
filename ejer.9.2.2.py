#instalamos biblioteca Seaborn - pip install seaborn
#importamos las bibliotecas necesarias
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
#Cargar el archivo .csv 

url= "https://drive.google.com/uc?export=download&id=1VbrQjDF2Br0tjHHiruUnp-0qmnQwon1I"
df=pd.read_csv(url )
print(df.head())

#Seleccionar columnas numericas para el mapa de calor
df_numeric=df.select_dtypes(include="number")
print("Columnas numericas:")
print(df_numeric.head())

#Calcular la matriz de correlacion
correlation_matrix=df_numeric.corr()
print("Matriz de correlacion:")
print(correlation_matrix)

#Crear el mapa de calor usando matplotlib y seaborn
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Mapa de calor de la matriz de correlacion")
plt.tight_layout()
plt.show()