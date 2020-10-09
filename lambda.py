def filtro(elemento):
    return elemento >=10

filtro_2 = lambda arg: arg >= 10

numeros = [1, 10, 15, 25, 4, 35, 2]

for item in filter(filtro, numeros):
    print(item)