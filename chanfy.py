
inp = []

for i in range(2):
    inp.append(input(" "))

if int(inp[0]) < int(inp[1]):
    print(int(inp[0])*2)
else:
    print(int(inp[1])*2)