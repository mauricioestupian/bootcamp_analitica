prom=0
for i in range(3):
    n1 = int(input(f"Ingrese nota {i+1}: "))
    while n1 >5 or n1 < 0:
        n1 = int(input(f"Ingrese nota {i+1}: "))
    #prom = prom + n1
    prom += n1
prom = prom / 3
if prom >= 3:
    print(f"Aprobado nota {prom}")
else:
    print(f"Reprobado nota {prom}")
    
