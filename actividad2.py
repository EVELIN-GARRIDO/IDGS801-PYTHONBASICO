# Limpiar líneas de consola
import os

class OperacionesBasicas:
    # Propiedades de la clase
    num1 = 0
    num2 = 0
    res = 0

    # Constructor de la clase
    def __init__(self):
        pass

    # Metodos de la clase
    def suma(self, a, b):
        self.num1 = a
        self.num2 = b
        self.res = self.num1 + self.num2
        print("La suma de: {} + {} = {}".format(self.num1, self.num2, self.res))

    def resta(self, a, b):
        self.num1 = a
        self.num2 = b
        self.res = self.num1 - self.num2
        print("La resta de: {} - {} = {}".format(self.num1, self.num2, self.res))

    def multiplicacion(self, a, b):
        self.num1 = a
        self.num2 = b
        self.res = self.num1 * self.num2
        print("La multiplicación de: {} x {} = {}".format(self.num1, self.num2, self.res))

    def division(self, a, b):
        self.num1 = a
        self.num2 = b
        self.res = self.num1 / self.num2
        print("La división de: {} / {} = {}".format(self.num1, self.num2, self.res))


def main():    
    while True: 
        print("""Bienvenido, elige la operación que quieras llevar a cabo ingresando su correspondiente número de acuerdo al siguiente menú:
            1.- Suma
            2.- Resta
            3.- Multiplicacion         
            4.- Division
            5.- Salir""")

        opc = int(input("Ingrese la operación que desea llevar a cabo: "))
        obj = OperacionesBasicas()

        if(opc == 1):
            os.system('cls')
            print("------- Ha seleccionado hacer una suma -------")
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            obj.suma(num1, num2)
            break

        elif(opc == 2):
            os.system('cls')
            print("------- Ha seleccionado hacer una resta -------")
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            obj.resta(num1, num2)
            break

        elif(opc == 3):
            os.system('cls')
            print("------- Ha seleccionado hacer una multiplicación -------")
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            obj.multiplicacion(num1, num2)
            break

        elif(opc == 4):
            os.system('cls')
            print("------- Ha seleccionado hacer una división -------")
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese el segundo numero: "))
            obj.division(num1, num2)
            break

        elif(opc == 5):
            print("Saliendo del menú de operaciones...")
            exit()
        
        else:
            print("La opción que acaba de ingresar es incorrecta, por favor, vuelva a intentarlo nuevamente.")
            main()
            break

if __name__ == '__main__':
    main()