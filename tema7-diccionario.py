miDiccionario = {"Matricula": "12345", "Nombre": "Dario", "edad": 23}

print(type(miDiccionario))
print(miDiccionario)

miDiccionario["Nombre"] = "Panfilo"
print(miDiccionario)
print(miDiccionario["edad"])
print(miDiccionario.values())
print(miDiccionario.keys())