from pycsp3 import *

n, e = data
CB = 7

x = VarArray(size=n, dom=range(1,n+1))
#y = VarArray(size=len(e), dom=range(1,CB+1))
z = []

for i in range(1,n+1):
    for j in range(1,n+1):
        if (abs(i-j) <=CB or abs(i-j)>=n-CB) and i!=j:
            z.append((i,j))
            z.append((j,i))
satisfy(
    AllDifferent(x),
    [(x[i-1], x[j-1]) in z for i,j in e]
)

#solve()