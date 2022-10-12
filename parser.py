from pycsp3.problems.data.parsing import *

ne_line = next_line().split(" ")

data["n"] = number_in(ne_line[2])
next_line()

data["e"] = []


for rl in remaining_lines():
    print(rl.split(" "))
    print(data["e"])
    if(int(rl.split(" ")[0]) in data["e"]):
        
        data["e"][int(rl.split(" ")[0])].append([int(rl.split(" ")[1])])
    else:
        data["e"].append(int(rl.split(" ")[0]))

print(data)