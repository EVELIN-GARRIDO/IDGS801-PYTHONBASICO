def tem():
    print("¡Hola desde my_modulo.py!")

def tem2():
    print("Adiós desde my_modulo.py!")

def main():
    print("¡Hola desde main!")
    tem()
    tem2()

# Estructura para poder establecer el ciclo de la ejecucion:
if __name__ == '__main__':
    main()
