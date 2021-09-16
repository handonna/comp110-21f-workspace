"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

i: int = int(input("Depth: "))
j: int = 1

if i > 0:
    while (j < i + 1):
        print(TREE * j)
        j += 1