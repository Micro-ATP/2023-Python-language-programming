import jieba
import wordcloud
from imageio import imread
mask = imread("chinamap.jpg")
f = open("2020年1号文件.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
t_ls = []
for i in ls:
    if len(i) >= 1:
        t_ls.append(i)
txt = " ".join(t_ls)
w = worldcloud.WordCloud(\
    width = 1000,height = 700,\
    background_color = "white",
    font_path = "msyh.ttc",mask = mask
    )