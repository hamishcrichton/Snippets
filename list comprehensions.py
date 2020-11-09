#Useful usages

characters = [char for char in full_name]

row_max = [max(row) for row in Matrix]

ceiling_numbers0 = [number if number <= max_value else max_value for number in numbers] 

cart_prod = [(i,j) for i in a for j in b]

common_list = [i for i in a if i in b]

num = [1, 2, 3, 4], double_num = map(lambda x: x + x, num)


#Using if/else

L1 = [name for name in name_list if name.startswith('Y')]

L2 = [name for name in name_list if name.startswith('Y') or len(name) < 4]

L3 = [name for name in name_list if len(name) < 4 and name.islower()]

L4 = [name if name.startswith('y') else 'Not Present' for name in name_list]


#Using a boolean function
four_legs_pets = [pet.capitalize() for pet in pets if has_four_legs(pet)]


#Using a method
L1 = [name.capitalize() for name in name_list]


#Adding a second level of list
L1 = [char for name in name_list for char in name]
L1 = [char for name in name_list if len(name) < 4 for char in name]


#map() function returns an iterable object, and thus we can use the list() function to generate a list from this iterable
map(function, iterable)
pets = ('bird', 'snake', 'dog', 'turtle', 'cat', 'hamster')
uppercased_pets = list(map(str.upper, pets))
#uppercased_pets returns ['BIRD', 'SNAKE', 'DOG', 'TURTLE', 'CAT', 'HAMSTER']


#Using a Walrus operator
>>> letters = list('this is to produce a list of letters')
>>> letters
['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 't', 'o', ' ', 'p', 'r', 'o', 'd', 'u', 'c', 'e', ' ', 'a', ' ', 'l', 'i', 's', 't', ' ', 'o', 'f', ' ', 'l', 'e', 't', 't', 'e', 'r', 's']
>>> import random
>>> vowels = [letter.upper() for _ in range(0, 10) if (letter := random.choice(letters)) in list('aeoui')]
>>> vowels
['I', 'O', 'O', 'O', 'O']


# syntax for set comprehension

{expression for item in iterable}

>>> numbers = (1, 34, 5, 8, 10, 12, 3, 90, 70, 70, 90)
>>> unique_even_numbers = {number for number in numbers if number%2 == 0}
>>> unique_even_numbers
{34, 70, 8, 10, 12, 90}


# syntax for dict comprehension

{key_expression : value_expression for item in iterable}

>>> words = ('python', 'is', 'a', 'big', 'snake')
>>> len_words = {word : len(word) for word in words}
>>> len_words
{'python': 6, 'is': 2, 'a': 1, 'big': 3, 'snake': 5}

>>> len_words_p = {word : len(word) for word in words if word.startswith('p')}
>>> len_words_p
{'python': 6}
