#!/usr/bin/env python3

import json
from otherfuns import *

def main():
    with open("filenames.json", "r") as fn:
        filenames = json.load(fn)
    filenames = filenames["filenames"]
    page_rank_graph = {}
    for f in filenames:
        print("[+] Working with file " + f)
        with open("../Resultados/map2/" + f + "-pagegraph.json", "r") as pg:
            filePG = json.load(pg)
        page_rank_graph = joinPageRank(page_rank_graph, filePG)
    with open("../Resultados/reduce2/pagegraph.json", "w") as prg:
        json.dump(page_rank_graph, prg)

if __name__ == "__main__":
    main()
