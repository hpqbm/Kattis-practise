
import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0].split(' '))

for ar in arr:
    print(abs(int(ar[0])-int(ar[1])))







