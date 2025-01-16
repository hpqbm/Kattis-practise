
number = input("")

words = []

for i in range(1,(int(number) + 1)):
    words.append(input(""))

for index, a in enumerate(words):
    if index % 2 == 0:
        print(a)






