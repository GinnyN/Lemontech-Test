def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def rightZeros(n):
    numberString = str(factorial(n))
    numberZeros = 0
    for digit in numberString:
        if digit == "0":
            numberZeros += 1
    return numberZeros


