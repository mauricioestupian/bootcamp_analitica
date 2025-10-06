agrupados={}
for producto in productos:
    cat=producto["categoria"]
    if cat not in agrupados:
        agrupados[cat]=[]
    agrupados[cat].append([producto["nombre"],producto["valor"]])

print(agrupados)