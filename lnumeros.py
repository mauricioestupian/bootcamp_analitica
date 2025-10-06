import random
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

num=[]
for i in range(15):
    num.append(random.randint(1,50))
print(num)
print(sum(num))
print(max(num))
print(min(num))
prom=sum(num)/len(num)
print(prom)
num2=num[::-1]
print(num[::-1])
print(num[-1])
print(set(num))
l2=set(num)
num.sort()
print(f"Numeros ordenados {num}")
num.sort(reverse=True)
print(f"Descendente: {num}")
print(num)





import numpy 
arreglo=[1,2,3]
print(arreglo)
Lista=[1,2,3]
my_array= numpy.array(Lista)
print(f"Lista {Lista}")
print(f"arreglo {my_array}")
b=Lista + my_array
print(f"combinar {b}")
array_lista = my_array.tolist()
union = array_lista + Lista
print(f"arreglo to list {array_lista}")
print(f"union de las listas {union}")