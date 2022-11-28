from pycsp3 import *
#from pysat import *
from pysat.solvers import Solver, Minisat22

n, e = data
k = 8

s = Solver(name='g4')
z = []
e = sorted(e)
print(e, "\n")
lastarc = e[0]

for i in range(len(e)-1):
    nextarc = e[i+1]
    arc = e[i]
    if(lastarc[0] == arc[0]):
        if(abs(arc[0]-arc[1]) > abs(nextarc[0]-nextarc[1])):
            lastarc = arc
    else:
        if(abs(lastarc[0]-lastarc[1])<=k or abs(lastarc[0]-lastarc[1])>=n-k):
            z.append(lastarc)
        else:
            z.append([lastarc[0],-lastarc[1]])
        lastarc = arc


print("z" , z)
#print("s" , s.get_model())
#s.solve()
#s.delete()

with Minisat22(bootstrap_with=z) as m:
    m.solve()
    print("m" , m.get_model())

#print[z]