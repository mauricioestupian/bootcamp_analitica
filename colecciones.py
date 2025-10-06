persona={
    "nombre":"Mauricio",
    "edad":42,
    "ciudad":"Chiquinquirá"
}

print (persona["edad"])
persona["nombre"]="Juanito"
print(persona)
persona["Profesion"]="Ingeniero"
print(persona)
print(persona.keys())
data2={
    "estrato":2,
    "eps":"Sanitas",
    "comidas":["pastas","Mexicana"],
    "Profesion":"Carnicero",
    "dirección":{
        "calle":"carrera",
        "numero":"75-26",
        "complemento":"Apto 602"
    }
}
persona.update(data2)
print(persona)
print(f"Nombre: {persona["nombre"]} apartamento: {persona["dirección"]}")
print(f"Nombre: {persona["nombre"]} apartamento: {persona["dirección"]["complemento"]}")
print(f"segunda comida {persona["comidas"]}")
print(f"segunda comida {persona["comidas"][1]}")
