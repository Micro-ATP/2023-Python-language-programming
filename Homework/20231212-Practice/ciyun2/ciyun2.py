import jieba
import wordcloud
excludes = {}
f = open("Homework\\20231212-Practice\\ciyun2\\词云2配套.txt","r",encoding="utf-8")
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
    font_path = "msyh.ttc",\
    max_words = 200)
w.generate(txt)
w.to_file("Homework\\20231212-Practice\\ciyun2\\pytestcloud2.png")