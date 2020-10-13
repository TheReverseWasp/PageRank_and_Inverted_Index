import json
import re

def main():
    with open("../Resultados/Content/dicfile.json", "r") as dicfile:
        dic_words = json.load(dicfile)
    r = "[a-z]+"
    with open("filenames.json", "r") as fn:
        filenames = json.load(fn)
    filenames = filenames["filenames"]
    acum = 0
    for k, v in dic_words.items():
        acum += 1
    actual = 0
    for k, v in dic_words.items():
        print("[+] Currently word " + k, actual, "of", acum)
        actual += 1
        key_dic = {}
        for f in filenames:
            key_dic[f] = 0
            with open("../Datos/" + f, "r") as actual_file:
                while True:
                    line = actual_file.readline()
                    if not line:
                        break
                    line = line.lower()
                    line = re.findall(r, line)
                    if len(line) > 1:
                        if line[0] == k:
                            key_dic[f] += 1
                        if line[1] == k:
                            key_dic[f] += 1
        with open("../Resultados/Content/words/" + k + ".json") as kjson:
            json.dump(key_dic, kjson)

if __name__ == "__main__":
    main()
