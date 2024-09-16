def multiplicar(a, b):

    # Caso 0
    if b == 0:
        return 0
    
    if b > 0:
        return a + multiplicar(a, b - 1)
    
    # Caso negativo
    if b < 0:
        return -multiplicar(a, -b)

# Ejemplo de uso
resultado = multiplicar(5, 3)
print(f"5 * 3 = {resultado}")