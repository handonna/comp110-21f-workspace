"""This is the numeric operators assignment to print messages from number variables."""
Left: str = input("Left-hand side: ")
Right: str = input("Right-hand side ")
a = int(Left)
b = int(Right)
power = a**b
print ((a), "**", (b), "is", (power))
divide = a/b
print ((a), "/", (b), "is", (divide))
floor = a // b
print ((a), "//", (b), "is", (floor))
mod = a % b
print ((a), "%", (b), "is", (mod))

__author__ = "730400224"
