#importar la librería pandas
import pandas as pd
import matplotlib.pyplot as plt

#Cargar los archivos .csv desde URLs
url="https://drive.google.com/uc?export=download&id=1JS7jkpbWMaOlpsh_7Q6P8nue1U9aiM-C"
df=pd.read_csv(url)
print("Datos ventas:")
print(df.head(10))  

#Agrupar los datos por la columna "Categoría"
precio_promedio=df.groupby("Categoría")['Precio Unitario'].mean().round(2).reset_index()
print("\nPrecio Unitario promedio por Categoría:")
precio_promedio=precio_promedio.sort_values(by='Categoría', ascending=True)#Ordenar por Categoría
print(precio_promedio)

#Visualizar los datos con un gráfico de barras
precio_promedio.plot(kind='bar', x='Categoría', y='Precio Unitario', legend=False, color='skyblue',edgecolor='black',title='Precio Unitario Promedio por Categoría')
plt.xticks(rotation=45)
plt.ylabel('Categoría')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Grafica con caterias dentro de las barras
fig,ax = plt.subplots()
barras= ax.bar(precio_promedio.index, precio_promedio['Precio Unitario'], color='skyblue', edgecolor='black')

#incluir etiquetas de valor encima de cada barra
for i, barra in enumerate(barras):
    categoria=precio_promedio['Categoría'][i]
    altura=barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura/2, categoria, ha='center', va='center', fontsize=8, rotation=90,color='black')
    
#oculatar lavel los eje X
ax.set_xticks([])

plt.title('Precio Unitario Promedio por Categoría con Etiquetas')
plt.ylabel('Precio Unitario')
plt.tight_layout()
plt.show()