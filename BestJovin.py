
inp = []
highest = int(-9999999)
name = ''
inpn = input("")
for i in range(int(inpn)):
    val = input(" ")
    sval = val.split(" ")
    if int(sval[1]) > highest:
        highest = int(sval[1])
        name = sval[0]

print(name)

