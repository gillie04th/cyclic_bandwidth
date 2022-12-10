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
    #"ibm32",
    #"pores_1",
    #"steam3",
    #"will57",
    ##"bcsstk01",
    ##"impcol_b",
    #"bcspwr03",
    #"bcsstk22",
    "dwt__234",
    ##"nos4",

]
#files = [f for f in listdir("data/") if isfile(join("data/", f))]
if(sys.argv[1] == "first"):
    for file in files:
        print(file + ":")
        os.system('python3 ' + sys.argv[1] + '_model.py -data=data/' + file + '.mtx.rnd -dataparser=parser.py -solver=[ace,v,args="-t=' + sys.argv[2] + 's"] -ev')
elif(sys.argv[1] == "second"):
    for file in files:
        print(file + ":")
        os.system('python3 ' + sys.argv[1] + '_model.py -data=data/' + file + '.mtx.rnd -dataparser=parser.py -solver=[ace,v,args="-t=' + sys.argv[2] + 's"] -ev ')#> out_' + file + '$(date +"%s").txt')
else:
    for file in files:
        print(file + ":")
        os.system('python3 ' + sys.argv[1] + '_model.py -data=data/' + file + '.mtx.rnd -dataparser=parser.py ')#> out_' + file + '$(date +"%s").txt')

os.system('rm solver*.log *.mtx.xml')