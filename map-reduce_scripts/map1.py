#!/usr/bin/env python3

import json
import re
import sys


r = "[a-z]+"
for k in sys.stdin:
    k = k[:-1]
    dw = {}
    # Number of refs per file
    drefs = {}
    # word and page Content
    print("Processing file: " + k)
    df = {}
    with open("../Datos/" + k, "r") as tf:
        drefs[k] = 0
        while True:
            line = tf.readline()
            if not line:
                break
            line = line.lower()
            line = re.findall(r, line)
            if len(line) > 1:
                drefs[k] += 1
                dw[line[0]] = k
                df[line[1]] = True
    with open("../Resultados/map1/" + k + "-content.json", "w") as js:
        json.dump(df, js)
    with open("../Resultados/map1/" + k + "-refs.json", "w") as refs:
        json.dump(drefs, refs)
    with open("../Resultados/map1/" + k + "-pos.json" , "w") as pos:
        json.dump(dw, pos)
