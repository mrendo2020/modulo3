dict_countrY = {

"es": "España",
"ec": "Ecuador",
"mx": "Mexico",
"pe": "Peru",
"co": "Colombia",
"ve": "Venezuela"
}

valid_codes = ["ec", "mx", "es"]

paises = [val for key,val in dict_countrY.items() if key in valid_codes]

print(paises)
