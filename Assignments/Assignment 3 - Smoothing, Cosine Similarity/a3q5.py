#!/local/bin/python3
import re
import sys

if len(sys.argv) == 1:
    print("\n\n*** Please enter the files as the arguments ***\n\n")
term_file = sys.argv[1]
file1 = sys.argv[2]
file2 = sys.argv[3]

bag_of_words = []
docOneWords = []
docTwoWords = []
with open(term_file, 'r') as termFile:
    term_file = [line.split(",") for line in termFile.read().splitlines()]
    for i in term_file:
        for j in i:
            bag_of_words.append(j)

with open(file1, 'r') as file1:
    file = [line.strip() for line in file1 if line.strip()]
    for i in file:
        j = i.split(' ')
        for k in j:
            docOneWords.append(re.sub("\W", '', k.lower()))

with open(file2, 'r') as file2:
    file = [line.strip() for line in file2 if line.strip()]
    for i in file:
        j = i.split(' ')
        for k in j:
            docTwoWords.append(re.sub("\W", '', k.lower()))

# print(bag_of_words)
# print(docOneWords)
# print(docTwoWords)

docOneWordsFreq = []
docTwoWordsFreq = []

for word in bag_of_words:
    docOneWordsFreq.append(docOneWords.count(word))

for word in bag_of_words:
    docTwoWordsFreq.append(docTwoWords.count(word))


# print(docOneWordsFreq)
# print(docTwoWordsFreq)

def getDotProduct(docOneWordsFreq, docTwoWordsFreq):
    return sum(i * j for i, j in zip(docOneWordsFreq, docTwoWordsFreq))


def getCosineSimilarity(docOneWordsFreq, docTwoWordsFreq):
    denominator = ((getDotProduct(docOneWordsFreq, docOneWordsFreq) ** 0.5) * (getDotProduct(docTwoWordsFreq, docTwoWordsFreq) ** 0.5))
    if denominator == 0:
        return 0
    else:
        return getDotProduct(docOneWordsFreq, docTwoWordsFreq) / denominator

cosineSimilarity = getCosineSimilarity(docOneWordsFreq, docTwoWordsFreq)

if cosineSimilarity:
    print(cosineSimilarity)
else:
    print("Cosine similarity not defined! (Division by zero!)")

