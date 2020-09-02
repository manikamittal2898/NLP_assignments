
import pandas as pd
import re
from collections import Counter
import easygui

df=pd.read_csv("MovieReviews.csv")
# print(list(reviews.columns))

def casefolding():
    df['Review']=df['Review'].str.lower()
    # print(df.head())

def stopwords_rem():
    df["Review"] = df['Review'].str.replace('[^\w\s]','')
    # print(df.head())

def tokenization(text):
    text = re.split('\W+', text)
    return text



casefolding()
stopwords_rem()
df['token'] = df['Review'].apply(lambda x: tokenization(x))
# print(df.head())
rows=len(df.index)
# print(rows)

pos=0
neg=0
tokens=[]
pos_tokens=[]
neg_tokens=[]
for ind in df.index: 
    if df['Class'][ind]=="positive":
        # print(type(df['Class'][ind]))
        pos+=1
        pos_tokens=pos_tokens+df['token'][ind]
        # print(pos)
    if df['Class'][ind]=="negative":
        neg+=1
        neg_tokens=neg_tokens+df['token'][ind]
    tokens=tokens+df['token'][ind]

p_pos=float(pos)/rows
p_neg=float(neg)/rows
uniq_tokens=list(set(tokens))

# print(tokens)
# print(p_pos)
# print(p_neg)
# print(uniq_tokens)

counts = Counter(tokens)
dictionary=(dict(counts))

prob=[]
for k,v in dictionary.items():
    if k in pos_tokens:
        prob.append(float(v+1)/(len(pos_tokens)+len(uniq_tokens)))
    else:
        prob.append(float(v+1)/(len(neg_tokens)+len(uniq_tokens)))

test = easygui.enterbox("Enter the movie review whose sentiment needs to be analysed")

test_tokens=tokenization(test)
test_pos=p_pos
test_neg=p_neg

for word in test_tokens:
    if word in pos_tokens:
        test_pos*=prob[uniq_tokens.index(word)]
    elif word in neg_tokens:
        test_pos*=1.0/(len(uniq_tokens))

    if word in neg_tokens:
        test_neg*=prob[uniq_tokens.index(word)]
    elif word in pos_tokens:
        test_neg*=1.0/(len(uniq_tokens))

# print(test_pos)
# print(test_neg)

if(test_pos>test_neg):
    print("Review is positive")
elif(test_pos<test_neg):
    print("Review is negative")
else:
    print("Review is neutral")

