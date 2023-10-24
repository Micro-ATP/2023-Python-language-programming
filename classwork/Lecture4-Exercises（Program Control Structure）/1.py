month = int(input("请输入一个月份（1-12）："))

if month == 1:
    days = 31
elif month == 2:
    days = 28
elif month == 3:
    days = 31
elif month == 4:
    days = 30
elif month == 5:
    days = 31
elif month == 6:
    days = 30
elif month == 7:
    days = 31
elif month == 8:
    days = 31
elif month == 9:
    days = 30
elif month == 10:
    days = 31
elif month == 11:
    days = 30
elif month == 12:
    days = 31
else:
    print("无效的月份输入")
    days = None

if days is not None:
    print(f"{month}月有{days}天。")
