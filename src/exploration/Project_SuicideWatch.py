import pandas as pandas
import nltk as nltk
from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords

#Collect SuicideWatch data
data = pandas.read_csv("C:\Users\Zeus\Desktop\Projects\SuicideWatch\Data\SuicideWatch posts 2016_11.csv")
titles = data.title
titles = list(titles)
posts = data.selftext

the_counter = Counter()
stopwords = set(stopwords.words('english'))

for line in titles:
    try:
        line = line.decode('ascii',errors='ignore')
        words = word_tokenize(line)
        for word in words:
            if word not in stopwords:
                word = word.lower()
                the_counter[word] += 1
    except:
        print line
        #break
        #for word in words:
        #  if word not in stopwords:
        #  word = word.lower()
        #  the_counter[word] += 1

the_counter.most_common(50)

