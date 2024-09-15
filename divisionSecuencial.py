def division_secuencial(dividendo, divisor):
    # Verifica si el divisor es 0
    if divisor == 0:
        raise ValueError("El divisor no puede ser 0")
    
    # Maneja el caso de números negativos
    negativo = (dividendo < 0) != (divisor < 0)
    dividendo = abs(dividendo)
    divisor = abs(divisor)
    
    cociente = 0
    residuo = dividendo
    
    while residuo >= divisor:
        residuo -= divisor
        cociente += 1
    
    # Ajusta el signo del cociente
    if negativo:
        cociente = -cociente
    
    return cociente, residuo

# Ejemplo de uso
dividendo = 25
divisor = 4
cociente, residuo = division_secuencial(dividendo, divisor)
print(f"{dividendo} dividido por {divisor} da cociente {cociente} y residuo {residuo}")