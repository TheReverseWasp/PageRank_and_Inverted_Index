#!/usr/bin/env python3
import json

def main():
    with open("../Resultados/reduce3/dicfile.json", "r") as df:
        dic_dic = json.load(df)
    with open("filenames.json", "r") as fn:
        filenames = json.load(fn)
    fn = filenames["filenames"]
    acum = 0
    total = 0
    for k, v in dic_dic.items():
        total += 1
    for k, v in dic_dic.items():
        print("[+] Palabra " + k + " | ", acum, "de", total)
        acum += 1
        key_dic = {}
        for f in fn:
            with open("../Resultados/map5/" + f + ".json", "r") as jf:
                tempd = json.load(jf)
            if not f in key_dic:
                if not k in tempd:
                    key_dic[f] = 0
                else:
                    key_dic[f] = tempd[k]
        with open("../Resultados/reduce5/" + k + ".json", "w") as kjson:
            json.dump(key_dic, kjson)

if __name__ == "__main__":
    main()
