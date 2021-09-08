"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730400224"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
guess=(randint(1,4))
a=guess
if a == 1:
    print("You will experience something fun soon.")
else: 
    if guess ==2:
        print("Something surprising will happen to you.")
    if guess ==3:
        print("You will have some fun adventures.")
    if guess ==4:
        print("Your future is bright.")
print("Now, go spread positive vibes!")