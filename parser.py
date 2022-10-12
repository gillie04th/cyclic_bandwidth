from pycsp3.problems.data.parsing import *

ne_line = next_line().split(" ")

data["n"] = number_in(ne_line[2])
next_line()

data["e"] = []


for rl in remaining_lines():
    print(rl.split(" "))
    print(data["e"])
    if(not int(rl.split(" ")[0]) in data["e"]):
        data["e"].append(int(rl.split(" ")[0]))
    else:
        print(data["e"][int(rl.split(" ")[0])])
        data["e"][int(rl.split(" ")[0])].append([int(rl.split(" ")[1])])

print(data)