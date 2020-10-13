#!/usr/bin/env python3

import json
import re
import sys

r = "[a-z]+"
for k in sys.stdin:
    k = k[:-1]
    print("[+] Working in " + k)
    with open("filenames.json", "r") as fn:
        filenames = json.load(fn)
    filenames = filenames["filenames"]
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
    with open("../Resultados/map4/" + k + ".json") as kjson:
        json.dump(key_dic, kjson)
