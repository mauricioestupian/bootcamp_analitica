import datetime as data
fecha_llegada= data.datetime.now()
print(f"La fecha y hora de llegada: {fecha_llegada}")

print(fecha_llegada.strftime("%Y-%m-%d"))

f1=data.date(2024,10,5)
f2=data.date(2025,10,25)
print(f"total de dias: {f2-f1}")
diferencia= f2-f1
print(f"total de dias: {diferencia.}")