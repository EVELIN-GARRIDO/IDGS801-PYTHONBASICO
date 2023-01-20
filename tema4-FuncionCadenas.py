cadena = "Universidad Tecnológica de León"

print(cadena)
print(cadena.lower())
print(cadena.upper())
print(cadena.title())
print(cadena.find("de")) # Buscar una cadena dentro de otra cadena
print(cadena.count("a")) # Contabilizar la cantidad de cractere que hay en una cadena

textoFinal = cadena.replace("a", "4")
print(textoFinal)

cadenaNueva = cadena.split(" ") # Generar una lista a partir de cada palabra de la cadena
print(cadenaNueva)