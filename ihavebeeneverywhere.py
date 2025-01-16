
num_sets = int(input(" "))
final = []
for i in range(num_sets):
    vals = []
    n_vals = int(input(""))
    for j in range(n_vals):
        t = input("")
        if t not in vals:
            vals.append(t)
    final.append(len(vals))

for i in range(len(final)):
    print(final[i])
