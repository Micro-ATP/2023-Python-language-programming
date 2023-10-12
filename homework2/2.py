def isPrime(num):


    if num <= 1:
        return False  

    for i in range(2, num):
        if num % i == 0:
            return False 

    return True 
n = 1
stopNum = int(input("请输入一个数字："))
for i in range(1,stopNum + 1):
    if isPrime(n) == True:
        print(n)
        n += 1
    else:
        n += 1
    