from utils import * 


def computeSSE(data, centers, clusterID):
    sse = 0 
    nData = len(data) 
    for i in range(nData):
        c = clusterID[i]
        sse += squaredDistance(data[i], centers[c]) 
        
    return sse 

def updateClusterID(data, centers):
    nData = len(data) 
    
    clusterID = [0] * nData
    
    # TODO 
    # assign the closet center to each data point
    for j in range(nData):
        for k in range(len(centers)):
            if squaredDistance(data[j], centers[k]) < squaredDistance(data[j], centers[clusterID[j]]):
                clusterID[j] = k
    
    return clusterID

# K: number of clusters 
def updateCenters(data, clusterID, K):
    nDim = len(data[0])
    centers = [[0] * nDim for i in range(K)]

    # TODO recompute the centers based on current clustering assignment
    # If a cluster doesn't have any data points, in this homework, leave it to ALL 0s
    for k in range(K):
        nClusterPts = clusterID.count(k)
        if nClusterPts == 0:
            continue
        ClusterPts = [data[d] for d in range(len(data)) if clusterID[d] == k]
        centers[k] = divByConst(reduce(add, ClusterPts), nClusterPts)
    return centers 

def kmeans(data, centers, maxIter = 100, tol = 1e-6):
    nData = len(data) 
    
    if nData == 0:
        return [];

    K = len(centers) 
    
    clusterID = [0] * nData
    
    if K >= nData:
        for i in range(nData):
            clusterID[i] = i
        return clusterID

    nDim = len(data[0]) 
    
    lastDistance = 1e100
    
    for iter in range(maxIter):
        clusterID = updateClusterID(data, centers) 
        centers = updateCenters(data, clusterID, K)
        
        curDistance = computeSSE(data, centers, clusterID) 
        if lastDistance - curDistance < tol or (lastDistance - curDistance)/lastDistance < tol:
            print "# of iterations:", iter 
            print "SSE = ", curDistance
            return clusterID
        
        lastDistance = curDistance
        
    print "# of iterations:", iter 
    print "SSE = ", curDistance
    return clusterID


def add(a,b):
    return map(sum, zip(a,b))

def divByConst(myList, constant):
    return [myList[j]/constant for j in range(len(myList))]
