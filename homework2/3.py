def isLeapYear(n):
    if n % 400 == 0:
        return True
    if n % 100 != 0:
        if n % 4 == 0:
            return True
        else:
            return False
    else:
        return False
    
n = int(input("请输入一个年份："))
if isLeapYear(n) == True:
    print("是闰年")
else :
    print("不是闰年")