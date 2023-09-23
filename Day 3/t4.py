def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

n_terminos = int(input("Número de términos en la secuencia de Fibonacci: "))
resultado = fibonacci(n_terminos)
print("Secuencia de Fibonacci:", resultado)
