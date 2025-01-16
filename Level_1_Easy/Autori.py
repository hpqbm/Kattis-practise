import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0].split(' '))

temp = arr[0][0].split('-')
result = ''
for e in temp:
   result = result + e[0] 

print(result)