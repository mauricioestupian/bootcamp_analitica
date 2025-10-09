import pandas as pd

#Leer json
df = pd.read_json("data/data.json")
print("DataFrame original:")
print(df)

#Filtro por fecha
df["fecha_Nac"]=pd.to_datetime(df["fecha_Nac"],format=('%d/%m/%Y'))
df_filtrado= df[df["fecha_Nac"].between('1998-01-01','2001-01-01') ]
print("Nuevo data frame por fecha")
print(df_filtrado)