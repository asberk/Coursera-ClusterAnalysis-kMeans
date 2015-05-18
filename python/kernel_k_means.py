from utils import * 
from math import exp 

def kernel(data, sigma):
    nData = len(data)
    Gram = [[0] * nData for i in range(nData)] 
    # TODO
    # Calculate the Gram matrix 
    ## exp(-norm(X_i-X_j)^2/(2*sigma**2))
    Gram = [ [rbf(data[j], data[k], sigma) for k in range(nData)] for j in range(nData) ]
    return Gram 

def rbf(x, y, sigma):
    return exp(- sum(map(lambda x,y: (x-y)**2, x, y)) / (2*sigma**2) )


