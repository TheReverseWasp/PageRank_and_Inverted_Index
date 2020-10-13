#!/usr/bin/env python3

import json
import re
import sys

r = "[a-z]+"
for f in sys.stdin:
    dic_words = {}
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
    with open("../Resultados/map3/" + f +"-dicfile.json", "w") as dicfile:
        json.dump(dic_words, dicfile)
