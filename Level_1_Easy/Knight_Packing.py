import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0].split(' '))

a = int(arr[0][0])

if a % 2 == 0:
    print('second')
elif a % 2 == 1:
    print('first')
    


    
