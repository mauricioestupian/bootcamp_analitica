productos=[
    {"nombre":"Manzana","categoria":"fruta","valor":500},
    {"nombre":"Pan rollo", "categoria":"pan","valor":600},
    {"nombre":"Pera", "categoria":"fruta","valor":200},
    {"nombre":"Espinaca", "categoria":"Verdura","valor":500},
    {"nombre":"Guineo", "categoria":"fruta","valor":300},
    {"nombre":"Zanahoria", "categoria":"Verdura","valor":500}   
]
#Agrupar productos por categoria

agrupados={}
for producto in productos:
    cat=producto["categoria"]
    if cat not in agrupados:
        agrupados[cat]=[]
    agrupados[cat].append([producto["nombre"],producto["valor"]])

print(agrupados)

def ordenar_por_valor_desc(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j][1] < lista[j + 1][1]:
                # Intercambiar si el siguiente es mayor
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Aplicar ordenamiento a cada categoría
for categoria in agrupados:
    agrupados[categoria] = ordenar_por_valor_desc(agrupados[categoria])

print(agrupados)