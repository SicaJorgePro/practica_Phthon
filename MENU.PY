import os
# LISTA 
Lista_LengujeProgr=["Python","Java","C","C++","JavaScript","Ruby","Go","PHP"]
Lista_SistemaOper=["Windows","Linux","macOS","Ubuntu","Fedora","Debian","Arch Linux"]
Lista_StacksTegnologicos=[
    "MERN (MongoDB, Express.js, React, Node.js)", 
    "MEAN (MongoDB, Express.js, Angular, Node.js)", 
    "LAMP (Linux, Apache, MySQL, PHP)", 
    "LEMP (Linux, Nginx, MySQL/MariaDB, PHP/Python)", 
    "JAMstack (JavaScript, APIs, Markup)", 
    "Serverless (AWS Lambda, API Gateway, DynamoDB, etc.)", 
    "Spring (Spring Boot, Spring MVC, Hibernate, Java)", 
    "Django Stack (Django, Python, PostgreSQL, Nginx)", 
    "Ruby on Rails (Ruby, Rails, PostgreSQL, Redis)", 
    "Flutter (Dart, Flutter SDK)", 
    "Android Development (Java/Kotlin, Android SDK, SQLite)"]

#  funciones de opciones 
def opcion1():
   os.system('cls')
   print("Lenguajes de Programación\n")
#    crea un lista nueva todo en minuscula
   lenguajes=[lenguaje.upper() for lenguaje in Lista_LengujeProgr]
   for lenguaje in lenguajes:
     print(lenguaje)
     
   input("\npresione enter para volver al <Menú>")

def opcion2():
   os.system('cls')
   print("Sistema Operativo\n")
   for lenguaje in Lista_SistemaOper:
       print(lenguaje)
   input("\npresione enter para volver al <Menú>")
   
def opcion3():
   os.system('cls')
   print("Stacks Tecnológicos\n")
   for lenguaje in Lista_StacksTegnologicos:
       print(lenguaje)
   input("\npresione enter para volver al <Menú>")
  
def menu():
    while True:
            os.system('cls')
            print("Menú de Opciones\n")
            print("1- Visualizacion Lenguaje de Programacion")
            print("2- Visualizacion Sistemas Operativos     ")
            print("3- Visualizacion Stacks Tegnológicos     ")
            print("0- Salir\n                               ")
            opcion=input ("Eliga la opcion:")
            if opcion == '1':
                    opcion1()
            elif opcion == '2':
                    opcion2()
            elif opcion == '3':
                   opcion3()
            elif opcion == '0':
                    break
                            
            else:
                    print("\nOpción inválida. Por favor, ingresa una opción entre 1 y 3, 0(cero)para salir ")
                    input("\npresione enter")
                    
menu()             
