'''
Ejercicios bootcamp analisis de datos
semana 2 sesión 3
'''
import random;

frutas=["uva","pera","manzana","banano","fresa"]
print(frutas[0])#Accede a primer elemento de la lista
print(frutas[-1]) #Accede al ultimo elemento de la lista
print("_____________")
#recorer toda la lista elemento por elemento
for elemento in frutas:
    print(elemento)
#eliminar manzana???
print("________________")
#del frutas[2]
print(frutas)
if "manzana" in frutas:
    print("Manzana se encuentra en la lista")
else:
    print("Manzana NO se encuentra en la lista")
print("________________")
#Contar elementos de lista 
print(f"La lista de frutas contiene {len(frutas)} elementos")
#contar elmentos de la lista con nombre menor a 5 letras
f_corta = [f for f in frutas if len(f)<= 4]#<5

f_corta2=[]
for f in frutas:
    if len(f)<= 4:
        f_corta2.append(f)

print(f"La lista cuenta con {len(f_corta)} frutas con nombres cortos") 
print(f" las frutas con nombres cortos son: {f_corta}")
n=random.randint(1,10)#genera numeros aleatorios enre 1 y 10
print(f"número aleatorio es {n}")

#Crear una lista de 15 numeros generados aleatoriamente  entre 1 y 50y mostrar en una nueva lista los paress e impares; adicional si el numero 32 se encuentra entre la