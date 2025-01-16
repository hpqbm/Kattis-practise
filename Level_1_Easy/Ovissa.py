def count_letters(input_string):
    letters_count = sum(1 for char in input_string if char.isalpha())
    return letters_count

user_input = input(" ")

result = count_letters(user_input)
print(result)