# coding=utf-8

import string
import re
from zhon.hanzi import punctuation
import codecs
import operator

FILEPATH= '/Users/yangxu/Code/OpenMind/DeepLearningStartUp/happiness_seg.txt'
SEPC = '&'

CountDict = {} 

def processSentence(sentence):
    words = string.split(sentence, ' ')
    if len(words) < 2:
        return
    i = 0
    while i < len(words) - 1:
        key = words[i] + ' ' + words[i + 1]
        addKeyToDict(key)
        i = i + 1

def addKeyToDict(key):
    if CountDict.has_key(key):
        CountDict[key] = CountDict[key] + 1
    else:
        CountDict[key] = 1
    return


with open(FILEPATH, 'rb') as f:
    count = 0
    for line in f:
        count = count + 1
        line = line.decode("utf-8")
        sentences = (re.sub(ur"([%s]+) | (― ―)" %punctuation, SEPC, line))
        sentences = string.split(sentences, SEPC)
#        print(line)
#        print(sentences)
        for sentence in sentences:
            processSentence(sentence.strip())

sortedCountDict = sorted(CountDict.iteritems(), key=operator.itemgetter(1),
        reverse=True)

for item in sortedCountDict[:10]:
    print("%s = %d" % (item[0],item[1]))
