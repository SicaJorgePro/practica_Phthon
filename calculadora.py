def calcular(num_a, num_b, operacion):
    try:
        # Comprobamos la operación y realizamos la correspondiente
        if operacion == "suma":
            resultado = num_a + num_b
        elif operacion == "resta":
            resultado = num_a - num_b
        elif operacion == "multiplicacion":
            resultado = num_a * num_b
        elif operacion == "division":
            if num_b == 0:
                raise ValueError("Error: No se puede dividir por cero.")
            resultado = num_a / num_b
        else:
            raise ValueError("Error: Operación no válida. Las opciones son 'suma', 'resta', 'multiplicacion' o 'division'.")
        
        # Retornar el resultado de la operación
        return resultado

    except ValueError as e:
        print(f"Error: {e}")
        return None  # Retorna None si hay un error de valor
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None  # Retorna None en caso de cualquier otro error

# Función principal para interactuar con el usuario
def solicitar_numero(prompt):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
def main():
    try:
        # Solicitar al usuario los dos números con la validación mejorada
        num_a = solicitar_numero("Ingrese el primer número: ")
        num_b = solicitar_numero("Ingrese el segundo número: ")

        # Solicitar al usuario qué operación desea realizar
        print("Operaciones disponibles: suma, resta, multiplicacion, division")
        
        while True:  # Bucle para pedir la operación hasta que sea válida
                operacion = input("Ingrese la operación que desea realizar: ").lower()
                
                # Verificar si la operación ingresada es válida
                if operacion in ["suma", "resta", "multiplicacion", "division"]:
                    break  # Salir del bucle si la operación es válida
                else:
                    print("Operación no válida. Por favor ingrese una operación válida: suma, resta, multiplicacion o division.")
                    
        # Llamar a la función calcular
        resultado = calcular(num_a, num_b, operacion)

        # Mostrar el resultado
        if resultado is not None:
            print(f"El resultado de la {operacion} es: {resultado}")
        else:
            print("No se pudo realizar la operación.")
    except ValueError:
        print("Error: Por favor ingrese números válidos.")

# Ejecutar el programa
main()
