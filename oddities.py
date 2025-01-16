
num = int(input(""))

arr = []
for i in range(1 , (num + 1)):
    arr.append(input(""))

for index in arr:
    if int(index) % 2 == 0:
        print(f"{index} is even")
    else:
        print(f"{index} is odd")
