import time

def func_print():
    print("El bloque print es usado para mostrar información en la consola.")
    time.sleep(1)
    print("Puede mostrar texto, números y variables.")
    time.sleep(1)
    print("Estructura: print(Value)")
    time.sleep(1)
    print()
    print("Ejemplo: print('Hello World')")
    print()
    input("Presiona Enter para continuar...")
    
    from app import menu
    menu()