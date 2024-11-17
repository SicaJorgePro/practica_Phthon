def crear_lista():
  while True:  # Bucle para permitir al usuario ingresar la lista varias veces
    try:
        # Solicitar al usuario que ingrese lenguajes separados por comas
        lenguajes_input = input("Ingrese una lista de lenguajes de programación separados por comas: ")
        
        # Crear la lista y eliminar los espacios innecesarios alrededor de cada lenguaje
        lenguajes_lista = [lenguaje.strip().lower() for lenguaje in lenguajes_input.split(',')]
        
        # Si la lista está vacía después de limpiar los espacios, se lanza un error
        if not any(lenguajes_lista):
            raise ValueError("La lista de lenguajes no puede estar vacía.")
            
        
        # Validar que cada lenguaje no sea un número
        for lenguaje in lenguajes_lista:
            if lenguaje.isdigit():  # Si es solo un número, lo rechazamos
                raise ValueError(f"Error: '{lenguaje}' no es un lenguaje válido. Los números no están permitidos.")
                       
        # Si no se encontró ningún número, la lista es válida
        return lenguajes_lista  # Devolver la lista válida     
        
    except ValueError as e:
        print(f"Error: {e}")
        continue
 
def agregar_lenguaje(lista_lenguajes):
    try:
        while True:
            # Solicitar al usuario que ingrese el nuevo lenguaje
            nuevo_lenguaje = input("Ingrese el nuevo lenguaje que desea agregar: ").strip()
            
            # Validar que el lenguaje no esté vacío
            if not nuevo_lenguaje:
                print("Error: No ingresó un lenguaje válido. Por favor ingrese un lenguaje no vacío.")
                
            elif nuevo_lenguaje.isdigit():
                print("Error: No puede ingresar un número como lenguaje. Por favor ingrese un lenguaje válido.")    
                
            else:
                lista_lenguajes.append(nuevo_lenguaje.lower())
                break  # Salir del bucle cuando se ingresa un lenguaje válido    
          
        return lista_lenguajes
      
    except ValueError as e:
        print(f"Error: {e}")
        return lista_lenguajes

def eliminar_lenguaje(lista_lenguajes):
    try:
        while True:
            lenguaje_a_eliminar = input("Ingrese el lenguaje a eliminar: ").strip()
            
            # Validar que el lenguaje no esté vacío
            if not lenguaje_a_eliminar:
                print("Error: No ingresó un lenguaje válido. Por favor ingrese un lenguaje no vacío.")
                
            else:
                break  # Salir del bucle cuando se ingresa un lenguaje válido
              
        # Convertir la entrada del lenguaje a eliminar a minúsculas
        lenguaje_a_eliminar = lenguaje_a_eliminar.lower()
        
        # Intentar eliminar el lenguaje de la lista
        if lenguaje_a_eliminar in lista_lenguajes:
            lista_lenguajes.remove(lenguaje_a_eliminar)
            print(f"El lenguaje '{lenguaje_a_eliminar}' ha sido eliminado de la lista.")
        else:
            print(f"El lenguaje '{lenguaje_a_eliminar}' no se encuentra en la lista, Nada se elimino.")
      
        return lista_lenguajes
      
    except ValueError as e:
        print(f"Ocurrió un error inesperado: {e}")
        return lista_lenguajes  # Retorna la lista sin cambios en caso de error
      
    
def encontrar_mas_extenso(lista_lenguajes):
    try:
        # Verificar si la lista no está vacía
        if not lista_lenguajes:
            raise ValueError("La lista de lenguajes está vacía.")
        
        # Usamos la función max() con key=len para encontrar el lenguaje más largo
        lenguaje_extenso = max(lista_lenguajes, key=len)
        
        # Retornar el lenguaje más extenso
        return lenguaje_extenso
      
    except ValueError as e:
        print(f"Error: {e}")
        return None
      

# Crear la lista inicial de lenguajes

lenguajes = crear_lista()

if lenguajes:  # Solo continuar si la lista no está vacía
  
    # Mostrar la lista de lenguajes 
    print("Lista de lenguajes antes de agregar el nuevo lenguaje:", lenguajes)

    # Llamar a la función para agregar el nuevo lenguaje
    lenguajes_actualizados = agregar_lenguaje(lenguajes)

    # Mostrar la lista actualizada 
    print("Lista de lenguajes después de agregar el nuevo lenguaje:", lenguajes_actualizados)

    # Llamar a la función para eliminar el lenguaje
    lenguajes_finales = eliminar_lenguaje(lenguajes_actualizados)

    # Mostrar la lista final 
    print("Lista de lenguajes después de eliminar el lenguaje:", lenguajes_finales)

    # llamar la funcion y Encontrar el lenguaje más extenso 
    lenguaje_extenso = encontrar_mas_extenso(lenguajes_finales)

    # Mostrar el lenguaje más extenso
    if lenguaje_extenso:
        print(f"El lenguaje más extenso (con el nombre más largo) es: {lenguaje_extenso}")
else:
    print("No se pudo crear la lista de lenguajes. Terminando el programa.")

