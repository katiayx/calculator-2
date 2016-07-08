"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.

# No setup
repeat forever:
    read input
    tokenize input
    if the first token is 'q'
        quit
    else
        decide which math function to call based on first token
"""

from arithmetic import *

arithmetic_string = raw_input("Please provide an operator (+, -, *, /, square, cube, pow, mod) and number(s):\n")

token = arithmetic_string.split(" ")
if len(token) >= '3':
    token[1] = int(token[1])
    token[2] = int(token[2])
else:
    token[1] = int(token[1])

if token[0] == "+":
    print add(token[1], token[2])

elif token[0] == "-":
    print subtract(token[1], token[2])

elif token[0] == "*":
    print multiply(token[1], token[2])

elif token[0] == "/":
    print divide(token[1], token[2])

elif token[0] == "square":
    print square(token[1])

elif token[0] == "cube":
    print cube(token[1])

elif token[0] == "pow":
    print power(token[1], token[2])

elif token[0] == "mod":
    print mod(token[1], token[2])

else:
    print "Looks like you did not provide an operator and two numbers, try again!"