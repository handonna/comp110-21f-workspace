"""Repeating a beat in a loop."""

__author__ = "730400224"


# Begin your solution here...
beat = input("What beat do you want to repeat? ")
maximum = int(input("How many times do you want to repeat it? "))
count = maximum
while count >0:
    print(beat)
    count -= 1
else: 
    if maximum <= 0:
        print("No beat...")