preguntas = [
    "¿CUAL ES EL ANIMAL MAS GRANDE DE LA TIERRA?", 
    "¿CUAL ES EL VALOR DEL NUMERO PI?",
    "¿QUE NOMBRE TIENE LA CAPITAL DE RD?"
]
opciones = [
    ("LA BALLENA AZUL", "LEON", "ELEFANTE"),
    ("3.14", "2.71", "1.62"),
    ("SANTO DOMINGO", "SANTIAGO", "LA VEGA")
]
# Las respuestas correctas en una lista aparte para comparar
correctas = ["LA BALLENA AZUL", "3.14", "SANTO DOMINGO"]

for i in range(len(preguntas)):
    print(" ------ ESCRIBE EL NOMBRE COMPLETO EN LA RESPUESTA O DIRA (INCORRECTA) ")
    print("\n" + preguntas[i]) # Imprime la pregunta
    
    # Ciclo para imprimir las opciones de esa pregunta
    for j in range(len(opciones[i])):
        print(f"{j+1}- {opciones[i][j]}")
    
    # Pedimos la respuesta justo después de mostrar las opciones
    usuario = input("Tu respuesta: ").upper() # .upper() por si escribe en minúsculas
    
    # Evaluamos de una vez
    if usuario == correctas[i]:
        print("✅ RESPUESTA CORRECTA")
    else:
        print(f"❌ INCORRECTA. La respuesta era: {correctas[i]}")

print("\n--- Juego terminado ---")
print(type(i))