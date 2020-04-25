#!/local/bin/python3

from nltk.corpus import stopwords 
from nltk.tokenize import sent_tokenize, word_tokenize

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."

stopWords = set(stopwords.words('english'))
words = word_tokenize(data.lower())
wordsFiltered = []

for w in words:
      if w not in stopWords:
           wordsFiltered.append(w)

print(len(stopWords))
print(stopWords)
print(wordsFiltered)
