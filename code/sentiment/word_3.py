import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
import pandas as pd
file_set = ['E:/mydata/pacon/output_{}.csv'.format(str(i)) for i in range(1,11)]
def get_wordclud(file_set):
    line_set = []
    for j in range(10):
        reader=csv.reader(open(file_set[j], 'r'))
        for line in reader:
            line_set.append(line[1])
    word_list = [" ".join(jieba.cut(sentence)) for sentence in line_set]
    new_text = ' '.join(word_list)
    wordcloud = WordCloud(font_path="C:/Python34/Lib/site-packages/wordcloud/simhei.ttf", background_color="black").generate(new_text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

get_wordclud(file_set)

