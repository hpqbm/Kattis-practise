input_string = input("")

index_of_a = input_string.find('a')

if index_of_a != -1:
    new_string = input_string[index_of_a:]
    print(new_string)
