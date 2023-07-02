def sum_list(numbers):
    total=0
    for num in numbers:
        total+= num
    return total    
numbers = [1, 2, 4, 6, 9]
print(sum_list(numbers))