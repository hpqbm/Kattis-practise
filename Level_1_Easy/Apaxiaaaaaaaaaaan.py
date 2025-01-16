def compact_name(name):
    if not name:
        return name  

    compact_version = name[0] 
    for i in range(1, len(name)):
        if name[i] != name[i - 1]:
            compact_version += name[i]

    return compact_version

input_name = input(" ")
result = compact_name(input_name)
print( result )
