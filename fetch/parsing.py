import nltk
from nltk.tokenize import word_tokenize


def redditPass(text, id, score, time, parent) :
    # print("ghjk")
    text = word_tokenize(text)
    
    var = parser(parent, text) #send the text and link to parent to the parser and 
    #print(text)

"""
reddit comment -->
redditPass (--> parser) -->
storeformat -->
non-volitile mem
"""

def parser(parent, text) :
    text = nltk.pos_tag(text)
    nounList = []
    for list in text :
        if list[1] == "NN" : 
            # print(list[0])
            nounList.append(list[0])
    return nounList
    # print(text)
