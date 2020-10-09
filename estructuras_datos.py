from typing import Dict

secuencia = [1, 3, 5, 7]
print(secuencia[2])
secuencia[2] = 10
print(secuencia[2])
secuencia.append(22)
print(secuencia[-1])
valor_eliminado = secuencia.pop(3)
print(secuencia, " ", valor_eliminado)
paises = [
    "España",
    "Ecuador",
    "Mexico",
    "Peru",
    "Colombia",
    "Venezuela"
]
for recorrer in paises:
    print(recorrer)
for recorre in paises:
    print(recorrer)
print( "####### Tuplas#####3")
claves = ("123", "541")
for item in claves:
    print(item)
print("####### Tuplas#####3")

dict_countrY = {

"es": "España",
"ec": "Ecuador",
"mx": "Mexico",
"pe": "Peru",
"co": "Colombia",
"ve": "Venezuela"
}
print(dict_countrY.get("es"))

for key, value in dict_countrY:
    print(key, "; ", value)
    print(dict_countrY.keys())
    print(dict_countrY.values())

if "ec" in dict_countrY.keys():
    print(">> ", dict_countrY.get("ec"))

res = {
    "warning": "Mensaje de alerta",
    "values": {
        "id": 158,
        "name": "XXFGTX NAME",
        "price": 1245.58,


    },

}

for key, value in res.items():
    print(key, "; ", value)
    if "values" == key:
        print(value["id"])
        print("",format(value.get("id")))
        print("id: {} - name: {}".format(value.get("id"),value.get("name")))
