#!/usr/bin/env python
#-*-coding:utf-8-*-
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

s1 = """ 在克鲁伊夫时代，巴萨联赛中完成了四连冠，后三个冠军都是在末轮逆袭获得的。
在91/92赛季，巴萨末轮前落后皇马1分，结果皇马客场不敌特内里费使得巴萨逆转。
一年之后，巴萨用几乎相同的方式逆袭，皇马还是末轮输给了特内里费。
在93/94赛季中，巴萨末轮前落后拉科1分。
巴萨末轮5比2屠杀塞维利亚，拉科则0比0战平瓦伦西亚，巴萨最终在积分相同的情况下靠直接交锋时的战绩优势夺冠。
神奇的是，拉科球员久基奇在终场前踢丢点球，这才有了巴萨的逆袭。"""

s2 = """ 巴萨上一次压哨夺冠，发生在09/10赛季中。末轮前巴萨领先皇马1分，只要赢球就将夺冠。
末轮中巴萨4比0大胜巴拉多利德，皇马则与对手踢平。
巴萨以99分的佳绩创下五大联赛积分纪录，皇马则以96分成为了悲情的史上最强亚军。"""

s3 = """在48/49赛季中，巴萨末轮2比1拿下同城死敌西班牙人，以2分优势夺冠。
52/53赛季，巴萨末轮3比0战胜毕巴，以2分优势力压瓦伦西亚夺冠。
在59/60赛季，巴萨末轮5比0大胜萨拉戈萨。皇马巴萨积分相同，巴萨靠直接交锋时的战绩优势夺冠。"""

mylist = [s1, s2, s3]
word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]
new_text = ' '.join(word_list)
wordcloud = WordCloud(font_path="C:/Python34/Lib/site-packages/wordcloud/simhei.ttf", background_color="black").generate(new_text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()