"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *
list_of_operators = ['+','-','*','/','square','cube','pow','mod','q']
list_of_functions = [add, subtract, multiply, divide, square, cube, power, mod]

while True:
    user_input = raw_input()
    tokens = user_input.split(" ")
    print tokens

    # for operator in list_of_operators:
    for i in range(len(list_of_operators)):
        if tokens[0] == list_of_operators[i]:
            if (tokens[0] != 'square' and tokens[0] != 'cube'):
        # if tokens[0] == operator :
                print list_of_functions[i](float(tokens[1]), float(tokens[2]))
            else:
                print list_of_functions[i](float(tokens[1]))

