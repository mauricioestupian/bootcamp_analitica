#importar la librería pandas
import pandas as pd
import matplotlib.pyplot as plt

#Cargar los archivos .csv desde URLs
url="https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df=pd.read_csv(url)
#print("Datos ventas:")
#print(df.head(10))  

#Agrupar los datos por la columna "Categoría"
precio_promedio=df.groupby("Categoría")['Precio Unitario'].mean().round(2).reset_index()
print("\nPrecio Unitario promedio por Categoría:")
precio_promedio=precio_promedio.sort_values(by='Categoría', ascending=True)#Ordenar por Categoría
print("DataFrame con índice original:")
print(precio_promedio.head())


#No es posible eliminar el índice en pandas, imprimir sin índice  
noindex=precio_promedio.values.tolist()  
from tabulate import tabulate #si  no tienes tabulate, instala con: pip install tabulate
print("\nDataFrame sin índice original:")
print(tabulate(noindex, headers=list(precio_promedio.columns), tablefmt='grid'))

#Nombrar columna index e inicar desde 1
df_nuevo=precio_promedio.copy()
df_nuevo.index=range(1, len(df_nuevo) + 1) # type: ignore
df_nuevo.index.name='ID' # type: ignore
print("\nDataFrame con índice comenzando en 1:")
print(df_nuevo.head())

#Visualizar los datos con un gráfico de barras
precio_promedio.plot(kind='bar', x='Categoría', y='Precio Unitario', legend=False, color='skyblue',edgecolor='black',title='Precio Unitario Promedio por Categoría')
plt.xticks(rotation=45)
plt.ylabel('Categoría')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Grafica con caterias dentro de las barras
fig,ax = plt.subplots()
barras= ax.bar(precio_promedio.index, precio_promedio['Precio Unitario'], color=['skyblue','green'], edgecolor='black')

#incluir etiquetas de valor encima de cada barra
for i, barra in enumerate(barras):
    categoria=precio_promedio['Categoría'][i]
    altura=barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/0, altura/1, categoria, ha='center', va='center', fontsize=8, rotation=90,color='black')
    
#oculatar lavel los eje X
ax.set_xticks([])

plt.title('Precio Unitario Promedio por Categoría con Etiquetas')
plt.ylabel('Precio Unitario')
plt.tight_layout()
plt.show()