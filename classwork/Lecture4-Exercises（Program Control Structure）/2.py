all = int(input("请输入总鸡和兔的数量："))
LegNum = int(input("请输入它们的总腿数："))

tu = (LegNum - all * 2) / 2

if tu.is_integer():
    ji = all - int(tu)
    print(f"鸡的数量为 {ji}，兔子的数量为 {int(tu)}。")
else:
    print("输入数据不正确，兔子的数量不是整数。")
