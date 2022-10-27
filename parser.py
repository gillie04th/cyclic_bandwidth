from pycsp3.problems.data.parsing import *

ne_line = next_line().split(" ")

data["n"] = number_in(ne_line[0])
next_line()

data["e"] = []

for rl in remaining_lines():
    data["e"].append([int(rl.split(" ")[0])])
    data["e"][-1].append(int(rl.split(" ")[1]))

print(data)