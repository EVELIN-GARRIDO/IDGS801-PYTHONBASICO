# Concatenacion de cadenas
texto1 = "Hola"
texto2 = "Mundo!!"
textoFinal = texto1 + " " + texto2

print(textoFinal)

print("El saludo es: %s %s "% (texto1, texto2))

cadena = "Saludar dos: {1} {0} ".format(texto1, texto2)
print(cadena)

cadena = "Saludar dos: {x} {y} ".format(x = texto1, y = texto2)
print(cadena)