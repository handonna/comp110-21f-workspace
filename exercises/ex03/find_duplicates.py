"""Finding duplicate letters in a word."""

__author__ = "123456789"

i: str = input("Enter an word: ")
j: int = 0
is_true: int = 0

while (j < len(i)):
    k: int = 1
    while (k < len(i)):
        if (i[j] == i[k]):
            is_true += 1
        k += 1
    j += 1

if is_true >= 1:
    print("Found duplicate: True")
if is_true == 0:
    print("Found duplicate: False")
