#!/usr/bin/env python3

import json
import re
import sys

r = "[a-z]+"
for f in sys.stdin:
    f = f[:-1]
    print("[+] Procesando " + f)
    d = {}
    with open("../Datos/" + f, "r") as fc:
        while True:
            line = fc.readline()
            if not line:
                break
            line = line.lower()
            line = re.findall(r, line)
            if len(line) > 1:
                if not line[0] in d:
                    d[line[0]] = 0
                if not line[1] in d:
                    d[line[1]] = 0
                d[line[0]] += 1
                d[line[1]] += 1
    with open("../Resultados/map5/" + f + ".json", "w") as jf:
        json.dump(d, jf)
