def addCollatzVariable(n, d):
    c = (n%2 == 0)*(n//2)+(n%2 == 1)*(n*3+1)
    if n in d.keys():
        return d
    elif c in d.keys():
        d[n] = [n]+d[c]
        return d
    else:
        return addCollatzVariable(n, addCollatzVariable(c, d))

def genCollatzDict(n):
    d = {2: [2,1]}
    for i in range(3,n+1):
        d = addCollatzVariable(i, d)
    return d

collatzDict = genCollatzDict(10000)

def itemSortKey(e):
    return len(e[1])

collatzDictSorted = {k: v for k, v in sorted(collatzDict.items(), key=lambda item: len(item[1]))}

longestCollatz = list(collatzDictSorted.items())[-1]

print("The longest chain is generated by the number {}, with a length of {}. Here is the chain: {} \n".format(longestCollatz[0],len(longestCollatz[1]),longestCollatz[1]))

shortestCollatz = [(k, v) for k, v in collatzDictSorted.items() if not k in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4098, 8192]][0]

print("The shortest chain which isn't generated by a power of two is generated by the number {}, with a length of {}. Here is the chain: {} \n".format(shortestCollatz[0],len(shortestCollatz[1]),shortestCollatz[1]))

collatzLengthAverage = sum([len(i) for i in collatzDict.values()])/len(collatzDict)

print("The average chain length is {}".format(collatzLengthAverage))
