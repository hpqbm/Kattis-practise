def decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)[2:]  
    return binary_representation

def reverse_binary(binary_representation):
    reversed_binary = binary_representation[::-1]
    return reversed_binary

decimal_input = int(input(" "))

binary_result = decimal_to_binary(decimal_input)
reversed_binary_result = reverse_binary(binary_result)


print(int(reversed_binary_result, 2))