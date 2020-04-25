#!/local/bin/python3

from nltk import FreqDist
from nltk.corpus import treebank
from nltk import chunk, tag

# load treebank data
data = [treebank.words(i) for i in treebank.fileids()]
data = [tag.pos_tag(i) for i in data]

# chunk the data
chunkd_data = [chunk.ne_chunk(i) for i in data]
# select subtrees which are NE
chunkd_tree = [i.subtrees(filter = lambda x: x.label() in ["ORGANIZATION", "PERSON", "LOCATION", "DATE", "TIME", "MONEY", "PERCENT", "FACULTY", "GPE"]) for i in chunkd_data]
chunkd_trees = [[i for i in j] for j in chunkd_tree]
arr = []
for i in chunkd_trees:
    for j in i:
        arr.append(j)
word_fd = FreqDist([' '.join(word for word, pos in tree.leaves()) for tree in arr])
print("Three most common named entities are: ")
for token, freq in word_fd.most_common(3):
    print("%s : %d"%(token, freq))
