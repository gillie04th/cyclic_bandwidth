from pycsp3 import *

n, e = data

# x[i] is the label of the ith node
x = VarArray(size=n, dom=range(1,n+1))

satisfy(
    AllDifferent(x)
    #x[0]==1,
    #x[0]<x[n-1],
)

minimize(
    Maximum(min(abs(x[i-1] - x[j-1]), n - abs(x[i-1] - x[j-1])) for i, j in e)
)

#print(x)