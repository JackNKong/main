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
 

 
documents = [["Support",  "Strange", "Unusual",  "fantasy",  "conspiracy"],
["Nano", "Art,", "Reloaded"],
["MUTEK" , "VIRTUAL", "FESTIVAL" ,"STUDIO", "project"],
["SketchPad", "Pro", "Filmmaker","Storyboard",  "iPad"],
["APPLES", "LEMONS", "REVIEWS"],
["HEART", "ART",  "PORTRAIT", "DESIGN", "COLLECTION"],
["From","Snapshot" , "Art"],
["Local", "Autonomy" ,"Networks", "Find", "Each" ,"Other"],
["Morning", "Sketch", "Calendar"],
["Apathetic", "Fairy", "Tales", "Magical", "Stories","Sub-par","Delivery"]

 ] 


K = 4 

 
document_topic_counts = [Counter() for _ in documents] 
topic_word_counts = [Counter() for _ in range(K)] 

topic_counts = [0 for _ in range(K)] 

document_lengths = [len(d) for d in documents]
  
distinct_words = set(word for document in documents for word in document) 
W = len(distinct_words) 
D = len(documents) 

def p_topic_given_document(topic, d, alpha=0.1): 
    """the fraction of words in document _d_ 
     that are assigned to _topic_ (plus some smoothing)""" 

 
    return ((document_topic_counts[d][topic] + alpha) / 
            (document_lengths[d] + K * alpha)) 

 
def p_word_given_topic(word, topic, beta=0.1): 
    """the fraction of words assigned to _topic_ 
    that equal _word_ (plus some smoothing)""" 
 
    return ((topic_word_counts[topic][word] + beta) / 
           (topic_counts[topic] + W * beta)) 

 
def topic_weight(d, word, k): 
    """given a document and a word in that document, 
    return the weight for the k-th topic""" 

 
    return p_word_given_topic(word, k) * p_topic_given_document(k, d) 

 
def choose_new_topic(d, word): 
    return sample_from([topic_weight(d, word, k) 
                        for k in range(K)]) 

 
 
random.seed(0) 
document_topics = [[random.randrange(K) for word in document] 
                   for document in documents] 

 
for d in range(D): 
    for word, topic in zip(documents[d], document_topics[d]): 
        document_topic_counts[d][topic] += 1 
        topic_word_counts[topic][word] += 1 
        topic_counts[topic] += 1 
 
 
for iter in range(1000): 
    for d in range(D): 
        for i, (word, topic) in enumerate(zip(documents[d], 
                                              document_topics[d])): 
 
 
            # remove this word / topic from the counts 
           # so that it doesn't influence the weights 
            document_topic_counts[d][topic] -= 1 
            topic_word_counts[topic][word] -= 1 
            topic_counts[topic] -= 1 
            document_lengths[d] -= 1 
 
           # choose a new topic based on the weights 
            new_topic = choose_new_topic(d, word) 
            document_topics[d][i] = new_topic 

 
           # and now add it back to the counts 
            document_topic_counts[d][new_topic] += 1 
            topic_word_counts[new_topic][word] += 1 
            topic_counts[new_topic] += 1 
            document_lengths[d] += 1

for k, word_counts in enumerate(topic_word_counts): 
         for word, count in word_counts.most_common(): 
             if count > 0: print (k, word, count) 

topic_names = ["topic1", 
                    "topic2", 
                    "topic3", 
                    "topic4"] 
 
 
for document, topic_counts in zip(documents, document_topic_counts): 
         print (document) 
         for topic, count in topic_counts.most_common(): 
             if count > 0: 
                 print (topic_names[topic], count) 
         print()            
