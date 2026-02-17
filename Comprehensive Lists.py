# Comprehensive list: 


# 1.	Write a list comprehension to generate squares of numbers from 1 to 10. 
square = [x**2 for x in range(1, 11)]
print (square)

# 2.	Create a list of even numbers between 1 and 50 using list comprehension. 
even = [x for x in range(1, 51) if x % 2 == 0]
print (even)

# 3.	Convert all strings in a list to uppercase using list comprehension. 
list1 = ["apple", "banana", "orange"]
upper = [s.upper() for s in list1]
print (upper)

# 4.	Given a list of integers, create a new list that contains only the positive numbers. 
num = [-5, 3, -2, 8, 0, 4]
positive = [x for x in num if x > 0]
print (positive)

# 5.	Create a list of tuples (num, num^2) for numbers 1 to 5. 
pair = [(x, x**2) for x in range(1, 6)]
print (pair)

# 6.	Extract all vowels from a given string using list comprehension. 
text = "Python Training"
vowel = [ch for ch in text if ch.lower() in "aeiou"]
print (vowel)

# 7.	Flatten a 2D list using list comprehension. 
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print (flat)

# 8.	Replace all negative numbers in a list with 0 using list comprehension. 
num = [-2, 5, -1, 4, -3]
result = [x if x >= 0 else 0 for x in num]
print (result)

# 9.	Given a list of words, create a list of lengths of each word. 
word = ["Piyush", "Siya", "Rajat"]
length = [len(word) for word in word]
print (length)

# 10.	Filter out words that start with the letter 'A' or 'a'. 
word = ["Apple", "banana", "Ant", "cat"]
new1 = [w for w in word if not w.lower().startswith('a')]
print (new1)

# 11.	From a list of numbers, generate a list of “even” or “odd” strings using list comprehension. 
num = [4,1,9,2, 3, 5, 8, 10]
even_odd = ["even" if x % 2 == 0 else "odd" for x in num]
print (even_odd)

# 12.	Create a list of numbers divisible by both 3 and 5 in range 1–100. 
div = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print (div)

# 13.	Write a nested list comprehension to generate a multiplication table for 1–5. 
table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
print (table) 

# 14.	Convert a dictionary’s keys into a list using list comprehension. 
d = {"a": 1, "b": 2, "c": 3}
keys = [k for k in d]
print (keys)

# 15.	Extract numeric digits from a string using list comprehension.
text = "Python8756"
digit = [ch for ch in text if ch.isdigit()] 
print (digit)

# 16.	Use list comprehension to remove all spaces from a string. 
text = "Bizmetric Python Training"
space = [ch for ch in text if ch != " "]
result = "".join(space)
print (result)

# 17.	Create a list of characters that appear more than once in a string. 
text = "programming"
lst = [ch for ch in set(text) if text.count(ch) > 1]
print (lst)

# 18.	From a list of sentences, generate a list of all words (split using list comprehension). 
sentences = ["Today is Monday", "This is a cat"]
word = [word for sent in sentences for word in sent.split()]
print (word)

# 19.	Create a list of unique elements from a list using list comprehension + condition. 
lst = [1, 2, 2, 3, 4, 4, 5]
unique = [x for i, x in enumerate(lst) if x not in lst[:i]]
print (unique)

# 20.	Generate all pairs (x, y) where x is from list A and y is from list B (cartesian product).
A = [1, 2, 3]
B = ['a', 'b']

pair = [(x, y) for x in A for y in B]
print (pair)



