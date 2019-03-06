# CITY RECOMMENDER


# input file should be named as attributes.txt
# each attribute has to be listed in a new line
# last attribute must be the maximum price you are willing to pay per night
# output is the cities and crime indexes 


#%%  IMPORTING LIBRARIES AND CSVs
import csv
import pandas as pd
import nltk
import numpy as np
from nltk.tokenize import PunktSentenceTokenizer,RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import pairwise_distances
import warnings

#to ignore deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

#Please use xlsx file format to read the data
#I faced issues with csv
cities=pd.read_csv('/Users/Erkin/Desktop/McGill/Spring/Information Systems/project/cities.csv')
crime=pd.read_csv('/Users/Erkin/Desktop/McGill/Spring/Information Systems/project/crime_index.csv')
prices=pd.read_csv('/Users/Erkin/Desktop/McGill/Spring/Information Systems/project/cities_price.csv')
combined=pd.read_csv('/Users/Erkin/Desktop/McGill/Spring/Information Systems/project/Final_DF.csv')
combined['airbnb_daily']=combined['airbnb_(monthly)']/30
combined=combined.drop(['Unnamed: 0', 'City','airbnb_(monthly)'],axis=1)
cities=combined
#%%  PREPROCESSING THE TEXT


#Lowercasing
cities["lower_text"]=cities["text"].apply(lambda x : x.lower()) 


# tokenize
tokenizer = RegexpTokenizer(r'\w+')
cities["tokenized_text"] = cities["lower_text"].apply(lambda row: tokenizer.tokenize(row))

# lemmatize 
wnl = nltk.WordNetLemmatizer()

def lem(lst):
    list1=list()
    for i in lst : 
        list1.append(wnl.lemmatize(i))
    return list1

cities["lemmatized_text"]=cities["tokenized_text"].apply(lambda x : lem(x))


print("Number of rows with null values:")
print(cities.isnull().sum().sum())
cities=cities.dropna() 

#%%  PREPROCESSING THE ATTRIBUTES


attributes=list(line.strip() for line in open('attributes.txt'))
treshold=int(attributes[-1])
del attributes[-1]


attributes_lem=[]
for word in attributes:
    attributes_lem.append(wnl.lemmatize(word).lower())
    
attributes_text=" ".join(attributes_lem)
   
    
#%%  CALCULATING THE SCORES
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(min_df=0, ngram_range=(1, 2), stop_words='english', strip_accents='unicode', norm='l2',lowercase=True)

X=[" ".join(text) for text in cities["lemmatized_text"].values]
X.append(attributes_text)
tf_idf=tfidf_vectorizer.fit_transform(X)

tf_idf_array=tf_idf.toarray()

from sklearn.metrics.pairwise import linear_kernel
cosine_similarities = linear_kernel(tf_idf[-1], tf_idf[0:130]).flatten()

#%%  PRINTING OUTPUT
cities['similarity']=cosine_similarities
cities_selected=cities.loc[cities.airbnb_daily<treshold,:]
output=cities_selected[['city','Crime Index','similarity','airbnb_daily']].sort_values(by='similarity',ascending=False).head(3)
print(output[['city','Crime Index','airbnb_daily']])
