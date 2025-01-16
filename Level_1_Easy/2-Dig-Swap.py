import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0].split(' '))
a = int(arr[0][0])

def swapper():
    ten = a // 10
    one = a % 10
    result = one * 10 + ten
    print( result )

swapper()


