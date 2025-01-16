
inp = []
inpn = int(input())

for i in range(inpn):
    inp.append(int(input(" ")))

rev = inp[::-1]

for i in range(inpn):
   print(rev[i])