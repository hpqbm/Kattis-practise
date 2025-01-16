
num = int(input(""))

hangover = 0

conditions = []
for i in range(1, (num + 1)):
    conditions.append(input())
 
for index, c in enumerate(conditions):
    if index == 0:
        continue
    if ((c == "sober") & (conditions[index - 1] == "sober")):
        continue
    if ((c == "sober") & (conditions[index - 1] == "drunk")):
        hangover += 1
        continue
    if ((c == "drunk") & (conditions[index - 1] == "drunk")):
        continue
    if ((c == "drunk") & (conditions[index - 1] == "sober")):
        continue

print(hangover)
