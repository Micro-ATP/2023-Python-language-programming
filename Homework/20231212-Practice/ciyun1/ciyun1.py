import wordcloud
txt = "python python C Rust Rust Java PHP PHP C++ python"
w = wordcloud.WordCloud(background_color = "white")
w.generate(txt)
w.to_file("Homework\\20231212-Practice\\ciyun1\\pytestcloud1.png")