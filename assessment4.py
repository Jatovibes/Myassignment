def reverse_string(input_string):
    output_string = ""
    for i in range(len(input_string)-1, -1, -1):
        output_string += input_string[i]
    return output_string
input_string = "My name is Josh"
output_string = reverse_string(input_string)
print("The reversed string is:", output_string)