from pycsp3 import *
from pysat.solvers import Minisat22
from threading import Timer
import time

tempsDepart=time.time()

def interrupt(s):
    s.interrupt()

def thirdModel(interval,n,e,contrainte,X):
    impossible=[]
    cb=int((interval[0]+interval[1])/2)

    ## Ensemble impossible d'arete en fonction du cb
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (abs(i-j) >cb  and abs(i-j)<n-cb) and i!=j:
                impossible.append((i,j))
    
    newContrainte=[]
    for newC in contrainte:
        newContrainte.append(newC)

    clause=[]
    for i,j in e:
        for a,b in impossible:
                clause.append([-X[i-1][a-1],-X[j-1][b-1]]) # Pas d'étiquette ne respectant pas le cb en focntion de e
                clause.append([-X[i-1][b-1],-X[j-1][a-1]]) 

    for c in clause:
        newContrainte.append(c)

    ## Résolution
    m=Minisat22(bootstrap_with=newContrainte)
    timer = Timer(10, interrupt, [m])
    timer.start()
    print(interval)
    print(cb)
    if(m.solve_limited(assumptions=[1],expect_interrupt=True)):

        if interval[1]-interval[0] == 2:
            print("SOLVABLE")
            result=[]
            i=0
            for res in m.get_model():
                if res>0:
                    result.append(res-(n*i))
                    i=i+1
            print(result)
            timer.cancel()
            tempsFin=time.time()
            print(tempsFin-tempsDepart)
        else:
            print("solv")
            interval[1]=int((interval[0]+interval[1])/2)
            thirdModel(interval,n,e,contrainte,X)
    else:
        if interval[1]-interval[0] == 2:
            print("unsolv")
            interval[1]=interval[1]+1
            interval[0]=interval[0]+1
            thirdModel(interval,n,e,contrainte,X)
        elif interval[1]-interval[0] == 1:
            print("unsolv")
            interval[1]=interval[1]+1
            thirdModel(interval,n,e,contrainte,X)
        else:
            print("unsolv")
            interval[0]=cb
            thirdModel(interval,n,e,contrainte,X)

    
n, e = data
interval=[0,n]
## Creation n*n variable 
X =[[j for j in range(1,n+1)] for i in range(n)] # X[i][j] : etiquette i sur le sommet j
contrainte= []
i=0
for k in X:
    for j in range(len(k)):
        k[j]=n*i+k[j]
    i=i+1


## Creation des clauses
for k in X:
    clause_e1=[]
    for j in k:
        clause_e1.append(j) # Au moins un sommet par etiquette
        for j2 in k:
            if j!=j2:
                contrainte.append([-j,-j2]) # Au plus un sommet par etiquette
    contrainte.append(clause_e1) 
    for k2 in X:
        if X.index(k) != X.index(k2):
            for j in range(0,n):
                contrainte.append([-k[j] , -k2[j]]) # Pas deux étiquette sur le meme sommet

thirdModel(interval,n,e,contrainte,X)