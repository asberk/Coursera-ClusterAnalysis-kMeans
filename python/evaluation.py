from math import log, sqrt

def  purity(groundtruthAssignment, algorithmAssignment):

    purity = 0
    # TODO  
    # Compute the purity 
    purity_table = table(algorithmAssignment, groundtruthAssignment)
    print len(algorithmAssignment), len(groundtruthAssignment)
    for j in range(max(algorithmAssignment)+1):
        try:
            purity += max(purity_table[j])
        except IndexError:
            print j 
            print purity_table
    
    purity = purity / len(groundtruthAssignment)
    return purity 


def NMI(groundtruthAssignment, algorithmAssignment):
    NMI = 0
    # TODO
    # Compute the NMI
    nPts = len(algorithmAssignment)
    P_CT = table(algorithmAssignment, groundtruthAssignment, nPts)
    P_C = [ float(algorithmAssignment.count(k))/nPts for k in range(max(algorithmAssignment)+1)]
    P_T = [ float(groundtruthAssignment.count(k))/nPts for k in range(max(groundtruthAssignment)+1)]
    NMI = information(P_CT, P_C, P_T)/sqrt(entropy(P_C)*entropy(P_T))
    return NMI


def table(a,b, nmz=None):
    nCols = max(b)+1
    nRows = max(a)+1
    abtab = [[0]*nCols for _ in range(nRows)]
    if not len(a) == len(b):
        raise ValueError('required that len(a) = len(b)')
    for j in range(len(a)):
        abtab[a[j]][b[j]] += 1.
    if nmz:
        for j in range(nRows):
            for k in range(nCols):
                abtab[j][k] = abtab[j][k]/nmz
    return abtab


def entropy(px):
    pxnz = [x for x in px if not x==0]
    IC = map(lambda x: x*log(x), pxnz)
    return -reduce(lambda x,y: x+y, IC)

## ab = joint pmf of variables a & b
##  a = marginal of a : a[j] = sum_k ab[j][k]
##  b = marginal of b : b[k] = sum_j ab[j][k]
def information(ab, a, b):
    info = 0
    for j in range(len(a)):
        for k in range(len(b)):
            if ab[j][k] == 0:
                continue
            info += ab[j][k]*log(ab[j][k]/(a[j]*b[k]))
    return info
    
