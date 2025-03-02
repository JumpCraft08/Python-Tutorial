import os

def menu():
    os.system("cls")
    print("  _____       _   _                   _______    _             _       _ ")
    print(" |  __ \     | | | |                 |__   __|  | |           (_)     | |")
    print(" | |__) |   _| |_| |__   ___  _ __      | |_   _| |_ ___  _ __ _  __ _| |")
    print(" |  ___/ | | | __| '_ \ / _ \| '_ \     | | | | | __/ _ \| '__| |/ _` | |")
    print(" | |   | |_| | |_| | | | (_) | | | |    | | |_| | || (_) | |  | | (_| | |")
    print(" |_|    \__, |\__|_| |_|\___/|_| |_|    |_|\__,_|\__\___/|_|  |_|\__,_|_|")
    print("         __/ |                                                           ")
    print("        |___/                                                            ")
    print()
    print("[1] Bloque print")
    print("[2] Variables y tipos de datos")

    option = input("> ")
    if option == "1":
        os.system("cls")
        from func_print import func_print
        func_print()
    elif option == "2":
        os.system("cls")
        from func_variable import func_variable
        func_variable()

menu()