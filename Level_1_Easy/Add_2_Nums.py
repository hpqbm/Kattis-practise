import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0].split(' '))

a = int(arr[0][0])
b = int(arr[0][1])

print(a+b)
