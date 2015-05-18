import sys
from LoadData import * 
from k_means import * 
from evaluation import * 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "[usage] <data-file> <ground-truth-file>"
        exit(1) 
    
    dataFilename = sys.argv[1]
    groundtruthFilename = sys.argv[2]
    
    data = loadPoints(dataFilename) 
    groundtruth = loadClusters(groundtruthFilename) 
    
    nDim = len(data[0]) 
   
    K = 3  # Suppose there are 2 clusters 
    
    centers = []
    for k in range(K):
        centers.append(data[k])
    

    
    results = kmeans(data, centers) 

    ## print groundtruth
    ## print results

    res_Purity = purity(groundtruth, results) 
    res_NMI = NMI(groundtruth, results) 
    
    print "Purity =", res_Purity
    print "NMI = ", res_NMI
    

