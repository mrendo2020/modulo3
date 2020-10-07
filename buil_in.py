dict_countrY = {

"es": "España",
"ec": "Ecuador",
"mx": "Mexico",
"pe": "Peru",
"co": "Colombia",
"ve": "Venezuela"
}
paises = [
    "España",
    "Ecuador",
    "Mexico",
    "Peru",
    "Colombia",
    "Venezuela"
]

ordenado = sorted(dict_countrY.items())
print(ordenado)
ordenado = sorted(paises, reverse=True)
print(ordenado)