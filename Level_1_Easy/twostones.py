import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0])

N = int(arr[0])
while N > 2:
    N = N - 2
    
if N == 1:
    print('Alice')
if N == 2:
    print('Bob')