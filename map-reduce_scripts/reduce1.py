#!/usr/bin/env python3

import json
from otherfuns import *

def main():
    with open("filenames.json", "r") as fn:
        filenames = json.load(fn)
    filenames = filenames["filenames"]
    drefs = {}
    dw = {}
    for f in filenames:
        print("[+] Working on " + f)
        with open("../Resultados/map1/" + f + "-refs.json", "r") as trefs:
            tr = json.load(trefs)
        drefs = joinDictionaries(drefs, tr)
        with open("../Resultados/map1/" + f + "-pos.json", "r") as tpos:
            tp = json.load(tpos)
        dw = joinDictionaries(dw, tp)
    with open("../Resultados/reduce1/refs.json", "w") as refs:
        json.dump(drefs, refs)
    with open("../Resultados/reduce1/pos.json", "w") as pos:
        json.dump(dw, pos)
    print("[+] Done!")

if __name__ == "__main__":
    main()
