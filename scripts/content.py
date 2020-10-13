import json
import re

def main():
    with open("filenames.json", "r") as fn:
        allfn = json.load(fn)
    # Page Rank Prev
    # and dw == pages of certain domain (filename)
    with open("../Resultados/Content/pos.json" , "r") as pos:
        dw = json.load( pos)
    page_rank_graph = {}
    for f in allfn["filenames"]:
        print("iniciando... " + f)
        with open("../Resultados/Content/" + f + "-content.json", "r") as jf:
            # all the reference from document k
            df = json.load(jf)
        for k, v in dw.items():
            if k in df:
                if not f in page_rank_graph:
                    page_rank_graph[f] = {}
                if not v in page_rank_graph[f]:
                    page_rank_graph[f][v] = 0
                page_rank_graph[f][v] += 1
    with open("../Resultados/Content/pagegraph.json", "w") as pg:
        json.dump(page_rank_graph, pg)


if __name__ == "__main__":
    main()
