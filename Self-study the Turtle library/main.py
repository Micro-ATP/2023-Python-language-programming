# 作业：陆岩淅 202229013034N 联系方式：atp@cuc.edu.cn

import turtle as ATP  # 用网名取代turtle，顺便偷懒少打点字

ATP.setup(1360,768,0,0)  # 将窗体横纵分辨率改为显示器常用分辨率，且将窗口置于左上角贴住屏幕边缘

ATP.penup()  # 抬起画笔，以便调整海龟出发点

ATP.fd(-400)  # 先移动到偏左的地方以便等下开始爬行

ATP.pendown()# 把海龟放下

ATP.pensize(20)  # 海龟（笔触）宽度

ATP.pencolor("green")  # 海龟颜色(python为绿似乎也没什么)

ATP.seth(-40)  # 旋转海龟初始朝向，顺时针40度方向
for i in range(6):
    #以左侧距离为r（如果r是负数，则以右侧距离-r）的点为圆心蛇皮走位（半径，旋转角度）
    ATP.circle(45,80)  # 半径45，弧度80
    ATP.circle(-45,80)  # 半径-45，弧度80
ATP.circle(45,45)  # 半径40，弧度40
ATP.fd(45)  # 向前40
ATP.circle(18,180)  # 半径18，掉头
ATP.fd(30)

ATP.done()  # 窗口保持
# 海龟没必要删除，留下了正好当python的眼睛



