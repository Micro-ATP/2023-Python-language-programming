while True:
    try:
        numJudges = int(input("请输入评委人数: "))
        if numJudges < 2:
            print("评委人数必须至少为 2 人。请重新输入。")
        else:
            break
    except ValueError:
        print("无效输入。请输入一个有效的数字。")

scores = []
for i in range(1, numJudges + 1):
    while True:
        try:
            score = float(input(f"请输入第 {i} 位评委的得分 (0 到 10 分): "))
            if 0 <= score <= 10:
                scores.append(score)
                break
            else:
                print("无效得分。得分必须在 0 到 10 之间。请重新输入。")
        except ValueError:
            print("无效输入。请输入一个有效的得分。")


if len(scores) < 3:
    print("至少需要 3 个评分才能计算最终得分。")
else:
    scores.remove(max(scores))
    scores.remove(min(scores))
    
    final_score = sum(scores) / len(scores)
    print(f"最终平均得分为: {final_score:.2f}")
