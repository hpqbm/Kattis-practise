import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0].split(' '))

print(arr[0][0], ' ',  arr[0][0], ' ',  arr[0][0])



