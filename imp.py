
inp = []
inpn = int(input(""))

for i in range(inpn):
    inp.append(input(""))

flag = 0
if 'keys' not in inp:
    print("keys")
    flag=1
if 'phone' not in inp:
    print("phone")
    flag=1
if 'wallet' not in inp:
    print("wallet")
    flag=1
if flag != 1:
    print("ready")


