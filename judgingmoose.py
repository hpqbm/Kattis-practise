
inp = input()

inp.split(" ")

if int(inp[0]) == int(inp[2])  & int(inp[0]) != 0:
    print(f"Even {int(inp[0]) + int(inp[2])}" )
elif int(inp[0]) == int(inp[2])  & int(inp[0]) == 0:
    print("Not a moose")

if int(inp[0]) > int(inp[2])  & int(inp[0]):
    print(f"Odd {int(inp[0])*2}")
else:
    print(f"Odd {int(inp[2])*2}")