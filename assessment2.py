def amount_vowels(string):
    vowels='aeiou'
    count=0
    for char in string:
        if char in vowels:
            count +=1
    return count
string = "a, b, g, t, o, y, e,z"
num_vowels = amount_vowels(string)
print(num_vowels)