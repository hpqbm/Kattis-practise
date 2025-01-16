
word = input("")

k_count = 0
b_count = 0
for letter in word:
    if letter == "k":
        k_count += 1
    if letter == "b":
        b_count += 1

if k_count > b_count:
    print("kiki")

if k_count < b_count:
    print("boba")

if k_count == b_count:
    if k_count != 0:
        if b_count != 0:
            print("boki")

if k_count == 0:
    if b_count == 0:    
        print("none")
    
    