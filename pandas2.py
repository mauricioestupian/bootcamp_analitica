import pandas as pa
datos= {
    'Nombre':['Juan', 'Ana','Milena'],
    'edad':[15,25,32],
    'ciudad':['Bogota','Cali','Medellin']
}

dataf= pa.DataFrame(datos)
print(dataf)

print(dataf['edad'])

print(dataf.loc[1])
print(dataf.iloc[-1])

filtro= dataf[dataf['edad']>=25]
print(filtro)