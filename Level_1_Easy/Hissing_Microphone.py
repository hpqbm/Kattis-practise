import sys

arr = []
for line in sys.stdin:
    if line == '\n':
        break
    arr.append(line.split('\n')[0].split(' '))



def check_ss(str):

    if 'ss' in str:
        print('hiss')
    else:
        print('no hiss')


check_ss(arr[0][0])




        



