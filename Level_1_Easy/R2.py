import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0].split(' '))


print((2 * (int(arr[0][1]))) - int(arr[0][0]))
