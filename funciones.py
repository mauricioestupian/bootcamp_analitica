'''def suma(a,b):
    sum=a+b
    return sum

print(suma(8,10))
print(suma(2,4))
print(suma(6,5))


def saluda(nom):
    return print(f"hola buenos dias {nom}")

saluda("Miguel")
saluda("Juan")
saluda("Paola")

def cuadrado(n):
    return n ** 2

numero= cuadrado(2)
print(f"el resultado es: {numero}")'''

def cambia(d,o):
    p="hola"
    m="otra cosa"
    r=[]
    for i in d:
        if i is None:
            r.append(o)
        else:
            r.append(i)     
    return print(f"p es= {p}, m es {m}, r es:{r}")

datos=[1,None,2,None,3]
print(f"cabia normal {cambia(datos,0)}")

cambia2 = lambda datos,p: [p if i is None else i for i in datos]
print(f"cambia con Lambda {cambia2(datos,0)}")

suma2 = lambda x,y:x+y
print(f"la suma de 4 + 1 = {suma2(4,1)}")

#numeros=[10,8,45,26,7]


