import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.strip('\n')[0])

print(arr)
X = int(arr[0])
Y = int(arr[1])

if X > 0 and Y > 0: {
    print(1)
}
elif X < 0 and Y > 0:{
    print(2)
}
elif X < 0 and Y < 0:{
    print(3)
}
elif X > 0 and Y < 0:{
    print(4)
}


