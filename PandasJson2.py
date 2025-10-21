import pandas as pd

#Carga archivo json
df=pd.read_json("data/json2.json")
print("dataframe original")
print(df)

#seccionar o dividir grupos por dataframe separados para luego unirlos
df1 = pd.json_normalize(df["grupo1"].tolist())#para versiones anteriores de python 13.13
df2 = pd.DataFrame(df["grupo2"].tolist())#Vesiones 13.13 en adelante sin el .tolist()
n= 5
print(f"datos 1 {n}")
print(df1)
print("datos 2")
print(df2)

#se unifica la data para que se muestre en un solo conjunto de datos
df_final=pd.concat([df1,df2],axis=0,ignore_index=True)

print("Validacion data duplicada:")
print(df_final.duplicated())
#Suamtoria de duplicados
print("total de datos duplicados")
print(df_final.duplicated().sum())

#verificar duplicados por columna
print(df_final)
print(df_final.duplicated(subset=["Id","Nombre"]))

#dataframe sin duplicados
df_limpio=df_final.drop_duplicates(keep="last")
print(df_final)
print("Dataset sin duplicados:")
print(df_limpio)

#Suma edades 
print(df_final)
#Convertir Texto en Numero
df_final["Edad"]=pd.to_numeric(df_final["Edad"],errors="raise")
print(f"suma edades {df_final["Edad"].sum()}")
