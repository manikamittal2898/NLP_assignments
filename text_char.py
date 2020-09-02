
import nltk

f = open("sample.txt", "r")

data=f.read()
# print(data)
 
words = len(data.split()) 
paras = len(data.split("\n\n"))
sents = len(nltk.sent_tokenize(data))

# printing result 
print ("The number of words in file are : " + str(words)) 
print ("The number of sentences in file are : " + str(sents))
print ("The number of paras in file are : " + str(paras)) 
