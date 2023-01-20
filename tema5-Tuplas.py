# Una tupla no es reemplazable, no emite cambios, se mantiene estatica

tupla = (1, 2, 3)
print(tupla)
print(type(tupla)) # Imprimir el tipo de dato

tupla2 = (7, "Roberto", True, 23.8, 16 + 7j)
print(tupla2)
print(type(tupla2))

print(tupla2[1]) # Imprimir el elemento de la tupla en la poscion especificada

print(tupla2[4]) # Mostrar el ultimo elemento de la tupla
print(tupla2[-1]) # Mostrar el ultimo elemento de la tupla
print(tupla2[0:3])
print(tupla2[:3])
print(tupla2[3:])

a, b, c = tupla
print(a)
print(b)
print(c)

tuplaN = tupla + tupla2
print(tuplaN)
print(tupla.count(2))

# No se puede cambiar el valor de una tupla
tupla[2] = 23 