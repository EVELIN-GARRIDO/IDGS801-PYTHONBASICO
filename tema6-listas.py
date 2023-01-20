# Crear listas
nombres = ["Juan", "Mario", "Laura"]
numeros = [1, 2, 3, 4, 5]
datos = [1, 2.5, "Mario", True]

# Sustituir Juan por Roberto en la lista
nombres[0] = "Roberto"

print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

nombres.append("Dario") # Agregar elementos nuevos a la list
print(nombres)

nombres.insert(2, "Maria")
print(nombres)

nombres.extend(["checha", 2, 23, 5])
print(nombres)

nombres.remove("checha")
print(nombres)

# Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

n = ["juam"]
n2 = n * 5
print(n2)

del nombres[2]
print(nombres)