# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13q68d63zJlXhugGpS2bZB6DaRu1VfIlw
"""

import numpy as np
import re
import nltk
import string
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import LancasterStemmer
from nltk.corpus import wordnet
from nltk.tag import pos_tag

#Holds all document in DocArray with .A section 

documentList = []
vectorDocument = []
string = ""
lock = False
lock2 = True
i = 0;

# load data
filename = '../Nlp/DataSet/moreCleanDocuments.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

with open("../Nlp/DataSet/moreCleanDocuments.txt", "r") as a_file:
  for line in a_file:
    for word in line.split():  
        
        if  word == ".W" or word == ".T" or word ==".K" or word == ".A":
            lock = True
            lock2 = True
        elif word == ".B":
            lock2 = False
                   
        elif word == ".I":
            if lock == True:
                documentList.append(string)
                string = ""
            lock = False
           
    if lock == True and lock2 == True and word != ".W" and word != ".T" and word != ".K" and word != ".A" :      
        string = string + line
        
print("doc --->",documentList[324])

# Split queries into QueryArray without .N section   #

queryList = []
string = ""
lock = False
lock2 = True

i = 0;

with open("../Nlp/DataSet/queries.txt", "r") as a_file:
  for line in a_file:
    for word in line.split():  
        
        if  word == ".W" :
            lock = True
            lock2 = True
        elif word == ".A" or word == ".N":
            lock2 = False       
        elif word == ".I" :
            if lock == True:
                queryList.append(string)
                string = ""
            lock = False
    
    if lock == True and lock2 == True and word != ".W" and word !=".N"  :      
        string = string + line
    
print("selected queries -->",queryList[62])    

# Fetch Common words

filename = '../Nlp/DataSet/common_vocab.txt'
file = open(filename, 'rt')
cmnWords = file.read()
file.close()        

PreparedCommonWords = []
print("*****************************")

words = cmnWords.split()
# prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))
# remove punctuation from each word
stripped = [re_punc.sub('', w) for w in words]
PreparedCommonWords = stripped

import string
from nltk.corpus import wordnet
import nltk
from nltk.stem import WordNetLemmatizer
#  data processing for docs and queries such as remove punctation, lower case converts, stemming
finalPreparedQueries = []
finalPreparedDocuments = []

#print(queryList)
def removePunc (sentence):
    tokens = nltk.word_tokenize(sentence)
#    sentence_words
    new_sentence=[]
    stemmedLists = []
#    for word in sentence_words:  
    tokens = [w.lower() for w in tokens]
# prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
# remove punctuation from each word
    stripped = [re_punc.sub('', w) for w in tokens]
    for w in stripped:
        if not w in PreparedCommonWords:
            stemmedLists.append(w)  
    for index in stemmedLists:
        new_sentence.append(index)
        new_sentence.append(" ")
    return "".join(new_sentence)

# Part 1 - Data processing of Queries

for line in queryList:
    finalPreparedQueries.append(removePunc(line))
    
print(finalPreparedQueries[63])
print("*****")
print(queryList[63])

# # Part 2 - Data processing of Documents

for line in documentList:
    finalPreparedDocuments.append(removePunc(line))
    
print(finalPreparedDocuments[2298])
print("******")
print(documentList[2298])

# Lemmatize Part #   
lemmatizer = WordNetLemmatizer()
lemmanedDocuments = []
lemmanedQueries = []
def lemmatize_all(sentence):
    wnl = WordNetLemmatizer()
    for word, tag in pos_tag(word_tokenize(sentence)):
       
        if tag.startswith("NN"):
            yield wnl.lemmatize(word, pos='n')
        elif tag.startswith('VB'):
            yield wnl.lemmatize(word, pos='v')
        elif tag.startswith('JJ'):
            yield wnl.lemmatize(word, pos='a')
        else:
            yield word


print(' '.join(lemmatize_all("programming")))
# apply Lemmatize stemming to query 
for line in finalPreparedQueries:
    lemmanedQueries.append(' '.join(lemmatize_all(line)))

    
print(finalPreparedQueries[63])
print("**********")
print(lemmanedQueries[63])
print("---------------------------------------")
# apply Lemmatize stemming to documents   
for line in finalPreparedDocuments:
    lemmanedDocuments.append(' '.join(lemmatize_all(line)))

print(finalPreparedDocuments[10])
print("**********")
print(lemmanedDocuments[10])

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


resultSet1 = [1410  ,1572  ,1605  ,2020 ,2358]
resultSet2 = [2434 ,2863  ,3078]
resultSet3 = [1134  ,1613  ,1807 ,1947 ,2290  ,2923]
resultSet4 = [1749,1811,2256,2371 ,2597 ,2796 ,2912 ,3043 ,3073 ,3082 ,3127 ,3128 ]
resultSet5 = [756,1307,1502 ,2035 ,2299 ,2399 ,2501 ,2820]
resultSet6 = [1543,2078,2828]
resultSet7 = [1198,1338  ,1877  ,1960  ,2150  ,2228  ,2256  ,2280  ,2320  ,2342  ,2376  ,2482  ,2578  ,2597  ,2618  ,2685  ,2700  ,2777  ,2865  ,2866  ,2895  ,2912  ,2941  ,3043,3082,3128,3141,3148]
resultSet8 = [2625,2849,3032]
resultSet9 = [2372 ,2632 ,2870 ,2876 ,3068 ,3111 ,3128 ,3158 ,3177]
resultSet10 = [46 ,141  ,392  ,950  ,1158 ,1198  ,1262  ,1380  ,1471  ,1601  ,1613  ,1747  ,1795  ,1811  ,2060  ,2150  ,2256  ,2289  ,2342  ,2376  ,2433  ,2618  , 2664  ,2685  ,2700  ,2714  ,2777  ,2785  ,2851  ,2895  ,2896  ,2912 ,3039 ,3075 ,3156]
resultSet11 = [1043 ,1188  ,1306  ,1358  ,1396  ,1491 ,1923  ,2246  ,2316  ,2527  ,2699  ,2710  ,2715  ,2716  ,2906  ,2923  ,2956  ,3073  ,3150]
resultSet12 = [1523 ,2080 ,2246  ,2629  ,3127]
resultSet13 = [115 ,1223  ,1231  ,1551  ,1625  ,1795  ,1807  ,1947  ,2495  ,2579  ,2897]
resultSet14 = [74 ,117  ,232  ,776 ,827  ,850 ,851 ,852 ,854 ,855 ,856  ,857 ,858 ,860 ,861 ,862 ,864  ,865 ,866  ,1175 ,1724  ,1919  ,1956 ,1969 ,1980 ,1997 ,2017  ,2041 ,2108  ,2118  ,2146 ,2176 ,2191  ,2272  ,2337  ,2348  ,2397  ,2563 ,2664 ,2679 ,2714 ,2716 ,3075 ,3187]
resultSet15 = [1231 ,1551 ,1613 ,1947  ,2263  ,2495 ,2598  ,2685  ,2701 ,2880]
resultSet16 = [1746 ,1749 ,1828 ,1854 ,1960 ,2070  ,2114 ,2342 ,2376  ,2378 ,2500 ,2632 ,2817 ,2912 ,3073 ,3105 ,3148]
resultSet17 = [115 ,405  ,1134  ,1223  ,1231  ,1535 ,1551  ,1613  ,1807  ,1934  ,1947  ,2290  ,2495  ,2579 ,2586  ,2923]
resultSet18 = [1158 ,1215 ,1262  ,1471 ,1613  ,1811  ,2060  ,2175  ,2413  ,2433  ,2685]
resultSet19 = [141 ,863 ,950 ,1601 ,2266 ,2664 ,2714 ,2973 ,3075 ,3156 ,3175]
resultSet20 = [1563 ,2695 ,2986]
resultSet21 = [1429 ,1847  ,2189  ,2490  ,2603  ,2701  ,2702  ,2703  ,2932  ,3018 ,3139]
resultSet22 = [2369 ,2384  ,2441  ,2473  ,2564  ,2637  ,2638  ,2678 ,2692 ,2751  ,2760  ,2761  ,2827  ,2828 ,2829 ,3116 ,3149]
resultSet23 = [2578  ,2849  ,3137  ,3148]
resultSet24 = [268  ,1696  ,1892  ,2069  ,2123 ,2297  ,2373  ,2667  ,2862  ,2970 ,2996  ,3078  ,3098]
resultSet25 = [268,757 ,963 ,1408  ,1518 ,1526 ,1533 ,1572 ,1653 ,1698 ,1719 ,1805 ,1892 ,1901 ,2085 ,2095 ,2218  ,2277 ,2318 ,2319  ,2358 ,2373  ,2434 ,2452 ,2535 ,2582  ,2667  ,2668 ,2669  ,2681 ,2741 ,2765 ,2798  ,2818 ,2831 ,2859 ,2862 ,2863  ,2881 ,2918  ,2928  ,2984  ,2988  ,2996  ,3006  ,3048 ,3059  ,3067 ,3088  ,3089  ,3119]
resultSet26 = [1071 ,1198 ,1338 ,1749 ,1828 ,1854 ,1960 ,2080 ,2150 ,2256 ,2320 ,2342 ,2376 ,2379 ,2541 ,2597 ,2618 ,2632 ,2700 ,2740 ,2777 ,2851  ,2866 ,2912 ,2938 ,3039 ,3043 ,3048 ,3082 ,3128]
resultSet27 = [1641 ,1642 ,1750 ,1752 ,1879 ,1884 ,1901 ,2095  ,2297 ,2435 ,2481 ,2498 ,2560 ,2596 ,2669 ,2734 ,2747 ,2768 ,2798 ,2818 ,2859 ,2864 ,2902 ,2918 ,2955 ,2983 ,2988 ,3000  ,3052]
resultSet28 = [2578 ,2849  ,2890 ,2949 ,3032]
resultSet29 = [377 ,513 ,610 ,935 ,1094 ,1420 ,1537 ,1538 ,1539 ,1840 ,1841 ,1967 ,2028 ,2089 ,2120 ,2462 ,2927  ,2932  ,3037]
resultSet30 = [1926 ,2486 ,2786 ,2917]
resultSet31 = [2125 ,3047]
resultSet32 = [366 ,1145,3139]
resultSet33 = [2805]
resultSet34 = []
resultSet35 = []
resultSet36 = [1265 ,1350 ,1683 ,1768 ,1787 ,1825 ,1836 ,2015 ,2084 ,2110 ,2179  ,2340 ,2423 ,2702 ,2708 ,2733 ,2824 ,2836 ,2986 ,3094]
resultSet37 = [2265 ,2377 ,2558 ,2625 ,2632 ,2651 ,2738 ,2840 ,2939 ,2941 ,3144 ,3148]
resultSet38 = [2265 ,2558 ,2625 ,2632 ,2651 ,2868 ,2939 ,2940,2941 ,2956 ,2957 ,2958 ,2960 ,3031 ,3103 ,3150]
resultSet39 = [1693 ,1861 ,2126 ,2265 ,2317 ,2558 ,2625 ,2632 ,2651 ,2939 ,2941,3031]
resultSet40 = [1614 ,2126 ,2148 ,2265 ,2651 ,2939,2940 ,2941,2956 ,2958]
resultSet41 = []
resultSet42 = [963 ,1069 ,1518 ,1572 ,1653 ,1805 ,1827 ,1884 ,2022 ,2085 ,2151 ,2247,2318 ,2344 ,2522 ,2542 ,2749 ,2951 ,2984 ,3048 ,3072]
resultSet43 = [122 ,266 ,297 ,462 ,1113 ,1325 ,1528,1554 ,1686 ,1697 ,2004 ,2195 ,2201 ,2211 ,2382,2400 ,2421 ,2514 ,2523 ,2655 ,2687,2751 ,2754,2771 ,2788 ,2811 ,2826 ,2827 ,2828 ,2829 ,2841 ,2883 ,2910 ,2913 ,2924 ,2994 ,3047 ,3062 ,3116 ,3149 ,3172]
resultSet44 = [1804 ,1891 ,2004 ,2382 ,2514 ,2523 ,2547 ,2687 ,2751 ,2771,2827 ,2829 ,2910 ,2913 ,2924 ,3013 ,3047]
resultSet45 = [268 ,1831 ,1935,2140 ,2257 ,2359 ,2360 ,2452 ,2493 ,2669 ,2680 ,2716 ,2765 ,2816 ,2878 ,2882 ,2900 ,2964 ,2965 ,2969 ,3002 ,3058 ,3129,3137 ,3152 ,3168]
resultSet46 = []
resultSet47 = []
resultSet48 = [149 ,1353 ,1666 ,1729 ,1797 ,1863 ,2073 ,2223 ,2226 ,2285 ,2325,2589]
resultSet49 = [1152 ,1515 ,1681 ,2127 ,2390,2561,2795 ,2832]
resultSet50 = []
resultSet51 = []
resultSet52 = []
resultSet53 = []
resultSet54 = []
resultSet55 = []
resultSet56 = []
resultSet57 = [3077]
resultSet58 = [432 ,536,1293 ,1344 ,1398,1411,1420 ,1445 ,1619 ,1629 ,1631 ,1691 ,1709 ,1812 ,1944 ,2098 ,2115 ,2122 ,2123 ,2249 ,2349 ,2395 ,2634 ,2636 ,2719 ,2731 ,2825 ,3159 ,3166 ,3167]
resultSet59 = [440 ,944 ,1112 ,1170 ,1235 ,1314 ,1324 ,1456 ,1457 ,1700 ,1785 ,1786 ,1855 ,1860 ,1885 ,1973 ,2018,2032 ,2033 ,2092 ,2107 ,2111 ,2127 ,2203 ,2251 ,2274 , 2359 ,2412 ,2524 ,2530 ,2532 ,2537 ,2543 ,2552 ,2559 ,2631 ,2673 ,2905 ,2974,2991 ,3053 ,3083 ,3126]
resultSet60 = [2023 ,2046 ,2198 ,2377 ,2406 ,2452 ,2493 ,2516 ,2526 ,2593 ,2710 ,2715 ,2716 ,2717 ,2718 ,2765 ,2816 ,2817 ,2882 ,2957 ,2959 ,2960 ,2964 ,2976 ,3087 ,3137 ,3147]
resultSet61 = [239 ,440 ,634 ,1032 ,1236 ,1457 ,1514 ,1675 ,1830 ,1927 ,1976 ,2160 ,2307,2363 ,2451 ,2452 ,2524 ,2575 ,2631 ,2641,2711 ,2765 ,2965 ,2966 ,2976 ,2990 ,3001 ,3012 ,3134 ,3168 ,3169]
resultSet62 = [950,1601 ,1811 ,2289 ,2664 ,2714 ,3075 ,3156]
resultSet63 = [950 ,1601 ,1795 ,1811 ,2266 ,2289 ,2557 ,2664 ,2714 ,2973 ,3075 ,3156]
resultSet64 = [2651]

vectorizer = TfidfVectorizer(analyzer='word',
                     min_df = 0, sublinear_tf=True, ngram_range=(1,1))
# tokenize and build vocab
VectorizedDoc=lemmanedDocuments
fitted_docs = vectorizer.fit(VectorizedDoc)
# summarize

selected_query = 63
selectedSet = resultSet64

print(VectorizedDoc[1004])
print("-----------------------")
print(lemmanedQueries[selected_query])

print("**************")

print(VectorizedDoc[962])
print("-----------------------")
print(lemmanedQueries[selected_query])

vector1 = vectorizer.transform([lemmanedQueries[selected_query]])
vector2 = vectorizer.transform([VectorizedDoc[266]])

print(vector1.shape)
print(vector1.toarray())
print(vector2.shape)
print(vector2.toarray())
cos_sim = cosine_similarity(vector1,vector2).flatten()
print(cos_sim.sum())
similartiy_matrix = [0] * len(VectorizedDoc)

def calculate_tfidf(queries, docs, vectorizer, index):
    tfidf_matrix = [0] * len(VectorizedDoc)
    
    docs_tfidf = vectorizer.fit(docs)
    query_tfidf = vectorizer.transform([queries[index]])
    for g in range(len(docs)):    
        doc_tfidf =  vectorizer.transform([docs[g]])
        cos_sim = cosine_similarity(query_tfidf,doc_tfidf).flatten()
        tfidf_matrix[g] = cos_sim.sum()
    return tfidf_matrix

similartiy_matrix = calculate_tfidf(lemmanedQueries, VectorizedDoc, fitted_docs, selected_query)
print("Similarity Score --->", similartiy_matrix[1157])

# retrive top K documents

validResults = []
def retrive_doc_for_query(queryNo, K):
    k_return = []
    k_return = similartiy_matrix
    index_return = [0] * len(similartiy_matrix)
    
    for h in range(len(lemmanedDocuments)):
        index_return[h] = h+1
    for i in range(len(k_return)-1): 
        for j in range(len(k_return)-i-1):
            if k_return[j] < k_return[j+1] :
                
                k_return[j], k_return[j+1] = k_return[j+1], k_return[j] 
                index_return[j], index_return[j+1] = index_return[j+1], index_return[j]
                
    for index in range(K):
        print(index_return[index], "-->", k_return[index])
   
    print("***************************")

    for i in range(K):
        for j in range(len(selectedSet)):
            if index_return[i] == selectedSet[j]:
                validResults.append(selectedSet[j])
                print(selectedSet[j])
                break
    return index_return[:20]

returnedDocs = retrive_doc_for_query(selected_query,20)

calc = 0
y_true = returnedDocs
y_resultSets = validResults

for i in range(len(y_resultSets)):
    for j in range(len(y_true)):
        if y_true[j] == y_resultSets[i]:
            calc = calc + (i+1)/(j+1)
            
print("\n")            
avg = calc / len(validResults)
print("Avg(P) =","%.2f" % avg)

# Calculate Mean Average precision for selected document
sumAvg = 0.30 + 0.92 + 0.17 + 0.83 + 0.23 + 0.58 + 0.84 + 0.25 + 0.23 + 0.95 + 0.90 + 0.60 + 0.61 + 0.58 + 0.45 + 0.58 + 0.40 + 0.22 + 0.50 + 0.29 + 0.20 + 0.82 + 0.95 + 0.76 + 0.70 + 0.14 + 0.58 + 0.95 + 0.99 + 0.27 + 0.33 + 0.63 + 0.64 + 0.34 + 0.70 + 0.56 + 0.73 + 0.33 + 0.35 + 0.75 + 0.80 + 0.48 + 0.25 + 1 + 0.81 + 0.72 + 0.55 + 0.86 + 0.48 + 1                
MAP = sumAvg/64
MAP





