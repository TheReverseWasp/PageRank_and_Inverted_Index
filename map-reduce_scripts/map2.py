#!/usr/bin/env python3

import json
import re
import sys

for f in sys.stdin:
    f = f[:-1]
    print("[+] Working in " + f)
    with open("../Resultados/reduce1/pos.json" , "r") as pos:
        dw = json.load( pos)
    page_rank_graph = {}
    with open("../Resultados/map1/" + f + "-content.json", "r") as jf:
        # all the reference from document k
        df = json.load(jf)
    for k, v in dw.items():
        if k in df:
            if not f in page_rank_graph:
                page_rank_graph[f] = {}
            if not v in page_rank_graph[f]:
                page_rank_graph[f][v] = 0
            page_rank_graph[f][v] += 1
    with open("../Resultados/map2/" + f + "-pagegraph.json", "w") as pg:
        json.dump(page_rank_graph, pg)
print("[+] Done!")
