# 参考资料：https://blog.csdn.net/weixin_43823808/article/details/104038733

def Hanoi(n, a, b, c):
    if n == 0:
        return
    Hanoi(n - 1, a, c, b)
    print(f"Move disk {n} from {a} to {c}")
    Hanoi(n - 1, b, a, c)


n = int(input("Enter the number of disks: （题目说要64，请您自己输入64吧，但是运行时间非常长，受不了就换个小的）"))
Hanoi(n, 'A', 'B', 'C')
