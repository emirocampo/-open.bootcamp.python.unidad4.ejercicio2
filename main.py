print("PROGRAMA QUE HALLA LOS NUEMEROS IMPARES EN UN RANGO DADO")
print("digite desde donde desea iniciar")
inicio = int(input())
print("digite hasta donde desea llegar")
fin = int(input())
vector = []
for x in range(inicio,fin):
    if(x % 2 != 0):
        vector.append(x)

print(vector)