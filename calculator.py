"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
# accept input from user

while True:
    user_input = input('> ')
    tokens = user_input.split(' ')
    print(tokens[0])
    
    if tokens[0] == '+':
        # add(tokens[1], tokens[2])
        result = float(tokens[1]) + float(tokens[2])
    elif tokens[0] == '-':
        # subtract(tokens[1], tokens[2])
        print(float(tokens[1]) - float(tokens[2]))

    print(result)



# tokenize input
# check elements/items in arithmetic file
# run function that corresponds to token 
# display answer from user's input
