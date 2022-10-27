from pickle import TRUE
from pycsp3 import *

n, e = data
CB = 7

x = VarArray(size=n, dom=range(1,n+1))
y = VarArray(size=len(e), dom=range(1,CB+1))

satisfy(
    AllDifferent(x),
    CB in y ==TRUE,
    [(interval <= CB) | (interval>=n-CB) for interval in y],
    [abs(x[edge[0]-1] - x[edge[1]-1]) == y[idx] for idx,edge in enumerate(e)]

)

#solve()