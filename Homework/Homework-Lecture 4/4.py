import math

n = int(input("Enter an integer less than 1000: "))

def primeFactors(n):
    k = 2
    factors = []
    while k <= math.sqrt(n):
        if n % k == 0:
            factors.append(k)
            n //= k
        else:
            k += 1
    if n > 1:
        factors.append(n)
    print(*factors)

primeFactors(n)
