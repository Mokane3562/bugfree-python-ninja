#########################################################
##  CS 4750 (Fall 2014), Assignment #3                 ##
##   Script File Name: CKYprb.py                       ##
##       Student Name: Michael Singleton               ##
##         Login Name: mnjs51                          ##
##              MUN #: 201103561                       ##
#########################################################

import math


def tuple_key(i, j):
    tup = (i, j)
    return str(tup)

def CKY_PParse_3(words, G):
    P = {}
    for i in range(0, len(words)):
        for j in range(i+1, len(words)+1):
            key = tuple_key(i, j)
            P[key] = {}
            for N in G:
                P[key][N] = (-1, float("-inf"))
    for i in range(0, len(words)):
        key = tuple_key(i, i+1)
        for N in G:
            rules = G[N]
            for value in rules:
                (rule, prob) = value
                if words[i] in rule:
                    P[key][N] = (key, math.log(float(prob)))
        change = True
        while change is True:
            change = False
            for N in G:
                (bestIndex, bestProb) = P[key][N]
                if bestIndex != -1:
                    for M in G:
                        rules = G[M]
                        for value in rules:
                            (rule, x) = value
                            if N is rule:
                                (index, prob) = P[key][M]
                                if index == -1:
                                    P[key][M] = (key, bestProb + math.log(float(x)))
                                    change = True
    for j in range(1, len(words)+1):
        for i in range(j-2, -1, -1):
            key = tuple_key(i, j)
            for k in range(i+1, j):
                for N in G:
                    rules = G[N]
                    for value in rules:
                        (rule, prob) = value
                        parts = rule.split()
                        if len(parts) > 1:
                            key0 = tuple_key(i, k)
                            key1 = tuple_key(k, j)
                            (index0, prob0) = P[key0][parts[0]]
                            if prob0 > float("-inf"):
                                (index1, prob1) = P[key1][parts[1]]
                                if prob1 > float("-inf"):
                                    (bestIndex, bestProb) = P[key][N]
                                    if bestProb < log(float(prob)) + prob0 + prob1:
                                        P[key][N] = (key0+"->"+key1, log(float(prob)) + prob0 + prob1)
            change = True
            while change is True:
                change = False
                for N in G:
                    (bestIndex, bestProb) = P[key][N]
                    if bestIndex != -1:
                        for M in G:
                            rules = G[M]
                            for value in rules:
                                (rule, x) = value
                                if N is rule:
                                    (index, prob) = P[key][M]
                                    if prob < bestProb + math.log(float(x)):
                                        P[key][M] = (key, bestProb + math.log(float(x)))
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
            for i in range(2, len(splits)-1):
                rule += splits[i]
            try:
                x = grammer[non_terminal]
                x.append((rule, splits[ len(splits)-1 ]))
            except KeyError:
                grammer[non_terminal] = []
                x = grammer[non_terminal]
                x.append((rule, splits[ len(splits)-1 ]))
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
    G = read_eCNF("g2.pcf")
    print G
    words = read_utterences("u2.utt")
    for line in words:
        print line
        cky = CKY_PParse_3(line, G)
        for i in range(0, len(line)):
            for j in range(i+1, len(line)+1):
                key = tuple_key(i, j)
                if key == tuple_key(0, len(line)):
                    print cky[key]
        print