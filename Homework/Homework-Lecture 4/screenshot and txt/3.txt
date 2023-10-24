import random

def main():
    print("欢迎来到文本冒险游戏！")
    print("你的任务是在提瓦特大陆中寻找宝藏。")

    player_location = "风起地"
    treasure_found = False

    while not treasure_found:
        print(f"你现在在{player_location}。")

        if player_location == "风起地":
            print("你可以选择向前、左转或右转。")
            choice = input("请输入你的选择：")
            if choice == "向前":
                player_location = "龙脊雪山"
            elif choice == "左转":
                player_location = "苍风高地"
            elif choice == "右转":
                player_location = "归离原"
            else:
                print("无效的选择，你不能离开提瓦特大陆。")

        elif player_location == "龙脊雪山":
            print("在龙脊雪山里你遇到了一只冰深渊法师！")
            choice = input("你可以选择“战斗”或“逃跑”：")
            if choice == "战斗":
                if random.randint(0, 1) == 1:
                    print("你勇敢地战胜了冰深渊法师，但受了点伤。将回七天神像治疗。")
                    player_location = "风起地"
                else:
                    print("冰深渊法师太强了，你被击败了。")
                    break
            elif choice == "逃跑":
                print("你逃跑了。将回七天神像休整。")
                player_location = "风起地"
            else:
                print("无效的选择，请重新选择。")

        elif player_location == "苍风高地":
            print("你在苍风高地发现了一个宝箱！")
            choice = input("你可以选择“打开”或“离开”：")
            if choice == "打开":
                print("恭喜你，你找到了宝藏！你赢了游戏！")
                treasure_found = True
            elif choice == "离开":
                print("你离开了宝箱。回了家")
                player_location = "风起地"
            else:
                print("无效的选择，请重新选择。")

        elif player_location == "归离原":
            print("在归离原你发现了一只浪船。")
            choice = input("你可以选择“乘船”或“回头”：")
            if choice == "乘船":
                print("你乘船渡过了云来海，到达了苍风高地，继续你的冒险。")
                player_location = "苍风高地"
            elif choice == "回头":
                print("你回头了。回了家")
                player_location = "风起地"
            else:
                print("无效的选择，请重新选择。")

    print("游戏结束！")

if __name__ == "__main__":
    main()
