import nltk
from nltk.corpus import stopwords


p=open("positive.txt","r")
pos=p.readlines()
n=open("negative.txt","r")
neg=n.readlines()

x=["positive"]*len(pos)
y=["negative"]*len(neg)
ptweets=zip(pos,x)
ntweets=zip(neg,y)
print "\n"
for i in ptweets:
    print i
print "\n"
for i in ntweets:
    print i

tweetsw=[]
for(line,senti)in ptweets+ntweets:
    eachone=[i.lower() for i in line.split()]
    tweetsw.append((eachone,senti))

for i in tweetsw:
    print "\n"
    print i

def frequencydist():
    words=[]
    for (i,k) in tweetsw:
        words.extend(i)
    f=nltk.FreqDist(words)
    print f.keys()
    return f

f=frequencydist()
customstopwords=["bangalore","shahrukh khan","salman han","love","like","icecream"] #normal words that doesnt signify positivity or negativity
f= [i for i in f if not i in stopwords.words('english')]
f= [i for i in f if not i in customstopwords]

print "\n"
print f

def featureextractor(document):
    document=set(document)
    features={}
    for i in f:
        features['contains(%s)'%i]=(i in document)
    return features
trainingset=nltk.classify.apply_features(featureextractor,tweetsw)
print "\n"
print trainingset
classifier =nltk.NaiveBayesClassifier.train(trainingset)
print"\n"
while 1:
    z=raw_input("WELCOME \n SENTI \n Enter a sentence : \n")
    if z=='exit':
        break
    print classifier.classify(featureextractor(z.strip().split()))
#classifier.show_most_informative_features(n=12)
p.close()
n.close()
