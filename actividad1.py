# Declarar variable
print("Tabla de multiplicar")

num = int(input("Ingrese el numero del cual desee obtener su tabla de multiplicar: "))

def realizarTablaMultiplicar(x):
    for i in range(1, 11):
        resultado = x * i
        print(x, " * ", i, " = ", resultado)

realizarTablaMultiplicar(num)