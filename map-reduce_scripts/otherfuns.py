def joinDictionaries(d1, d2):
    for k, v in d2.items():
        d1[k] = v
    return d1

def joinPageRank(d1, d2):
    for k, v in d2.items():
        if not k in d1:
            d1[k] = v
        else:
            for k2, v2 in v.items():
                if not k2 in d1[k]:
                    d1[k][k2] = v2
                else:
                    d1[k][k2] += v2
    return d1
