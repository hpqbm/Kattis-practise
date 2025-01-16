import sys

oarr = []
for line in sys.stdin:
    if line == '\n':
        break
    oarr.append(line.split('\n')[0].split(' '))

move = oarr[-1][0]
print('move = ',move)
arr = []
for row in range(0,4):
    arr.append([0]*4)

for r in range(0,4):
    for c in range(0,4):
        arr[r][c] = int(oarr[r][c])


if move == '0': # left
    print("Left")
    for row in range(0,4):
        for col in range(3,0,-1):
            print(f'checking: {row},{col}')
            for left in range(col-1,-1,-1):
                if arr[row][left] == 0:
                    print(f'checking left: {row},{left}')
                    continue
                else:
                    if arr[row][col] == arr[row][left]:
                        arr[row][left] *= 2
                        #arr[row][col] = 0
                        for p in range(col,3):
                            arr[row][p] = arr[row][p+1]
                        arr[row][3] = 0
                        print(f'{arr[row][left]} added')
                    else:
                        break


if move == '1': # up
    for col in range(0,4):
        for row in range(3,0,-1):
            for up in range(row-1,-1,-1):
                if arr[up][col] == 0:
                    continue
                else:
                    if arr [row][col] == arr[up][col]:
                        arr[up][col] *= 2
                        #arr[row][col] = 0
                        for p in range(row,3):
                            arr[p][col] = arr[p+1][col]
                        arr[3][col] = 0
                        print(f'{arr[row][left]} added')
                    else:
                        break


 
  
if move == '2': # right
    for row in range(0,4):
        for col in range(0,3):
            for right in range(col+1,0):
                if arr[row][right] == 0:
                    continue
                else:
                    if arr[row][col] == arr[row][right]:
                        arr[row][right] *= 2
                        arr[row][col] = 0
                    else:
                        break
    

if move == '3': #down
    for col in range(0,4):
        for row in range(0,3):
            for down in range(row+1,0):
                if arr[down][col] == 0:
                    continue
                else:
                    if arr[row][col] == arr[down][col]:
                        arr[down][col] *= 2
                        arr[row][col] = 0
                    else:
                        break

print(arr)
