from pycsp3 import *
import time

n, e = data
interval=[0,n]
x = VarArray(size=n, dom=range(1,n+1))

def find(intervale):
    start = time.time()
    k=int((intervale[1]+intervale[0])/2)
    res = search(k)
    print("k:" + str(k) + ", res:" + str(res) + ", interval:" + str(intervale) + ", time:" + str(time.time() - start))
    if(intervale[1]-intervale[0] <= 2):
        print("Lower bound : " + str(k))
    elif(res is SAT):
        find([intervale[0], k])
    elif(res is UNSAT):
        find([k,intervale[1]])

def search(k):
    z = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (abs(i-j) <=k or abs(i-j)>=n-k) and i!=j:
                z.append((i,j))
    print(z.__sizeof__())
    satisfy(
        AllDifferent(x),
        [(x[i-1], x[j-1]) in z for i,j in e]
    )
    return solve(solver=ACE, options="-t=" + str(n) + "s")

find(interval)