from pycsp3 import *

n, e = data

# x[i] is the label of the ith node
x = VarArray(size=n, dom=range(n))

satisfy(
    AllDifferent(x)
)
minimize(
    Maximum(min(abs(x[i] - x[j]), n - abs(x[i] - x[j])) for i, j in e)
)

#solve()
