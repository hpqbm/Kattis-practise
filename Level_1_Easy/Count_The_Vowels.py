def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = input('')
num_vowels = count_vowels(input_string)
print(num_vowels)



