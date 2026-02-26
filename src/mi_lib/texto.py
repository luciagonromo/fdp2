def numero_a_palabras(n):
    """
    Convierte un número entero entre 0 y 999 en palabras.

    Parámetro:
    n (int): número entero entre 0 y 999

    Devuelve:
    str: número escrito en palabras o mensaje de error
    """

    # Validación del rango
    if n < 0 or n > 999:
        return "Número fuera de rango"

    # Diccionario de unidades
    unidades = {
        0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro",
        5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"
    }

    # Números especiales del 10 al 15
    especiales = {
        10: "diez", 11: "once", 12: "doce",
        13: "trece", 14: "catorce", 15: "quince"
    }

    # Diccionario de decenas
    decenas = {
        2: "veinte", 3: "treinta", 4: "cuarenta",
        5: "cincuenta", 6: "sesenta",
        7: "setenta", 8: "ochenta", 9: "noventa"
    }

    # Diccionario de centenas
    centenas = {
        1: "ciento", 2: "doscientos", 3: "trescientos",
        4: "cuatrocientos", 5: "quinientos",
        6: "seiscientos", 7: "setecientos",
        8: "ochocientos", 9: "novecientos"
    }

    # Del 0 al 9
    if n < 10:
        return unidades[n]

    # Del 10 al 15
    if n <= 15:
        return especiales[n]

    # Del 16 al 19
    if n < 20:
        return "dieci" + unidades[n - 10]

    # Del 20 al 29
    if n < 30:
        return "veinte" if n == 20 else "veinti" + unidades[n - 20]

    # Del 30 al 99
    if n < 100:
        d = n // 10          # decenas
        u = n % 10           # unidades
        return decenas[d] if u == 0 else decenas[d] + " y " + unidades[u]

    # Caso especial 100
    if n == 100:
        return "cien"

    # Del 101 al 999
    c = n // 100            # centenas
    resto = n % 100         # resto del número
    return centenas[c] if resto == 0 else centenas[c] + " " + numero_a_palabras(resto)
