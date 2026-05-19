# MENU

def menu():
        print("1. Opción 1: cafe con leche. PRECIO 1000")
        print("2. Opción 2: cafe solo. PRECIO 800")
        print("3. Opción 3: jugo de naranja. PRECIO 600")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        return opcion

resultado = 0
while True:
        opcion = menu()
        if opcion == "1":
                resultado += 1000
                print("Has seleccionado cafe con leche. PRECIO 1000")
                
        elif opcion == "2":
                        resultado += 800
                        print("Has seleccionado cafe solo. PRECIO 800")
                        
        elif opcion == "3":
                resultado += 600
                print("Has seleccionado jugo de naranja. PRECIO 600")
        elif opcion == "4":
                        print(f"EL TOTAL A PAGAR ES: {resultado}")
                        break
        else:
                        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

