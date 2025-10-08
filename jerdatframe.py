import pandas as pd
datos= {
    'Producto':['Manzana', 'banana','Cereza'],
    'Precio':[2.5,1.8,3.0],
    'Cantidad':[10,15,8]
}
df = pd.DataFrame(datos)
print(df.head(2))
print(df.tail(2))
df["P_Total"]=df['Precio']*df['Cantidad']
print("La nueva serie es:")
print(df)
print(f"La suma total de los P_Total es: {df["P_Total"].sum()}")

df_ordenado = df.sort_values(by='Precio')
print("el data Frame ordenado es:")
print(df_ordenado)