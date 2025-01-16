
inp = []
for i in range(3):
    inp.append(input(""))

names = ["Monnei", "Fjee", "Dolladollabilljoll"]
smallest_index = 0
for i in range(1,3):
    if int(inp[i]) < int(inp[smallest_index]):
        smallest_index = i

print(names[smallest_index])


