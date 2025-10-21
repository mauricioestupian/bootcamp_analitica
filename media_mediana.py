import statistics as st
import numpy as np
m=[2,4,8]
for c in m:
    n = int(input("Ingrese un número: "))
    m.append(n)
media = sum(m) / len(m)
print(f"La media de los números ingresados es: {media}")
mediana = sorted(m)[len(m) // 2]
print(f"La mediana de los números ingresados es: {mediana}")

#uso de la libreria statistics
media_st = st.mean(m)
mediana_st = st.median(m)
print(f"La media usando statistics es: {media_st}")
print(f"La mediana usando statistics es: {mediana_st}")

#uso de la libreria numpy
media_np = np.mean(m)
mediana_np = np.median(m)
print(f"La media usando numpy es: {media_np}")
print(f"La mediana usando numpy es: {mediana_np}")
round(media_np,2)
