import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0])
NumOfTimes = int(arr[0])
num = 1

while NumOfTimes != 0:
    print(num,' Abracadabra')
    NumOfTimes = NumOfTimes - 1
    num = num + 1



