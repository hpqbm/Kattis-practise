import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0].split(' '))
    
Base = int(arr[0][0])
Height = int(arr[0][1])

print((0.5 * Base * Height ))
