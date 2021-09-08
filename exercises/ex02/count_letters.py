"""Counting letters in a string."""

__author__ = "730400224"


# Begin your solution here...
letter: str=input("What letter do you want to search for?: ")
word: str=input("Enter a word: ")
i: int = 0
lettercount = 0
while(i<len(word)):
    if(word[i]==letter):
        lettercount = lettercount+1
    i=i+1

print("Count: ", lettercount)