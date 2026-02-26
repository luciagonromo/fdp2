def ahorcado(palabra):
    # Normalizamos la palabra a minúsculas y quitamos espacios
    palabra = palabra.strip().lower()

    # Convertimos la palabra en una lista de letras
    letras_palabra = list(palabra)
    # Lista de control de letras restantes (solo letras únicas)
    letras_restantes = set(letras_palabra)
    # Listas de control
    letras_acertadas = []
    letras_probadas = []

    # Contadores de fallos y fija fallos maximos
    fallos = 0
    MAX_FALLOS = 5

    def mostrar_palabra():
        # Construimos la palabra mostrando letras acertadas y * en las demás, recorriendo todas las letras de la palabra
        progreso = [
            letra if letra in letras_probadas else '*'
            for letra in letras_palabra
        ]
        print("Palabra:", "".join(progreso))  # une la lista y la muestra como texto
        return progreso

    mostrar_palabra()

    ##...JUEGO...##
    while fallos < MAX_FALLOS and letras_restantes:  # el juego sigue mientras no haya mas de 5 fallos y haya letras por adivinar 

        letra = input("Introduce una letra: ").lower()

        # Comprobamos que sea una sola letra
        if len(letra) != 1 or letra < 'a' or letra > 'z':
            print("Letra no válida")
            continue

        # Si ya se probó, no cuenta como fallo
        if letra in letras_probadas:
            print("Letra ya probada")
            continue

        letras_probadas.append(letra)

        # Comprobamos si la letra está en la palabra
        if letra in letras_restantes:
            letras_restantes.remove(letra)
            print("Acierto")
        else:
            fallos += 1
            print("Fallo")

        mostrar_palabra()
        print('Fallos:', fallos)

    # FINAL
    if not letras_restantes:
        print("Ganaste")
    else:
        print("Perdiste")
