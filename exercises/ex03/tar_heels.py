"""An exercise in remainders and boolean logic."""

__author__ = "730400224"


# Begin your answer here
i: int = int(input("Enter an int: "))
if i % 2 == 0:
    print("TAR")
else:
    if i % 7 == 0:
        print("HEELS")
    if i % 2 == 0 and i % 7 == 0:
        print("TAR HEELS")
    if i % 2 != 0 and i % 7 != 0:
        print("CAROLINA")
