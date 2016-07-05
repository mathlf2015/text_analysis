import pandas as pd
import matplotlib.pyplot as plt
file_set = ['E:/mydata/pacon/upload/upload_analysis_{}.csv'.format(str(i)) for i in range(1,11)]
fig,axes=plt.subplots(5,2)
axes = axes.flatten()
for i in range(10):
    df = pd.read_csv(file_set[i],header=None)
    df.plot(kind='bar',ax = axes[i],title='rank_{}'.format(str(i+1)),legend=False)
    axes[i].set_xticklabels(['bad','good','very bad','very good'],rotation=0,fontsize='small')
plt.subplots_adjust(wspace=0.2,hspace=0.5)
plt.savefig('E:/mydata/pacon/upload/analysis.png',dpi=1000,bbox_inches='tight')
plt.show()