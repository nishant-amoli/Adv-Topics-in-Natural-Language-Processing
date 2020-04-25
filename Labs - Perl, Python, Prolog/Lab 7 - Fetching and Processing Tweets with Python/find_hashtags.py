#!/local/bin/python3
import csv, re, pandas as pd, operator

# Taken from: https://github.com/s/preprocessor/blob/master/preprocessor/defines.py

class Patterns:
    URL_PATTERN=re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
    HASHTAG_PATTERN = re.compile(r'#\w*')
    MENTION_PATTERN = re.compile(r'@\w*')
    RESERVED_WORDS_PATTERN = re.compile(r'^(RT|FAV)')

    try:
        # UCS-4
        EMOJIS_PATTERN = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
        # UCS-2
        EMOJIS_PATTERN = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')

    SMILEYS_PATTERN = re.compile(r"(?:X|:|;|=)(?:-)?(?:\)|\(|O|D|P|S){1,}", re.IGNORECASE)
    NUMBERS_PATTERN = re.compile(r"(^|\s)(\-?\d+(?:\.\d)*|\d+)")

tweets_df = pd.read_csv('tweets.csv')
td = {}
for index, row in tweets_df.iterrows():
    screen_name = row['screen_name']
    if screen_name in td:
        ht = re.findall(Patterns.HASHTAG_PATTERN, row['text'])
        if ht:
            for i in ht:
                td[screen_name]['hashtags'].append(i)
        
        cle = re.sub(Patterns.URL_PATTERN, "", row['text'])
        cle = re.sub(Patterns.HASHTAG_PATTERN, "", cle)
        cle = re.sub(Patterns.EMOJIS_PATTERN, "", cle)
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", cle)
        cle = re.sub(Patterns.MENTION_PATTERN, "", cle.lower())
        cle = ''.join([c for c in cle if ord(c) < 128])
        cle = re.sub(r"\n", " ", cle)
        cle = re.sub(r"\s:\s", "", cle)
        
        td[screen_name]['text'].append(cle)
        
        
        words = re.findall(r"\b\w+\b", cle)
        for i in words:
            if i not in td[screen_name]['words_frequency']:
                td[screen_name]['words_frequency'][i] = 1
            else:
                td[screen_name]['words_frequency'][i] += 1
        
    else:
        td[screen_name] = {}
        
        td[screen_name]['hashtags'] = []
        ht = re.findall(Patterns.HASHTAG_PATTERN, row['text'])
        if ht:
            for i in ht:
                td[screen_name]['hashtags'].append(i)
                                                  
        td[screen_name]['text'] = []
        
        cle = re.sub(Patterns.URL_PATTERN, "", row['text'])
        cle = re.sub(Patterns.HASHTAG_PATTERN, "", cle)
        cle = re.sub(Patterns.EMOJIS_PATTERN, "", cle)
        cle = re.sub(Patterns.RESERVED_WORDS_PATTERN, "", cle)
        cle = re.sub(Patterns.MENTION_PATTERN, "", cle.lower())
        cle = ''.join([c for c in cle if ord(c) < 128])
        cle = re.sub(r"\n", " ", cle)
        cle = re.sub(r"\s:\s", "", cle)
        
        td[screen_name]['text'].append(cle)
        
        td[screen_name]['words_frequency'] = {}
        words = re.findall(r"\b\w*\b", cle)
        for i in words:
            if i not in td[screen_name]['words_frequency']:
                td[screen_name]['words_frequency'][i] = 1
            else:
                td[screen_name]['words_frequency'][i] += 1
                
for itr in td.keys():
    print(itr+":")
    print("* top 10 words: ",end="")
    c = 1
    del td[itr]['words_frequency'][""]
    for i in sorted(td[itr]['words_frequency'].items(), key=operator.itemgetter(1), reverse = True):
        if c < 10:
            print(i[0], end=", ")
            c += 1
        else:
            print(i[0])
            c += 1
            break
            
    print("* hashtags: ",end="")
    size = len(td[itr]['hashtags'])
    c = 1
    for i in td[itr]['hashtags']:        
        if c < size:
            print(i, end=", ")
            c += 1
        else:
            print(i)
            c += 1
            break
    print("* clean tweets: ")
    c = 1
    for i in td[itr]['text']:        
        print(c,". "+i)
        c+=1
    
