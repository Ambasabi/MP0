#MP0
import random
import os
import string
import sys
from collections import Counter

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
                 "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
                 "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this",
                 "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has",
                 "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or",
                 "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
                 "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in",
                 "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
                 "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
                 "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will",
                 "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

delimiterList = {" ", "\t", ",", ";", ".", "?", "!", "-", ":", "@", "[", "]", "(", ")", "{", "}", "_", "*", "/"}

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    ret = []
    # TODO
    wikiFile = sys.stdin
    lines = wikiFile.readlines()

    # open a list to loop through all elements of indexes
    for currIndex in indexes:
        wikiTitle = lines[currIndex]
        i=0
        for c in wikiTitle:
            if i < len(wikiTitle):
                if c in delimiterList:
                    wikiTitle = wikiTitle[:i] + ' ' + wikiTitle[i + 1:]
            i += 1

        newSplit = wikiTitle.split()
        j = 0
        for item in newSplit:
            newSplit[j] = item.decode('utf-8', 'strict').lower()
            j += 1

        for splitWiki in newSplit:
            if splitWiki in stopWordsList:
                continue
            else:
                ret.append(splitWiki)

    # Credit to: https://stackoverflow.com/questions/3496518/python-using-a-dictionary-to-count-the-items-in-a-list
    dataDict = dict(Counter(ret))

    # Credit to: https://stackoverflow.com/questions/28839182/sorting-dictionary-by-value-and-lexicographical
    for key, value in sorted(dataDict.items(), key=lambda x: (-x[1], x[0]))[:20]:
        print("{}".format(key, value))


process(sys.argv[1])


