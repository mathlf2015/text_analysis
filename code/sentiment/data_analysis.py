import pandas
file_set_out = ['E:/mydata/pacon/score_{}.csv'.format(str(i)) for i in range(1,11)]
file_upload_set_1 = ['E:/mydata/pacon/upload/upload_raw_{}.csv'.format(str(i)) for i in range(1,11)]
file_upload_set_2 = ['E:/mydata/pacon/upload/upload_analysis_{}.csv'.format(str(i)) for i in range(1,11)]
def score_factor(x):
	if x < -5:
		return 'very bad'
	elif x >=-5 and x<0:
		return 'bad'
	elif x>=0 and x<5:
		return 'good'
	else:
		return 'very good'
def get_upload(file_in,file_upload_1,file_upload_2):
	for i in range(10):
		df = pandas.read_csv(file_in[i],header=None)
		df.columns = ['id','score']
		df['score_factor'] = df['score'].apply(score_factor)
		df.to_csv(file_upload_1[i],index=False,encoding='utf-8')
		df.groupby(['score_factor'])['id'].count().to_csv(file_upload_2[i],encoding='utf-8')
		#print(df.groupby(['score_factor'])['id'].count())
		#print(df.info())
		#print(df.head())
get_upload(file_set_out,file_upload_set_1,file_upload_set_2)
