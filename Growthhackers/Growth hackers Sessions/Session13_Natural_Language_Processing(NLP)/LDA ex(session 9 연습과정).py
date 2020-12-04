from __future__ import division 
import math, random, re 
from collections import defaultdict, Counter 
from bs4 import BeautifulSoup 
import requests 

def sample_from(weights): 
     total = sum(weights) 
     rnd = total * random.random()       # uniform between 0 and total 
     for i, w in enumerate(weights): 
         rnd -= w                        # return the smallest i such that 
         if rnd <= 0: return i           # sum(weights[:(i+1)]) >= rnd 
 
 
documents = [ 
     ["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"], 
     ["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"], 
     ["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"], 
     ["R", "Python", "statistics", "regression", "probability"], 
     ["machine learning", "regression", "decision trees", "libsvm"], 
     ["Python", "R", "Java", "C++", "Haskell", "programming languages"], 
     ["statistics", "probability", "mathematics", "theory"], 
     ["machine learning", "scikit-learn", "Mahout", "neural networks"], 
     ["neural networks", "deep learning", "Big Data", "artificial intelligence"], 
     ["Hadoop", "Java", "MapReduce", "Big Data"], 
     ["statistics", "R", "statsmodels"], 
     ["C++", "deep learning", "artificial intelligence", "probability"], 
     ["pandas", "R", "Python"], 
     ["databases", "HBase", "Postgres", "MySQL", "MongoDB"], 
     ["libsvm", "regression", "support vector machines"] 
 ] 


K = 4 

 
document_topic_counts = [Counter() for _ in documents] 




topic_word_counts = [Counter() for _ in range(K)] 
topic_counts = [0 for _ in range(K)] 
print(topic_counts)
document_lengths = [len(d) for d in documents]
distinct_words = set(word for document in documents for word in document) 

#print(document_topic_counts)
#print(topic_word_counts)
#print(document_lengths)
#print(distinct_words)
print()



W = len(distinct_words) 
D = len(documents) 

#print(W,D)
#print()


random.seed(0) 
document_topics = [[random.randrange(K) for word in document] 
                   for document in documents]
print(document_topics)


for d in range(D): 
    for word, topic in zip(documents[d], document_topics[d]): 
        document_topic_counts[d][topic] += 1 
        topic_word_counts[topic][word] += 1 
        topic_counts[topic] += 1
print()
print(document_topic_counts)

print()
print(topic_word_counts)
print(topic_counts)


def p_topic_given_document(topic, d, alpha=0.1): 
    return ((document_topic_counts[d][topic] + alpha) / 
            (document_lengths[d] + K * alpha)) 



def p_word_given_topic(word, topic, beta=0.1): 
    return ((topic_word_counts[topic][word] + beta) / 
           (topic_counts[topic] + W * beta)) 


     
def topic_weight(d, word, k):

    return p_word_given_topic(word, k) * p_topic_given_document(k, d) 

print(p_topic_given_document(2,0))
print(p_word_given_topic('Java',2))
print(topic_weight(0,'Java',2))
 
def choose_new_topic(d, word): 
    return sample_from([topic_weight(d, word, k) 
                        for k in range(K)]) 



for d in range(D): 
  for i, (word, topic) in enumerate(zip(documents[d],document_topics[d])):
            
             document_topic_counts[d][topic] -= 1 
             topic_word_counts[topic][word] -= 1 
             topic_counts[topic] -= 1 
             document_lengths[d] -= 1 
 

             new_topic = choose_new_topic(d, word)
             document_topics[d][i] = new_topic 

 
             document_topic_counts[d][new_topic] += 1 
             topic_word_counts[new_topic][word] += 1 
             topic_counts[new_topic] += 1 
             document_lengths[d] += 1



#print(document_topic_counts) 
#print(document_topic_counts[0][0])
#print(topic_word_counts)
#print(topic_word_counts[0]['Java'])
print(topic_counts)
#for k, word_counts in enumerate(topic_word_counts): 
#         for word, count in word_counts.most_common(): 
#             if count > 0: print (k, word, count)
