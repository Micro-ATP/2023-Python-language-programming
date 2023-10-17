# 创建一个空的字典
movieRatings = {}

# 添加电影评分
def addMovieRating(movieName, rating):
    movieRatings[movieName] = rating
    print(f"电影 '{movieName}' 的评分已添加为 {rating}")

# 查找电影评分
def findMovieRating(movieName):
    if movieName in movieRatings:
        print(f"电影 '{movieName}' 的评分是 {movieRatings[movieName]}")
    else:
        print(f"找不到电影 '{movieName}' 的评分")

# 修改电影评分
def modifyMovieRating(movieName, newRating):
    if movieName in movieRatings:
        movieRatings[movieName] = newRating
        print(f"电影 '{movieName}' 的评分已更新为 {newRating}")
    else:
        print(f"找不到电影 '{movieName}' 的评分")

# 删除电影评分
def deleteMovieRating(movieName):
    if movieName in movieRatings:
        del movieRatings[movieName]
        print(f"电影 '{movieName}' 的评分已删除")
    else:
        print(f"找不到电影 '{movieName}' 的评分")


while True:
    print("\n电影评分系统")
    print("1. 添加电影评分")
    print("2. 查找电影评分")
    print("3. 修改电影评分")
    print("4. 删除电影评分")
    print("5. 退出")
    
    choice = input("请选择操作 (1/2/3/4/5): ")
    
    if choice == '1':
        movieName = input("请输入电影名称: ")
        rating = float(input("请输入评分: "))
        addMovieRating(movieName, rating)
    elif choice == '2':
        movieName = input("请输入电影名称: ")
        findMovieRating(movieName)
    elif choice == '3':
        movieName = input("请输入电影名称: ")
        newRating = float(input("请输入新的评分: "))
        modifyMovieRating(movieName, newRating)
    elif choice == '4':
        movieName = input("请输入电影名称: ")
        deleteMovieRating(movieName)
    elif choice == '5':
        break
    else:
        print("无效的选项，请重新选择。")
