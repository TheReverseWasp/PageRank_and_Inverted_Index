import json

def main():
    # usin drefs == total references / page
    with open("../Resultados/Content/refs.json", "r") as refs:
        drefs = json.load(refs)
    # loading page graph
    with open("../Resultados/Content/pagegraph.json", "r") as pg:
        page_graph = json.load(pg)
    page_rank = {}
    acum = 0
    for k, v in page_graph.items():
        acum += 1
    for k, v in page_graph.items():
        page_rank[k] = 1 / acum
    for i in range(0, 3):
        for k, v in page_graph.items():
            acum = 0
            for k1, v1 in v.items():
                acum += page_rank[k1] / drefs[k1]
            page_rank[k] = acum
    with open("../Resultados/Content/PageRank.json", "w") as pr:
        json.dump(page_rank, pr)

if __name__ == "__main__":
    main()
