import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0])

final = 0
for i in range(1, int(arr[0])+1):
    if len(arr) <= 2:
        final = int(arr[1])
        break
    if i == 1:
        final = int(arr[1])
        continue
    final = final + int(arr[i]) - 1

print(final)