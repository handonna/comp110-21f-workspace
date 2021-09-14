"""Repeating a beat in a loop."""

__author__ = "730400224"


# Begin your solution here...
beat = str(input("What beat do you want to repeat? "))
maximum = (int(input("How many times do you want to repeat it? ")))
count = maximum
string = str(beat)
add = maximum - 1
while count > 0:
    repeated = (((string) + " ") * (add) + string)
    print(repeated)
    count -= maximum
else: 
    if maximum <= 0:
        print("No beat...")