# Read the input string
input_string = input().strip()

# Extract the number of 'e's
num_es = input_string.count('e')

# Construct the output with double the 'e's
output_string = 'h' + 'e' * (2 * num_es) + 'y'

# Print the output
print(output_string)