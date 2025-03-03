import time, os

yel = "\033[33m" # [Amarillo] Bloques (print, input, etc)
syel = "\033[93m" # [Amarillo brillante] Parentesis
cya = "\033[36m" # [Cyan] Variables
ble = "\033[34m" # [Azul oscuro] Funciones
sgrn = "\033[92m" # [Verde Brillante] Numeros
orn = "\033[38;5;94m" # [Naranja] Texto
b_border = '\033[34m' # Borde azul
r_border = '\033[31m' # Borde rojo
g_border = '\033[32m' # Borde verde
reset = '\033[0m' # Resetear colores
grs = '\033[90m' # Gris oscuro

def func_variable(rounded_box):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r" __      __        _       _     _            ")
    print(r" \ \    / /       (_)     | |   | |           ")
    print(r"  \ \  / /_ _ _ __ _  __ _| |__ | | ___  ___  ")
    print(r"   \ \/ / _` | '__| |/ _` | '_ \| |/ _ \/ __| ")
    print(r"    \  / (_| | |  | | (_| | |_) | |  __/\__ \ ")
    print(r"     \/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/ ")
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
        os.system('cls' if os.name == 'nt' else 'clear')
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
        os.system('cls' if os.name == 'nt' else 'clear')
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
        
        os.system('cls' if os.name == 'nt' else 'clear')
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
        os.system('cls' if os.name == 'nt' else 'clear')
        rounded_box([f"{grs}Puedes asignar multiples variables en una sola linea"], g_border)
        time.sleep(1)
        print()
        rounded_box([f"{cya}a{reset}, {cya}b{reset}, {cya}c {reset}= {sgrn}5{reset}, {sgrn}3.2{reset}, {orn}'Hello'",
                     "",
                     f"{yel}print{syel}({cya}a{syel})",
                     f"{grs}# Nos dará 5",
                     "",
                     f"{yel}print{syel}({cya}b{syel})",
                     f"{grs}# Nos dará 3.2",
                     "",
                     f"{yel}print{syel}({cya}c{syel})",
                     f"{grs}#Nos dará 'Hello'"], b_border)
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        rounded_box([f"{grs}Puedes asignar multiples variables con el mismo valor"], g_border)
        time.sleep(1)
        print()
        rounded_box([f"{cya}x {reset}= {cya}y {reset}= {cya}z {reset}= {orn}'Same'",
                     "",
                     f"{yel}print{syel}({cya}x{syel})",
                     f"{grs}# Nos dará 'Same'",
                     "",
                     f"{yel}print{syel}({cya}y{syel})",
                     f"{grs}# Nos dará 'Same'",
                     "",
                     f"{yel}print{syel}({cya}z{syel})",
                     f"{grs}# Nos dará 'Same'"], b_border)
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        rounded_box([f"{grs}Puedes asignar multiples variables en una sola linea"], g_border)
        time.sleep(1)
        print()
        rounded_box([f"{cya}fruits {reset}= {syel}[{orn}'apple'{reset}, {orn}'banana'{reset}, {orn}'cherry'{syel}]",
                     "",
                     f"{cya}a{reset}, {cya}b{reset}, {cya}c {reset}= {cya}fruits",
                     "",
                     f"{yel}print{syel}({cya}a{syel})",
                     f"{grs}# Nos dará 'apple'",
                     ""
                     f"{yel}print{syel}({cya}b{syel})",
                     f"{grs}# Nos dará 'banana'",
                     ""
                     f"{yel}print{syel}({cya}b{syel})",
                     f"{grs}# Nos dará 'cherry'"], b_border)
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "6":
        os.system('cls' if os.name == 'nt' else 'clear')
        rounded_box([f"{grs}Puedes sumar variables"], g_border)
        time.sleep(1)
        print()
        rounded_box([f"{cya}x {reset}= {sgrn}5",
                     f"{cya}y {reset}= {sgrn}8",
                     f"{cya}z {reset}= {orn}'hola'",
                     "",
                     f"{yel}print{syel}({cya}x {reset}+ {cya}y{syel})",
                     f"{grs}# Nos dará 13",
                     "",
                     f"{yel}print{syel}({cya}z {reset}+ {cya}z {reset}+ {sgrn}str{syel}({cya}x{syel}))",
                     f"{grs}# Nos dará 'hola hola 5' (No se puede sumar un str con un int)",
                     "",
                     f"{yel}print{syel}({cya}x{reset}, {cya}y{reset}, {cya}z{syel})",
                     f"{grs}# Nos dará 5 8 hola"], b_border)
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        rounded_box([f"{grs}Si determinas una variable fuera de una función,",
                     f"{grs}podras usarlo en cualquier parte del codigo"], g_border)
        print()
        time.sleep(2)
        rounded_box([f"{cya}x {reset}= {orn}'Fantastico'",
                     "",
                     f"{ble}def {yel}myfunc{syel}()",
                     f"   {yel}print{syel}({orn}'Python es ' {reset}+ {cya}x{syel})",
                     "",
                     f"{yel}myfunc{syel}()",
                     f"{grs}# Nos dará 'Python es Fantastico', ya que la variable esta fuera de la función"], b_border)
        print()
        input("Presiona Enter para continuar...")

        os.system('cls' if os.name == 'nt' else 'clear')
        rounded_box([f"{grs}Con esta información, podriamos hacer dos variables con el mismo nombre, una",
                     f"{grs}dentro de una función y otra fuera"], g_border)
        print()
        time.sleep(2)
        rounded_box([f"{cya}x {reset}= {orn}'Horrible'",
                     "",
                     f"{ble}def {yel}myfunc{syel}()",
                     f"    {cya}x {reset}= {orn}'Maravilloso'",
                     f"{yel}print{syel}({orn}'Python es ' {reset}+ {cya}x{syel})",
                     "",
                     f"{yel}myfunc{syel}()",
                     f"{grs}# Eso dará Maravilloso, ya que la variable x de dentro de la función es Maravilloso",
                     "",
                     f"{yel}print{syel}({orn}'Python es ' {reset}+ {cya}x{syel})",
                     f"{grs}# Esto dará Horrible, ya que la variable x esta fuera de la función"])
        print()
        input("Presiona Enter para continuar...")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        rounded_box([f"{grs}Entonces, para poder usar una variable dentro de una función hacemos:"], g_border)
        print()
        time.sleep(2)
        rounded_box([f"{ble}def {yel}myfunc{syel}()",
                     f"   {ble}global {cya}x",
                     f"   {cya}x {reset}= {orn}'Maravilloso'",
                     "",
                     f"{yel}myfunc{syel}()",
                     "",
                     f"{yel}print{syel}({orn}'Python es ' {reset}+ {cya}x{syel})",
                     f"{grs}# Esto dará 'Python es Maravilloso', ya que la variable x es global"], b_border)
        time.sleep(1)
        print()
        input("Presiona Enter para continuar...")
        func_variable(rounded_box)
    elif option == "8":
        os.system('cls' if os.name == 'nt' else 'clear')
        from app import menu
        menu()