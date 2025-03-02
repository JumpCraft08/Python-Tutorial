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

def func_1(rounded_box):
    os.system("cls")
    print("  ____            _                     _        _____       _   _                 ")
    print(" |  _ \          (_)                   | |      |  __ \     | | | |                ")
    print(" | |_) | __ _ ___ _  ___ ___  ___    __| | ___  | |__) |   _| |_| |__   ___  _ __  ")
    print(" |  _ < / _` / __| |/ __/ _ \/ __|  / _` |/ _ \ |  ___/ | | | __| '_ \ / _ \| '_ \ ")
    print(" | |_) | (_| \__ \ | (_| (_) \__ \ | (_| |  __/ | |   | |_| | |_| | | | (_) | | | |")
    print(" |____/ \__,_|___/_|\___\___/|___/  \__,_|\___| |_|    \__, |\__|_| |_|\___/|_| |_|")
    print("                                                        __/ |                      ")
    print("                                                       |___/                       ")
    print()
    print("[1] Bloque print()")
    print("[2] Bloque input()")
    print("[3] Salir")
    print()
    option = input("> ")
    if option == "1": 
        os.system("cls")
        rounded_box([f"{grs}El bloque print() es usado para mostrar información en la consola.",
                     f"{grs}Puede mostrar texto, números y variables."], g_border)
        time.sleep(2)
        print()
        rounded_box([f"{yel}print{syel}({orn}Value{syel})"], r_border)
        time.sleep(2)
        print()
        rounded_box([f"{yel}print{syel}({orn}'Hello World'{syel})",
                     f"{yel}print{syel}({sgrn}10{syel})",
                     f"{yel}print{syel}({cya}x{syel})"], b_border)
        print()
        input("Presiona Enter para continuar...")
        func_1(rounded_box)
    elif option == "2":
        os.system("cls")
        rounded_box([f"{grs}El bloque input() es usado para recibir información del usuario.",
                 f"{grs}Puede recibir texto, números y variables."], g_border)
        time.sleep(2)
        print()
        rounded_box([f"{yel}input{syel}({orn}Value{syel})"], r_border)
        time.sleep(2)
        print()
        rounded_box([f"{yel}input{syel}({orn}'Ingresa tu nombre'{syel})",
                    f"{grs}# Esto dará --> Ingresa tu nombre (Nombre escrito por usuario)"], b_border)
        print()
        input("Presiona Enter para continuar...")
        func_1(rounded_box)
    elif option == "3":
        from app import menu
        menu()
    else:
        print("Opción no válida")
        time.sleep(1)
        func_1(rounded_box)