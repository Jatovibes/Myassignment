def find_max(numbers):
    max_num = None
    for num in numbers:
        if max_num is None or num > max_num:
            max_num = num
    return max_num
numbers=[1,4,55,89,45,23]
max_num = find_max(numbers)
print("The largest number is:", max_num)
