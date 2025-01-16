
num_ppl = int(input(" "))
all = []
while num_ppl != 0:
    Food = {}
    for i in range(num_ppl):
        t = input("")
        vals = t.split(" ")
        for v in vals[1:]:
            if v not in Food.keys():
                Food[v] = [vals[0]]
            else:
                Food[v].append(vals[0])
    all.append(Food)
    num_ppl = int(input(" "))

for a in all:
    for k in Food.keys():
        vv = [' '.join(j) for j in Food[k]]
        print(f"{k} {vv}")
    print("")

