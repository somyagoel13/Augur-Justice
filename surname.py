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
file1=open("muslim surname.txt")
file2=open("hindu surname.txt")
file3=open("christian surname.txt")
x =input("Enter your surname   ")
y=input("Enter your religion   ")
x=x.capitalize()
y=y.capitalize()
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
resultm = binarySearch(n, 0, len(n)-1, x)
resulth = binarySearch(m, 0, len(m)-1, x)
resultc = binarySearch(p, 0, len(p)-1, x)
if resultm!= -1 or y=="Muslim": 
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
    print("Also see: Dissolution of Musim Marriage")
elif resulth!=-1 or y=="Hindu": 
    f1=open("hindu.txt")
    f2=open("hindu01.txt")
    l1=f1.read()
    arr=sent_tokenize(l1)
    l2=f2.read()
    arr2=word_tokenize(l2)
    for i in range(0,len(arr)):
        li1.append(tuple((arr[i],arr2[i])))
    f1.close()
    f2.close()
    print("Also see: Hindu Marriage Act")
elif resultc!=-1 or y=="Christian":
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
    print("Also see: Indian Divorce Act")
mycase=input("Enter your case")
c1=0
c2=0
model= NaiveBayesClassifier(li1)
#print(model.classify(mycase))
case=sent_tokenize(mycase)
for i in range(0,len(case)):
    temp=model.classify(case[i])
    if temp=="0" or temp==0:
        c1=c1+1
    else:
        c2=c2+1
print("Probability of winning case",c1/(c1+c2))
