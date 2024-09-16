def division_recursiva(dividendo, divisor):
    # Caso base: si el dividendo es menor que el divisor, el cociente es 0
    if dividendo < divisor:
        return 0
    # Caso recursivo: restar el divisor del dividendo y contar una unidad en el cociente
    else:
        return 1 + division_recursiva(dividendo - divisor, divisor)

# Ejemplo de uso
dividendo = 20
divisor = 3

cociente = division_recursiva(dividendo, divisor)
print(f"El cociente de {dividendo} dividido por {divisor} es {cociente}.")