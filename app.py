import os, time, re
from func_variable import func_variable
from func_print import func_1

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

def rounded_box(lines, border_color):    
    # Calcular el ancho máximo de las líneas sin contar los códigos ANSI
    width = max(len(re.sub(r'\033\[[0-9;]*m', '', line)) for line in lines) + 4
    
    print(f"{border_color}╭{'─' * width}╮{reset}")
    
    # Imprimir cada línea con el borde especificado
    for line in lines:
        clean_length = len(re.sub(r'\033\[[0-9;]*m', '', line))  # Longitud sin los códigos ANSI
        padding = (width - 4) - clean_length  # Ajustar los espacios de relleno
        print(f"{border_color}│  {reset}{line}{' ' * padding}  {border_color}│{reset}")
    
    print(f"{border_color}╰{'─' * width}╯{reset}")

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(r"  _____       _   _                   _______    _             _       _ ")
        print(r" |  __ \     | | | |                 |__   __|  | |           (_)     | |")
        print(r" | |__) |   _| |_| |__   ___  _ __      | |_   _| |_ ___  _ __ _  __ _| |")
        print(r" |  ___/ | | | __| '_ \ / _ \| '_ \     | | | | | __/ _ \| '__| |/ _` | |")
        print(r" | |   | |_| | |_| | | | (_) | | | |    | | |_| | || (_) | |  | | (_| | |")
        print(r" |_|    \__, |\__|_| |_|\___/|_| |_|    |_|\__,_|\__\___/|_|  |_|\__,_|_|")
        print(r"         __/ |                                                           ")
        print(r"        |___/                                                            ")
        print()
        print("[1] Basicos de Python")
        print("[2] Variables y tipos de datos")

        option = input("> ")
        if option == "1": func_1(rounded_box)
        elif option == "2": func_variable(rounded_box)
        else: 
            print("Opción no válida")
            time.sleep(1)



menu()