import pandas as pa

serie= pa.Series([10,20,30], index=["A",'B','C'])
print(serie)
print(serie['B'])

serie2= pa.Series([10,20,30])
print(serie2)
print(serie2[2])
print(serie.mean())
serie3= serie+5
print(serie3)