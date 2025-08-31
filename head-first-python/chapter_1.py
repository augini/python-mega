import random
import this


suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

faces = ["Jack", "Queen", "King", "Ace"]

numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def draw():
    the_suit = random.choice(suits)
    the_card = random.choice(faces + numbered)
    return the_card, "of", the_suit


deck = set()


while len(deck) < 5:
    hand = draw()
    deck.add(draw())

print(deck)

print(dir(deck))
print(help(deck.add))

#  Who does what

# random - can generate numbers in an unpredictable order
# collections - provides a bunch of advanced data types
# os - lets you interact with your underlying operating system
# itertools - for all your advanced looping needs
# http.server - it’s a built-in web server
# pdb - you can use this to debug your Python code
# pprint - this does the trick when your output needs to be pretty
# csv - processes a comma-delimited file of text
# stat - reports on a file’s modification date, for instance
# unittest - this module let’s you test your code one function at a time
# re - a regular expression library (not “line noise”)
# enum - a set of typed named values
# ssl - digital certs and encrypted connections rely on this module
# json - popular structured text format, sometimes call a “document”
# sys - tells you all about the system you’re running on
# zipfile - if your data’s compressed in a file, this module’s got your back
# sqlite3 - the world’s most popular embedded relational database system
