import random
Num = random.randint(1, 100)

guessTime = 0

while True:
    userNum = int(input("请猜一个介于1和100之间的数字: "))
    
    guessTime = 1 + guessTime
    
    if userNum < Num:
        print("少了，再来。")
    elif userNum > Num:
        print("多了，再来。")
    else:
        print(f"太强啦！正确的数字是 {Num}，你猜了 {guessTime} 次就猜对了。")
        break
