import jieba
import wordcloud
from imageio import imread
mask = imread("Homework\\20231212-Practice\\ciyun4\\mind.png")
f = open("Homework\\20231212-Practice\\ciyun4\\三国演义.txt", "r", encoding="utf-8")
t = f.read ()
f.close()
ls = jieba.lcut(t)
t_1s=[]
for i in ls:
    if len(i) > 1:
        t_1s. append(i)
txt = " ".join(t_1s)
w = wordcloud.WordCloud(\
    width = 1000, height= 700,\
    background_color = "white",
    font_path = "Homework\\20231212-Practice\\ciyun4\\MSYH.TTC", mask = mask
    )
w.generate(txt)
w.to_file("Homework\\20231212-Practice\\ciyun4\\sanguo.png")