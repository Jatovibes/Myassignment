def long_words(words): 
 return[word for word in words if len(word)>4]
words=['Apple', 'Ball', 'Cup', 'Tiger']
print(long_words(words))