from pycsp3 import *

n, e = data
k = 8

x = VarArray(size=n, dom=range(1,n+1))
#y = VarArray(size=len(e), dom=range(1,CB+1))
z = []

for i in range(1,n+1):
    for j in range(1,n+1):
        if (abs(i-j) <=k or abs(i-j)>=n-k) and i!=j:
            z.append((i,j))
satisfy(
    AllDifferent(x),
    [(x[i-1], x[j-1]) in z for i,j in e]
)

print(z)

#solve()