def fibonacci(n):
    # Caso base: si n es 0 o 1, devolvemos n
    if n <= 1:
        return n
    # Caso recursivo: sumamos los dos términos anteriores
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de uso:
n = int(input("Introduce el número n: "))
print(f"El término {n} de la serie Fibonacci es: {fibonacci(n)}")
