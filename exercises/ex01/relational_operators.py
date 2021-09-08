"""This is the relational operators assignment to use relational operator functions."""
Left: str = input("Left-hand side: ")
Right: str = input("Right-hand side: ")
a = int(Left)
b = int(Right)
less = a < b
print((a), "<", (b), "is", (less))
greaterorequal = a >= b
print((a), ">=", (b), "is", (greaterorequal))
equal = a == b
print((a), "==", (b), "is", (equal))
inequality = a != b
print((a), "!=", (b), "is", (inequality))

__author__ = "730400224"