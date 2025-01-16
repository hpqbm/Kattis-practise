import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0])

number = arr[0]
print( "{:.2f}".format(int(number) / 4))
