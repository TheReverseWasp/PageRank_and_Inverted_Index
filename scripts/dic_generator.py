import json
import re

def main():
    r = "[a-z]+"
    with open("filenames.json", "r") as fn:
        filenames = json.load(fn)
    filenames = filenames["filenames"]
    dic_words = {}
    for f in filenames:
        print("[+] Iniciando " + f)
        with open("../Datos/" + f, "r") as datafile:
            while True:
                line = datafile.readline()
                if not line:
                    break
                line = line.lower()
                line = re.findall(r, line)
                if len(line) > 1:
                    dic_words[line[0]] = True
                    dic_words[line[1]] = True
    with open("../Resultados/Content/dicfile.json", "w") as dicfile:
        json.dump(dic_words, dicfile)

if __name__ == "__main__":
    main()
