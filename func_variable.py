import time, os

yel = "\033[33m" # [Amarillo] Bloques (print, input, etc)
syel = "\033[93m" # [Amarillo brillante] Parentesis
cya = "\033[36m" # [Cyan] Variables
sgrn = "\033[92m" # [Verde Brillante] Numeros
orn = "\033[38;5;94m" # [Naranja] Texto
b_border = '\033[34m' # Borde azul
r_border = '\033[31m' # Borde rojo
g_border = '\033[32m' # Borde verde
reset = '\033[0m' # Resetear colores
grs = '\033[90m' # Gris oscuro

def func_variable(rounded_box):
    os.system("cls")
    print(" __      __        _       _     _            ")
    print(" \ \    / /       (_)     | |   | |           ")
    print("  \ \  / /_ _ _ __ _  __ _| |__ | | ___  ___  ")
    print("   \ \/ / _` | '__| |/ _` | '_ \| |/ _ \/ __| ")
    print("    \  / (_| | |  | | (_| | |_) | |  __/\__ \ ")
    print("     \/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/ ")
    print()
    print("[1] ¿Que son?")
    print("[2] Tipos de datos")
    print("[3] Variables multiples")
    print("[4] Variables iguales")
    print("[5] Lista de objetos")
    print("[6] Suma de variables")
    print("[7] Variables globales")
    print("[8] Salir")
    print()
    option = input("> ")
    if option == "1":
        os.system("cls")
        rounded_box([f"{grs}Una variable es un contenedor para almacenar datos que se pueden usar en un programa.",
                     f"{grs}Puedes pensar en una variable como una etiqueta para un valor"],g_border)
        print()
        time.sleep(1)
        rounded_box([f"{syel}'{cya}Name{syel}' {reset}= {syel}({sgrn}Value{syel})"], r_border)
        print()
        time.sleep(1)
        rounded_box([f"{cya}x {reset}= {sgrn}10",
                     f"{cya}y {reset}= {orn}'Hello'",
                     "",
                     f"{yel}print{syel}({cya}x{reset}, {cya}y{syel})",
                     f"{grs}# Nos dará '10 Hello', ya que hay un espacio entre x e y"], b_border)
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "2":
        os.system("cls")
        rounded_box([f"{grs}En Python hay 3 tipos de datos:",
                     f"{grs}int = Número entero",
                     f"{grs}str = Cadena de texto",
                     f"{grs}float = Número decimal"], g_border)
        time.sleep(1)
        print()
        rounded_box([f"{syel}int{syel}({orn}Value{syel})",
                     f"{syel}str{syel}({orn}Value{syel})",
                     f"{syel}float{syel}({orn}Value{syel})"], r_border)
        time.sleep(1)
        print()
        rounded_box([f"{cya}x {reset}= {sgrn}10",
                     "",
                     f"{yel}print{syel}({sgrn}int{syel}({cya}x{syel}))",
                     f"{grs}# Nos dará 10",
                     "",
                     f"{yel}print{syel}({sgrn}str{syel}({cya}y{syel}))",
                     f"{grs}# Nos dará '10'",
                     "",
                     f"{yel}print{syel}({sgrn}float{syel}({cya}z{syel}))",
                     f"{grs}# Nos dará 10.0"], b_border)
        time.sleep(1)
        input("Presiona Enter para continuar...")
        
        os.system("cls")
        rounded_box([f"{grs}Puedes sacar el tipo de dato de una variable",
                        f"{grs}usando type()"], g_border)
        time.sleep(1)
        print()
        rounded_box([f"{yel}type{syel}({sgrn}Value{syel})"], r_border)
        time.sleep(1)
        print()
        rounded_box([f"{cya}x {reset}= {orn}'10'",
                     f"{cya}y {reset}= {sgrn}'Hello'",
                     "",
                     f"{yel}print{syel}({sgrn}type{syel}({cya}x{syel}))",
                     f"{grs}# Nos dará <class 'int'>",
                     "",
                     f"{yel}print{syel}({sgrn}type{syel}({cya}y{syel}))",
                     f"{grs}# Nos dará <class 'str'>"], b_border)
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "3":
        print("Puedes asignar multiples variables en una sola linea")
        time.sleep(1)
        print()
        print("a, b, c = 5, 3.2, 'Hello'")
        print("print(a)  --> Nos dará 5")
        print("print(b)  --> Nos dará 3.2")
        print("print(c)  --> Nos dará 'Hello'")
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "4":
        print("Puedes asignar multiples variables con el mismo valor")
        time.sleep(1)
        print()
        print("x = y = z = 'Same'")
        print("print(x)  --> Nos dará 'Same'")
        print("print(y)  --> Nos dará 'Same'")
        print("print(z)  --> Nos dará 'Same'")
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "5":
        print("Puedes asignar multiples variables en una sola linea")
        time.sleep(1)
        print()
        print("fruits = ['apple', 'banana', 'cherry']")
        print("a, b, c = fruits")
        print("print(a)  --> Nos dará 'apple'")
        print("print(b)  --> Nos dará 'banana'")
        print("print(c)  --> Nos dará 'cherry'")
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "6":
        print("Puedes sumar variables")
        time.sleep(1)
        print()
        print("x = 5")
        print("y = 8")
        print("z = 'hola'")
        print("print(x + y)  --> Nos dará 13")
        print("print(z + z + str(x))  --> Nos dará 'hola hola 5' (No se puede sumar un str con un int)")
        print("print(x, y, z)  --> Nos dará 5 8 hola")
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "7":
        os.system("cls")
        print("Si determinas una variable fuera de una función,")
        print("podras usarlo en cualquier parte del codigo")
        print()
        time.sleep(2)
        print("Ejemplo:")
        print("x = 'Fantastico'")
        print("def myfunc()")
        print("  print('Python es' + x)")
        print("")
        print("myfunc()")
        print()
        print()
        input("Presiona Enter para continuar...")
        os.system("cls")
        print("Con esta información, podriamos hacer dos variables con el mismo nombre, una")
        print("dentro de una funcion y otra global")
        print()
        time.sleep(2)
        print("Ejemplo:")
        print("x = Horrible")
        print()
        print("def myfunc()")
        print("   x = Maravilloso")
        print("   print('Python es ' + x)   # Este sacará Maravilloso, ya que la variable x dentro de la funcion es Maravilloso")
        print()
        print("myfunc()")
        print()
        print("print('Python es ' + x)   # Este sacará Horrible, ya que la variable x es global")
        print()
        input("Presiona Enter para continuar...")
        os.system("cls")
        print("Entonces, para poder usar una variable global dentro de una función hacemos:")
        print()
        time.sleep(2)
        print("def myfunc()")
        print("   global x")
        print("   x = 'Maravilloso'")
        print()
        print("myfunc()")
        print("")
        print("print('Python es ' + x)")
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "8":
        os.system("cls")
        from app import menu
        menu()