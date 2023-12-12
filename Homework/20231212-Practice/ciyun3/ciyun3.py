import jieba
import wordcloud
from imageio import imread
mask = imread("Homework\\20231212-Practice\\ciyun3\\chinamap.png")
f = open("Homework\\20231212-Practice\\ciyun3\\词云3配套.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
t_ls = []
for i in ls:
    if len(i) >= 1:
        t_ls.append(i)
txt = " ".join(t_ls)
w = wordcloud.WordCloud(\
    width = 1000,height = 700,\
    background_color = "white",
    font_path = "msyh.ttc",mask = mask
    )
w.generate(txt)
w.to_file("Homework\\20231212-Practice\\ciyun3\\testcloudm.png")