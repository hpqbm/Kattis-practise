
number = input("")

ls = []
final = 10000000000000000000

for i in range(1,(int(number) + 1)):
    ls.append(input(""))

for j in ls:
    if int(j) < final:
        final = int(j)

print(final)


    