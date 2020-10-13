import json
import copy as cp
import time
import sys

def searchWord(word):
    answer = []
    with open("../Resultados/PageRank.json", "r") as pr:
        my_pr = json.load(pr)
    try:
        with open("../Resultados/map4/" + word + ".json", "r") as wordjson:
            wdic = json.load(wordjson)
    except:
        return ([["0", "0"]])
    for k, v in wdic.items():
        my_pr[k] *= v**2
    for k, v in my_pr.items():
        answer.append([k, v])
    answer.sort(key = lambda x: x[1])
    answer.reverse()
    return answer
