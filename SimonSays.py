
num = int(input(""))
lines = []
arr = []
for i in range(num):
    lines.append(input(""))

for j in range(num):
    if "Simon Says " in lines[j]:
        lines[i].split("\n")
        arr.append(lines[j][3])

print(arr)
