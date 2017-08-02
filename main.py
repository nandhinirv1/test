# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:43:39 2017

@author: Nandhini
"""
from file_read import file_read
from search import search
import pandas as pd
import sys

obj=file_read()
var_train=obj.readin_variants("training_variants")
txt_train=obj.readin_text("training_text")
var_test=obj.readin_variants("test_variants")
txt_test=obj.readin_text("test_text")

var_train_l=var_train.values.tolist()
text_train_l=txt_train.values.tolist()
var_test_l=var_test.values.tolist()
text_test_l=txt_test.values.tolist()

print var_train_l[0] #2 is mutation
#print text_train_l[0] #1 is text
print var_test_l[0]
#print text_test_l[0]

sobj=search()
req_docs=[]
for i in range(0,len(var_train)):
    print i
    try:
        sur_words_g=list(sobj.search_word(var_train_l[i][1],text_train_l[i][1],20))
        sur_words_v=list(sobj.search_word(var_train_l[i][2],text_train_l[i][1],20))
        sur_words=sur_words_g+sur_words_v
        for j in range(0,len(sur_words)):
            req_docs.append(("".join(w+" " for w in sur_words[j]),var_train_l[i][3]))
    except:
        pass
    #print sur_words
    #sys.exit()
    
sents=[]
labels=[]
for i in range(0,len(req_docs)):
    sents.append(req_docs[i][0])  
    labels.append(req_docs[i][1])
    
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(encoding='latin1')
X_train = vectorizer.fit_transform(sents)
y_train=labels

from sklearn import svm
clf = svm.SVC()
clf.fit(X_train, y_train) 

x_to_be_pred=vectorizer.transform(["Regions analysis diagnostic antibodies overexpressing conformational tumors novel occur R570S by pRc activity melanoma disulfide ponatinib cells with were of values PML metastatic purchased"])

print clf.predict(x_to_be_pred[0])

