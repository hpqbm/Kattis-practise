def count_vowels_and_y(input_string):
    vowels = "aeiouAEIOU"
    y = "yY"
    
    num_vowels = sum(1 for char in input_string if char in vowels)
    num_vowels_and_y = sum(1 for char in input_string if char in vowels + y)
    
    print(f"{num_vowels} {num_vowels_and_y}")

# Example usage:
input_string = input(" ")
count_vowels_and_y(input_string)

