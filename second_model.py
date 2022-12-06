from pycsp3 import *
import time

start = time.time()
n, e = data
x = VarArray(size=n, dom=range(1, n+1))

intervale = [1, n]
good = []
wrong = []


def find(intervale):
    z = []
    k = int((intervale[1]+intervale[0])/2)
    for i in range(1, n+1):
        for j in range(1, n+1):
            ##if(not abs(i-j)<=intervale[0]):
                if (abs(i-j)<=k or abs(i-j)>=n-k and i!=j):
                    z.append((i, j))

    print("e:" + str(len(e)) + " z:" + str(len(z)) + " x:" + str(len(x)))
    satisfy(
        AllDifferent(x),
        [(x[i-1], x[j-1]) in z for i, j in e]
    )
    res = solve(solver=ACE, options="-t=" + str(len(e)) + "s", sols=1)
    unpost()
    print("k:" + str(k) + ", res:" + str(res) + ", interval:" + str(intervale))
    if(time.time()-start <= 1600):
        if (intervale[1]-intervale[0] <= 1):
            if (res is SAT):
                print("time:"+str(time.time()-start)+", bound:" + str(k) + ", tries:["+str(len(good))+","+str(len(wrong))+"]")
            else:
                print("time:"+str(time.time()-start)+", bound:" + str(intervale[1]) + ", tries[ok,nok]:["+str(len(good))+","+str(len(wrong))+"]")
        elif (res is SAT):
            good.append(k)
            find([intervale[0], k])
        elif (res is UNSAT):
            wrong.append(k)
            find([k, intervale[1]])
        else:
            print("time:"+str(time.time()-start)+", bound:[" + str(intervale[0]) + "," + str(intervale[1]) + "], tries[ok,nok]:["+str(len(good))+","+str(len(wrong))+"]")
    else:
        print("timeout:"+str(time.time()-start)+", bound:[" + str(intervale[0]) + "," + str(intervale[1]) + "], tries[ok,nok]:["+str(len(good))+","+str(len(wrong))+"]")

find([1, n])
