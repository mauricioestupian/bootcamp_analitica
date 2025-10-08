import datetime as data
import dateutil.relativedelta as rela #pip install python-dateutil - python -m pip install python-dateutil

f1= data.date(2024,10,5)
f2= data.date(2025,11,25)

diferencia=rela.relativedelta(f2,f1)
print(f" años: {diferencia.years}")
print(f" mese: {diferencia.months}")
print(f" dias: {diferencia.days}")