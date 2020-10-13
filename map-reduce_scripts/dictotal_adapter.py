import json

with open("../Resultados/reduce3/dicfile.json", "r") as dfile:
    dictotal = json.load(dfile)
with open("dicfile.txt", "w") as dresult:
    for k, v in dictotal.items():
        dresult.write(k + "\n")
