from itertools import izip, islice, tee

def ngramFunction(string, n):
    return list(izip(*(islice(j, i, None) for i,j in enumerate(tee(string,n)))))