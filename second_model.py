from pycsp3 import *
import time

start = time.time()
n, e = data
x = VarArray(size=n, dom=range(1,n+1))

intervale = [1,n]

def find(intervale):
    z = []
    k=int((intervale[1]+intervale[0])/2)
    for i in range(1,n+1):
        for j in range(1,n+1):
            #if([i-1,j-1] in e or [j-1,i-1] in e):
                if (abs(i-j) <=k or abs(i-j)>=n-k) and i!=j:
                    z.append((i,j))
    print("e:" + str(len(e)) + " z:" + str(len(z)) + " x:" + str(len(x)))
    satisfy(
        AllDifferent(x),
        [(x[i-1], x[j-1]) in z for i,j in e]
    )
    res = solve(solver=ACE, options="-t=" + str(n) + "s", sols=1)
    unpost()
    print("k:" + str(k) + ", res:" + str(res) + ", interval:" + str(intervale))
    if(intervale[1]-intervale[0] <= 1):
        if(res is SAT):
            print("Lower bound is " + str(k))
        else:
            print("Lower bound is " + str(intervale[1]))
        print("time:" + str(time.time() - start))
    elif(res is SAT):
        find([intervale[0], k])
    elif(res is UNSAT):
        find([k,intervale[1]])


find([1,n])