def count_positive_negative(numbers):
    positive_count =0
    negative_count =0
    for num in numbers:
        if num>0:
            positive_count += 1
        elif num<0:   
            negative_count -= 1
    return (positive_count,negative_count) 
numbers=(-2,-3,-67,-7,2,5,9,8)      
print(count_positive_negative(numbers))
        
