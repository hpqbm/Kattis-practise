
import math

array = []

num = int(input(""))

for i in range(1, (num + 1)):
    array.append(input(""))

IsItOdd = ""
IsItASquare = ""
for n in array:
    if n % 2 == 1:
        IsItOdd = "yes"
    else:
        IsItOdd = "no"
    
    math.sqrt(n)

