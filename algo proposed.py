#importing packages
import nltk
from nltk import sent_tokenize,word_tokenize
from textblob.classifiers import NaiveBayesClassifier
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd

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
def train_by_religion(file_religion,file_01,file_wordwise,feature_set):
    f1=open(file_religion,'r')
    f2=open(file_01,'r')
    #f3=open(file_wordwise,'r')  .......... yahan pandas ka code dalnaaaa
    l1=f1.read()
    arr=sent_tokenize(l1)
    l2=f2.read()
    arr2=word_tokenize(l2)
    f4=open("agnelvalentina.txt",'r')
    f5=open("agnelvalentina01.txt",'r')
    f6=open("chandramani.txt",'r')
    f7=open("chandramani01.txt",'r')
    f8=open('Maria Soosai Vs. Clara Mary.txt','r')
    f9=open('Maria Soosai Vs. Clara Mary01.txt','r')
    f10=open('prakashmartin.txt','r')
    f11=open('prakashmartin01.txt','r')
    f12=open('reynoldrajamani.txt','r')
    f12=open('reynoldrajamani01.txt','r')
    f13=open('sjayakumar.txt','r')
    f14=open('sjayakumar01.txt','r')
    for i in range(0,len(arr2)):
        li1.append(tuple((arr[i],arr2[i])))
    f1.close()
    f2.close()
    for i in range(40,90,10):
        length=(i/100)*len(li1)
        traning_set=li1[:length]
        testing_set=li1[length:]
        #x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
        #model= NaiveBayesClassifier(training_set)
        #classifier = GaussianNB()
        #classifier.fit(training_set,y_train)
        print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)   
    
def detect_religion ():
    file1=open("muslim surname.txt")
    file2=open("hindu surname.txt")
    file3=open("christian surname.txt")
    #inputcase=open('myinput.txt','r')
    muslim_feature=['cruelty', 'physical abuse', 'desertion', 'domestic voilence', 'alimony', 'maintenance', 'imprisonment for 7 years or more', 'insane', 'mahr', 'verbal abuse', 'emotional abuse', 'Given into marriage', 'Triple talaq', 'Dissolution of marriage']
    hindu_feature=['cruelty', 'physical abuse', 'desertion', 'domestic voilence','forcible conversion', 'bigamy','mutual consent','imprisonment for 7 years or more', 'insane'  ,'impotent','sexual disease','assault', 'dowry','unsound mind'  ,'adultery'	,'leave parents','rape',"sexual dissatisfaction"]
    christian_feature=['cruelty', 'physical abuse', 'desertion', 'domestic voilence','forcible conversion', 'bigamy','mutual consent','insane'  ,'impotent','sexual disease','assault','unsound mind'  ,'adultery'	,'special marriage act','rape',"sexual dissatisfaction",'misbehave','']

    x ="Barros"#input("Enter your surname   ")
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
    if binarySearch(n, 0, len(n)-1, x)!= -1:
        train_by_religion("muslim.txt","muslim01.txt",'mu.csv',muslim_feature)

    elif binarySearch(m, 0, len(m)-1, x)!=-1:
        train_by_religion("hindu.txt","hindu01.txt",'Hindu_w.csv',hindu_feature)
     
    
    elif binarySearch(p, 0, len(p)-1, x)!=-1:
        train_by_religion("AABalasundaram.txt","AABalasundaram01.txt",'Christian_w.csv',christian_feature)

detect_religion()
    
