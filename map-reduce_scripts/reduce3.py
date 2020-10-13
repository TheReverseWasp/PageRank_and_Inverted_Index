#!/usr/bin/env python3

from otherfuns import *

def main():
    with open("filenames.json", "r") as fn:
        filenames = json.load(fn)
    filenames = filenames["filenames"]
    dic_words = {}
    for f in filenames:
        with open("../Resultados/map3/" + f +"-dicfile.json", "r") as dicfile:
            temp_dic = json.load(dicfile)
        dic_words = joinDictionaries(dic_words, temp_dic)
    with open("../Resultados/reduce3/dicfile.json", "w") as dicfile:
        json.dump(dic_words, dicfile)

if __name__ == "__main__":
    main()
