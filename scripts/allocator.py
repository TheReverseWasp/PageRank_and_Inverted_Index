import json
import re

def main():
    r = "[a-z]+"
    with open("filenames.json", "r") as fn:
        allfn = json.load(fn)
    # Map refs
    print("iniciando mapeo de referencias")
    # dic of page: location
    dw = {}
    # Number of refs per file
    drefs = {}
    # word and page Content
    print("begin")
    for k in allfn["filenames"]:
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
        with open("../Resultados/Content/" + k + "-content.json", "w") as js:
            json.dump(df, js)
    with open("../Resultados/Content/refs.json", "w") as refs:
        json.dump(drefs, refs)
    with open("../Resultados/Content/pos.json" , "w") as pos:
        json.dump(dw, pos)

if __name__ == "__main__":
    main()
