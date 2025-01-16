def reverse_binary(n):
    binary_representation = bin(n)[2:]
    
    reversed_binary = binary_representation[::-1]
    
    return reversed_binary

number = int(input(" "))
reversed_binary = reverse_binary(number)
print(reversed_binary)