from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def pedir_numeros():
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    return num1, num2

def pedir_numeros_avanzados():
    numeros = input("Ingresa los números separados por espacio: ")
    numeros = list(map(float, numeros.split()))
    print("Resultado:", suma_avanzada(numeros))
    
def menu():
    menu = """
=================================
==== Calculadora Open Source ====
=================================
1. Sumar 2 números
2. Restar 2 números
3. Multiplicar 2 números
4. Dividir 2 números
5. Sumar muchos números, separados por comas
6. Salir
"""
    print(menu)



def operar(operacion):
    if operacion < '5' and operacion > '0':
        num1, num2 = pedir_numeros()
        if operacion == '1':
            return sumar(num1, num2)
        elif operacion == '2':
            return restar(num1, num2)
        elif operacion == '3':
            return multiplicar(num1, num2)
        elif operacion == '4':
            return dividir(num1, num2)
    elif operacion == '5':
        pedir_numeros_avanzados()
        


    

def iniciar_calculadora():
    while True:
        menu()
        opcion = input("Elige una opción: ")
        if opcion in ['1', '2', '3', '4', '5']:
            resultado = operar(opcion)
            if resultado is not None:
                print("Resultado:", resultado)
                otro = input("Para realizar otra operación, presiona 'Q'").lower()
                if otro == "q":
                    pass
                else:
                    break
                
        elif opcion == '6':
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

if __name__ == "__main__":
    iniciar_calculadora()