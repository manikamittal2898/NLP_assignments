# import statements
import pandas as pd
import re
from collections import Counter
import easygui

# Reading reviews
df=pd.read_csv("MovieReviews.csv")
# print(list(reviews.columns))

def casefolding(text):
    text=text.lower()
    return text
    
def punct_rem(text):
    text= text.replace('[^\w\s]','')
    return text
    # print(df.head())

def tokenization(text):
    text = re.split('\W+', text)
    return text


df['Review'] = df['Review'].apply(lambda x: casefolding(x))
df['Review'] = df['Review'].apply(lambda x: punct_rem(x))
df['token'] = df['Review'].apply(lambda x: tokenization(x))
# print(df.head())

# count no. of reviews
rows=len(df.index)
# print(rows)

pos=0
neg=0
tokens=[]
pos_tokens=[]
neg_tokens=[]
for ind in df.index: 
    if df['Class'][ind]=="positive":
        # count number of positive reviews in training set
        pos+=1
        # make list of tokens in postive reviews
        pos_tokens=pos_tokens+df['token'][ind]
        
    if df['Class'][ind]=="negative":
        neg+=1
        neg_tokens=neg_tokens+df['token'][ind]
    # make list of all tokens
    tokens=tokens+df['token'][ind]
# calculating prior probabilities
p_pos=float(pos)/rows
p_neg=float(neg)/rows

# removing empty strings from list of tokens
while("" in pos_tokens) : 
    pos_tokens.remove("") 
while("" in neg_tokens) : 
    neg_tokens.remove("") 
while("" in tokens) : 
    tokens.remove("") 

# list of unique tokens
uniq_tokens=list(set(tokens))
# print(tokens)
# print(pos)
# print(neg)
# print(pos_tokens)
# print(neg_tokens)
# print(len(uniq_tokens))

# creating dictionary of tokens and their frequencies in the training set
pos_counts = Counter(pos_tokens)
posdict=(dict(pos_counts))
neg_counts = Counter(neg_tokens)
negdict=(dict(neg_counts))

# calculating likelihood probabilities of tokens
posprob=[]
for k,v in posdict.items():
    posprob.append(float(v+1)/(len(pos_tokens)+len(uniq_tokens)))
    # print(str(k)+" "+ str(v+1)+" "+str((len(pos_tokens)+len(uniq_tokens))))
negprob=[]
for k,v in negdict.items():
    negprob.append(float(v+1)/(len(neg_tokens)+len(uniq_tokens)))
    # print(str(k)+" "+ str(v+1)+" "+str((len(neg_tokens)+len(uniq_tokens))))

# Testing
test = easygui.enterbox("Enter the movie review whose sentiment needs to be analysed.")
test=casefolding(test)
test=punct_rem(test)
test_tokens=tokenization(test)
test_pos=p_pos
test_neg=p_neg

# print(test_pos)
# print(test_neg)

for word in test_tokens:
    if word in pos_tokens:
        test_pos*=posprob[list(posdict).index(word)]
        # print(posprob[list(posdict).index(word)])
    elif word in neg_tokens:
        test_pos*=1.0/(len(uniq_tokens)+len(pos_tokens))
        # print(1.0/(len(uniq_tokens)+len(pos_tokens)))
    if word in neg_tokens:
        test_neg*=negprob[list(negdict).index(word)]
    elif word in pos_tokens:
        test_neg*=1.0/(len(uniq_tokens)+len(neg_tokens))
    # print(test_neg)
print("Postive class : "+str(test_pos))
print("Negative class : "+str(test_neg))

if(test_pos>test_neg):
    print("Review is positive")
else:
    print("Review is neutral")


