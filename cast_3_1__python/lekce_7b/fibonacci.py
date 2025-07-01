def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


try:
    pocet = int(input("Zadej počet členů Fibonacciho posloupnost: "))
    if pocet < 0:
        print("Nelze.")
    else:
        for i in range(pocet):
            print(fibonacci(i), end=" ")

except ValueError:
    print("Neplatná hodnota.")
