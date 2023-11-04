TK_SILENCE_DEPRECATION=1

# 参考资料：https://zhuanlan.zhihu.com/p/184922848
# 参考资料：https://blog.csdn.net/m0_46581543/article/details/108288808
# 以下内容主要是依葫芦画瓢

import turtle
import time

def drawGap():  # 画数码管的间隔
    turtle.penup()
    turtle.fd(5)
    
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()  # 紧凑写法
    turtle.fd(40)
    drawGap()
    turtle.right(90)
    
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
    
def drawDate(date):
    turtle.pencolor("gold") if date[-1]=='@' else turtle.pencolor("red")
    for i in date:
        if i=='-':
            turtle.right(90)
            turtle.fd(18)
            turtle.left(90)
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.left(90)
            turtle.fd(18)
            turtle.right(90)
            turtle.fd(40)
        elif i=='=':
            turtle.right(90)
            turtle.fd(18)
            turtle.left(90)
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.left(90)
            turtle.fd(18)
            turtle.right(90)
            turtle.fd(40)
        elif i== '+':
            turtle.right(90)
            turtle.fd(18)
            turtle.left(90)            
            turtle.write('日',font=("Arial",18,"normal"))
            turtle.pencolor("brown")
            turtle.left(90)
            turtle.fd(18)
            turtle.right(90)
            turtle.fd(40)
        elif i== '<':
            turtle.right(90)
            turtle.fd(18)
            turtle.left(90)
            turtle.write('时',font=("Arial",18,"normal"))
            turtle.pencolor("purple")
            turtle.left(90)
            turtle.fd(18)
            turtle.right(90)
            turtle.fd(40)
        elif i== '>':
            turtle.right(90)
            turtle.fd(18)
            turtle.left(90)            
            turtle.write('分',font=("Arial",18,"normal"))
            turtle.left(90)
            turtle.fd(18)
            turtle.right(90)
            turtle.fd(40)
        elif i== '@':
            turtle.pencolor("gold")
            turtle.right(90)
            turtle.fd(18)
            turtle.left(90)            
            turtle.write('秒',font=("Arial",18,"normal"))
            turtle.left(90)
            turtle.fd(18)
            turtle.right(90)
        else:
            drawDigit(eval(i))
            
def main():
    turtle.setup(1600,350,200,200)
    turtle.speed("fastest")
    turtle.penup()
    turtle.fd(-600)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+%H<%M>',time.localtime()))
    drawDate(time.strftime('%S@',time.localtime()))
    turtle.hideturtle()
    turtle.done()
main()