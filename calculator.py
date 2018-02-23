#!/usr/bin/env python
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)
#Welcome Message

welcome = """
 _    _      _                          
| |  | |    | |                         
| |  | | ___| | ___ ___  _ __ ___   ___ 
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ /
\  /\  /  __/ | (_| (_) | | | | | |  __/
 \/  \/ \___|_|\___\___/|_| |_| |_|\___/      

Welcome To Shining Dev's basic Python calculator.
\n      
"""
r1 = "[*] Use operators such as +, -, *, / \n"
r2 = "[*] You're only limited to 2 numbers \n"
r3 = "[*] More bugs coming soon :) \n"
r4 = "[*] You'll need a space for every digit, EX: 1 + 1, 2 * 2, 3 - 3, 4 / 4\n"


printout(welcome, RED)
printout(r1, GREEN)
printout(r2, GREEN)
printout(r3, GREEN)


# Store the user input of 2 numbers and the operator of choice
num1, operator, num2 = input("Enter Calculation: ").split()

# Convert the trings into integers
num1= float(num1)
num2 = float(num2)
# if they enter +, -, *, /, then we need to provide output based on operator

if operator == "+":
    print("{} + {} = {}".format(num1,num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1,num2, num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1,num2, num1*num2))
elif operator == "/":
    print("{} / {} = {}".format(num1,num2, num1/num2))
else:
    print("Syntax error")

