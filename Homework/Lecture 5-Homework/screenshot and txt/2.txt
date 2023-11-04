fibSum = 0

def fib(n):
    global fibSum
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def calFiSum(howLong):
    global fibSum
    fibSum = 0
    for i in range(howLong):
        fibSum += fib(i)
    return fibSum

howLong = int(input("请给出斐波那契数列的长度："))
totalSum = calFiSum(howLong)
print(f"斐波那契数列的前 {howLong} 个数字的总和为: {totalSum}")
