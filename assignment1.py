def multiply_even_numbers(numbers):
    product=1
    for num in numbers:
        if num%2 ==0:
            product*=num
    return product
numbers = [2,3,4,5,7,8,]        
print(multiply_even_numbers(numbers))           
