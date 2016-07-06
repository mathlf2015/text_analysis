import re
from bs4 import BeautifulSoup
import requests
url_set=['http://weibo.cn/comment/DC4q8qszv?uid=1537790411&rl=0&page={}'.format(str(i)) for i in range(1,100)]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Cookie':'ALF=1470298114; SCF=AgInCVdL4-h5FbmbwxvLYY8STjquGvSiT-hwoibnnesXwYEZjKGSsyQPGIFKfv6Sr5cdABFO_k2E1bHKpyexM-M.; SUB=_2A256fwQ-DeTxGeRJ7lYQ-C_Nwj-IHXVZg6x2rDV6PUJbktBeLUfEkW0EHSNw5HibVvU8nT-k01vMoC_Hxw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5IKW7zP-v6zdYM4qCfIeOB5JpX5o2p5NHD95QES0-XeKnpeK.0Ws4Dqcj1MNHVdrL0Us8ETKz7eKzt; SUHB=0S7SicPnd5-c6V; SSOLoginState=1467708526; gsid_CTandWM=4uMNCpOz5JBifd5JX6membyuh37; _T_WM=aff568ab6412aafc405b7d8ecaf2f08c'
}
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv
file =r'E:\mydata\pacon\result.csv'
writer=csv.writer(open(file, 'w'),lineterminator='\n')
def get_result(url_set):
    line_set = []
    for url in url_set:
        wb_data = requests.get(url,headers = headers)
        soup = BeautifulSoup(wb_data.text,'lxml')
        a = soup.select('span.ctt')
        for i in range(len(a)):
            text = re.sub('<[^>]*>', '',a[i].text)
            text = re.sub('鹿晗', ' ', text)
            text = re.sub('[\W]+', ' ', text)
            line_set.append(text)
            #print(text)
            #writer.writerow((i,text))
    word_list = [" ".join(jieba.cut(sentence)) for sentence in line_set]
    new_text = ' '.join(word_list)
    wordcloud = WordCloud(font_path="C:/Python34/Lib/site-packages/wordcloud/simhei.ttf", background_color="black").generate(new_text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

get_result(url_set)


