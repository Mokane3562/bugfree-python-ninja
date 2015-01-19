#########################################################
##  CS 4750 (Fall 2014), Assignment #3                 ##
##   Script File Name: CKYdet.py                       ##
##       Student Name: Michael Singleton               ##
##         Login Name: mnjs51                          ##
##              MUN #: 201103561                       ##
#########################################################

def tuple_key(i, j):
    tup = (i, j)
    return str(tup)

def CKY_DParse_2(words, G):
    P = {}
    for i in range(0, len(words)):
        for j in range(i+1, len(words)+1):
            key = tuple_key(i, j)
            P[key] = {}
            for N in G:
                P[key][N] = []
    for i in range(0, len(words)):
        key = tuple_key(i, i+1)
        for N in G:
            rules = G[N]
            for rule in rules:
                #print rule
                #print words[i]
                if words[i] in rule:
                    P[key][N].append(key)
    for i in range(0, len(words)):
        change = True
        while change is True:
            change = False
            key = tuple_key(i, i+1)
            for N in G:
                if len(P[key][N]) != 0:
                    for M in G:
                        rules = G[M]
                        for rule in rules:
                            if rule is N:
                                if len(P[key][M]) == 0:
                                    P[key][M].append(key)
                                    change = True
    for j in range(1, len(words)+1):
        for i in range(j-2, -1, -1):
            key = tuple_key(i, j)
            for k in range(i+1, j):
                for N in G:
                    rules = G[N]
                    for rule in rules:
                        parts = rule.split()
                        if len(parts) > 1:
                            key0 = tuple_key(i, k)
                            key1 = tuple_key(k, j)
                            if len(P[key0][parts[0]]) != 0:
                                if len(P[key1][parts[1]]) != 0:
                                    P[key][N].append(key0 + "->" + key1)
            change = True
            while change is True:
                change = False
                for N in G:
                    if len(P[key][N]) != 0:
                        for M in G:
                            rules = G[M]
                            for rule in rules:
                                if rule is N:
                                    if len(P[key][M]) == 0:
                                        P[key][M].append(key)
                                        change = True
    return P
    
def read_eCNF(file):
    grammer = {}
    with open(file, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            splits = line.split()
            non_terminal = splits[0]
            rule = ""
            for i in range(2, len(splits)):
                rule += splits[i]
            try:
                x = grammer[non_terminal]
                x.append(rule)
            except KeyError:
                grammer[non_terminal] = []
                x = grammer[non_terminal]
                x.append(rule)
    return grammer

def read_utterences(file):
    utterences = []
    with open(file, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            utterence = line.split()
            utterences.append(utterence)
    return utterences

if __name__ == "__main__":
    G = read_eCNF("g1.dcf")
    print G
    words = read_utterences("u2.utt")
    for line in words:
        print line
        cky = CKY_DParse_2(line, G)
        for i in range(0, len(line)):
            for j in range(i+1, len(line)+1):
                key = tuple_key(i, j)
                if key == tuple_key(0, len(line)):
                    print cky[key]
        print