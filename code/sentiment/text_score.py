import sys
import jieba as jb
import os
#print(os.getcwd())



def loadDict(fileName, score):
	wordDict = {}
	with open(fileName) as fin:
		for line in fin:
			word = line.strip()
			wordDict[word] = score
	return wordDict

def appendDict(wordDict, fileName, score):
	with open(fileName) as fin:
		for line in fin:
			word = line.strip()
			wordDict[word] = score

def loadExtentDict(fileName):
	extentDict = {}
	for i in range(6):
		with open(fileName + str(i + 1)+ u"词语（中文）" + ".txt") as fin :
			for line in fin:
				word = line.strip()
				extentDict[word] = i + 1
	return extentDict

postDict = loadDict(u"sentimentDict/正面情感词语（中文）.txt", 1)
appendDict(postDict, u"sentimentDict/正面评价词语（中文）.txt", 1)
appendDict(postDict, u"sentimentDict/正面评价词语（中文）1.txt", 1)
appendDict(postDict, u"sentimentDict/正面评价词语（中文）2.txt", 1)
#appendDict(postDict, u"sentimentDict/正面.txt", 1)
negDict = loadDict(u"sentimentDict/负面情感词语（中文）.txt", -1)
appendDict(negDict, u"sentimentDict/负面评价词语（中文）.txt", -1)
#appendDict(negDict, u"sentimentDict/负面.txt", -1)
#postDict = loadDict(u"sentimentDict/正面.txt", 1)
#negDict = loadDict(u"sentimentDict/负面.txt", -1)
extentDict = loadExtentDict(u"sentimentDict/程度级别")
inverseDict = loadDict(u"sentimentDict/否定词语.txt", -1)
punc = loadDict(u"sentimentDict/感叹号.txt", 1)
exclamation = {"!":2, "！":2}

file_set_in = ['E:/mydata/pacon/output_{}.csv'.format(str(i)) for i in range(1,11)]
file_set_out = ['E:/mydata/pacon/score_{}.csv'.format(str(i)) for i in range(1,11)]

import csv
def get_score(file_set_in,file_set_out):
	for j in range(10):
		reader=csv.reader(open(file_set_in[j], 'r'))
		writer=csv.writer(open(file_set_out[j], 'w'),lineterminator='\n')
		for record in reader:
			#print(record[1])
			key = record[0]
			content = record[1]
			wordList = list(jb.cut(content))
			#wordList.reverse()
			#print(wordList)
			lastWordPos = 0
			lastPuncPos = 0
			i = 0
			for word in wordList:
				#word = word.encode("utf-8")
				#print(word)
				if word in punc:
					lastPuncPos = i
				if word in postDict:
					if lastWordPos > lastPuncPos:
						start = lastWordPos
					else:
						start = lastPuncPos
					score = 1
					#print ("start: " + str(start))
					#print "end: " + str(i)
					#print(score)
					for word_before in wordList[start:i]:
						#word_before = word_before.encode("utf-8")
						#print(word_before)
						if word_before in extentDict:
							score = score * extentDict[word_before]
						if word_before in inverseDict:
							score = score * -1
					for word_after in wordList[i+1:]:
						#word_after = word_after.encode("utf-8")
						if word_after in punc:
							if word_after in exclamation:
								score = score + 2
							else:
								break;
					#print ('%s\t%s\t%s' % (key, word, score))
					#print ('%s\t%s' % (key, score))
					lastWordPos = i
				elif word in negDict:
					if lastWordPos > lastPuncPos:
						start = lastWordPos
					else:
						start = lastPuncPos
					score = -1
					#print "start: " + str(start)
					#print "end: " + str(i)
					for word_before in wordList[start:i]:
						#word_before = word_before.encode("utf-8")
						if word_before in extentDict:
							score = score * extentDict[word_before]
						if word_before in inverseDict:
							score = score * -1
					for word_after in wordList[i+1:]:
						#word_after = word_after.encode("utf-8")
						if word_after in punc:
							if word_after in exclamation:
								score = score - 2
							else:
								break;
					#print ('%s\t%s\t%s' % (key, word, score))
					#print ('%s\t%s' % (key, score))
					lastWordPos = i
				i = i + 1
			print ('%s\t%s' % (key, score))
			writer.writerow((key,score))

get_score(file_set_in,file_set_out)


