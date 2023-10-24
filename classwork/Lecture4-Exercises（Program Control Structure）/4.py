n = int(input("请输入一个整数 n:"))

a = 1

for i in range(1, n + 1):
    a *= i

print(f"{n} 的阶乘是 {a}")
