
import math 

inp = []
Trap = " "
Mah = " "

for i in range(int(4)):
    inp.append(input(" "))

dia = int(inp[0])
base = int(inp[1])
top = int(inp[2])
height = int(inp[3])

Mahjong = ((dia/2)*(dia/2)*math.pi)
Trapizza = 1/2 * height * (base + top)


if Trapizza > Mahjong:
    print("Trapizza!")
if Trapizza < Mahjong:
    print("Mahjong!")
if Trapizza == Mahjong:
    print("Jafn storar!")

    