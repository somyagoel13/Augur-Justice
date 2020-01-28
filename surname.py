import nltk
from nltk import sent_tokenize,word_tokenize
from textblob.classifiers import NaiveBayesClassifier
def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid =int( l + (r - l)/2)    
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid+1, r, x) 
    else: 
        return -1
def detect_religion:
    
file1=open("muslim surname.txt")
file2=open("hindu surname.txt")
file3=open("christian surname.txt")
x =input("Enter your surname   ")
x=x.capitalize()
a=file1.read()
b=file2.read()
c=file3.read()
n=[]
m=[]
p=[]
li1=[]
n=word_tokenize(a)
m=word_tokenize(b)
p=word_tokenize(c)
file1.close()
file2.close()
file3.close()
if binarySearch(n, 0, len(n)-1, x)!= -1 or y=="Muslim": 
    f1=open("muslim.txt")
    f2=open("muslim01.txt")
    l1=f1.read()
    arr=sent_tokenize(l1)
    l2=f2.read()
    arr2=word_tokenize(l2)
    for i in range(0,len(arr2)):
        li1.append(tuple((arr[i],arr2[i])))
    f1.close()
    f2.close()
elif binarySearch(m, 0, len(m)-1, x)!=-1 or y=="Hindu": 
    f1=open("hindu.txt")
    f2=open("hindu01.txt")
    l1=f1.read()
    arr=sent_tokenize(l1)
    l2=f2.read()
    arr2=word_tokenize(l2)
    for i in range(0,len(arr)):
        li1.append(tuple((arr[i],arr2[i])))
    for i in range(40,100,10):
        length=(i/100)*len(li1)
        traning_set=li1[:length]
        testing_set=li1[length:]
        model= NaiveBayesClassifier(training_set)
        print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)        
    f1.close()
    f2.close()
elif binarySearch(p, 0, len(p)-1, x)!=-1 or y=="Christian":
    f1=open("Christian.txt")
    f2=open("christian01.txt")
    l1=f1.read()
    arr=sent_tokenize(l1)
    l2=f2.read()
    arr2=word_tokenize(l2)
    for i in range(0,len(arr)):
        li1.append(tuple((arr[i],arr2[i])))
    f1.close()
    f2.close()
    
#mycase=input("Enter your case")
c1=0
c2=0
model= NaiveBayesClassifier(li1)
"""print(model.classify(mycase))
case=sent_tokenize(mycase)
for i in range(0,len(case)):
    temp=model.classify(case[i])
    if temp=="0":
        c1=c1+1
    else:
        c2=c2+1
print("Probability of winning case",c1/(c1+c2))"""
