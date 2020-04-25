#!/local/bin/python3

from nltk.corpus import gutenberg
from nltk import FreqDist

list_of_words = gutenberg.words("austen-persuasion.txt")
fd = FreqDist(list_of_words)

print("Total number of tokens: "+ str(fd.N())) #98171
print("Number of unique tokens: "+ str(fd.B())) #6132
print("Top 10 tokens:") #to
for token, freq in fd.most_common(10):
    print(token + "\t" + str(freq))
