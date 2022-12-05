import os
import sys
from os import listdir
from os.path import isfile, join

### 

files = [
    #"ash85",
    #"bcspwr01",
    #"bcspwr02",
    #"curtis54",
    #"ibm32",        # 9 pour le min en model2
    #"pores_1",
    "steam3",
    #"will57",
    #"bcsstk01",
    #"impcol_b"
]
#files = [f for f in listdir("data/") if isfile(join("data/", f))]
if(sys.argv[1] != "third"):
    for file in files:
        os.system('python3 ' + sys.argv[1] + '_model.py -data=data/' + file + '.mtx.rnd -dataparser=parser.py -solver=[ace,v,args="-t=' + sys.argv[2] + 's"]')
else:
    for file in files:
        os.system('python3 ' + sys.argv[1] + '_model.py -data=data/' + file + '.mtx.rnd -dataparser=parser.py')