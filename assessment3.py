from collections import Counter

def count_chars(string):
    return Counter(string)

string = "The quick brown fox jumps over the lazy dog."
char_counts = count_chars(string)
print(char_counts)
